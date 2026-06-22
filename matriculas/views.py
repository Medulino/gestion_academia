from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from cursos.models import Curso
from .models import Matricula

@login_required
def matricularse(request, curso_id):
    """Gestiona la inscripción de un alumno en un curso activo."""
    curso = get_object_or_404(Curso, pk=curso_id, activo=True)

    # Validación de tipo de usuario
    if getattr(request.user, 'tipo', None) != "alumno":
        messages.error(request, "Sólo los alumnos pueden matricularse.")
        return redirect("detalle_curso", curso_id=curso.id)

    # Validación de aforo disponible
    inscritos = curso.matriculas.count()
    if inscritos >= curso.plazas:
        messages.error(request, "No quedan plazas disponibles para este curso.")
        return redirect("detalle_curso", curso_id=curso.id)

    # Registro seguro de la matrícula
    matricula, creada = Matricula.objects.get_or_create(
        alumno=request.user, 
        curso=curso
    )

    if creada:
        messages.success(request, "Matrícula realizada correctamente.")
    else:
        messages.warning(request, "Ya estás matriculado en este curso.")

    return redirect("detalle_curso", curso_id=curso.id)


@login_required
def mis_cursos(request):
    """Lista los cursos del alumno optimizando las consultas del profesor."""
    matriculas = Matricula.objects.filter(
        alumno=request.user
    ).select_related(
        "curso",
        "curso__profesor",
        "curso__profesor__usuario"
    )
    return render(
        request, "matriculas/mis_cursos.html", {"matriculas": matriculas}
    )


@login_required
def dashboard(request):
    """Muestra el panel de control del alumno con datos consolidados."""
    total_matriculas = Matricula.objects.filter(alumno=request.user).count()
    
    # Optimización: Carga el curso y profesor en una sola query SQL
    ultimas_matriculas = (
        Matricula.objects.filter(alumno=request.user)
        .select_related(
            'curso',
            'curso__profesor',
            'curso__profesor__usuario'
        )
        .order_by('-fecha_matricula')[:5]
    )
    
    # Optimización: Al iniciar desde Curso, reducimos los saltos del JOIN
    proximo_curso = (
        Curso.objects.filter(matriculas__alumno=request.user)
        .select_related(
            'profesor',
            'profesor__usuario'
        )
        .order_by('fecha_inicio')
        .first()
    )
    
    return render(
        request,
        'matriculas/dashboard.html',
        {
            'total_matriculas': total_matriculas,
            'ultimas_matriculas': ultimas_matriculas,
            'proximo_curso': proximo_curso,
        }
    )


@login_required
@require_POST
def cancelar_matricula(request, matricula_id):
    """Cancela una matrícula existente de forma segura mediante POST."""
    matricula = get_object_or_404(
        Matricula,
        pk=matricula_id,
        alumno=request.user
    )
    matricula.delete()
    messages.success(request, 'Matrícula cancelada correctamente.')
    return redirect('mis_cursos')
