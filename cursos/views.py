from django.shortcuts import render, get_object_or_404
from .models import Curso


def lista_cursos(request):
    cursos = Curso.objects.filter(
    activo=True
    ).order_by(
    'fecha_inicio')
    return render(request, "cursos/lista_cursos.html", {"cursos": cursos})



def detalle_curso(request, curso_id):
    # 1. Primero se obtiene el curso de la base de datos
    curso = get_object_or_404(Curso, pk=curso_id, activo=True)

    # 2. Después se calculan las plazas ocupadas usando .count()
    ocupadas = curso.matriculas.count()

    # 3. Finalmente se pasan las variables al contexto del render
    return render(
        request,
        "cursos/detalle_curso.html",
        {"curso": curso, "ocupadas": ocupadas},
    )
