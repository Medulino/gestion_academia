from django.shortcuts import render, get_object_or_404
from .models import Curso


def lista_cursos(request):
    cursos = Curso.objects.filter(
    activo=True
    ).order_by(
    'fecha_inicio')
    return render(request, "cursos/lista_cursos.html", {"cursos": cursos})


def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id, activo=True)
    return render(
        request,
        "cursos/detalle_curso.html", 
        {"curso": curso}, 
    )

