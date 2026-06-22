from urllib import request

from django.shortcuts import render, get_object_or_404
from .models import Curso
from django.db.models import Q
from profesores.models import Profesor
from django.core.paginator import Paginator

def lista_cursos(request):
    busqueda = request.GET.get('buscar', '')
    profesor_id = request.GET.get('profesor','')


    cursos = Curso.objects.filter(activo=True)
    profesores = Profesor.objects.all()

    paginator = Paginator(
        cursos,
        6
    )

    page_number = request.GET.get(
        'page'
    )

    cursos = paginator.get_page(
        page_number
    )

    if busqueda:
        cursos = cursos.filter(
            Q(nombre__icontains=busqueda) | 
            Q(descripcion__icontains=busqueda)
        )

    if profesor_id:
        cursos= cursos.filter(profesor_id=profesor_id)

    return render(
        request, 
        'cursos/lista_cursos.html', 
        {
            'cursos': cursos, 
            'busqueda': busqueda,
            'profesores': profesores,
            'profesor_id' : profesor_id
        }
    )




def detalle_curso(
    request,
    slug
    ):
    curso = get_object_or_404(
        Curso,
        slug=slug,
        activo=True
    )
    ocupadas = (
        curso.matriculas.count()
    )
    return render(
        request,
        'cursos/detalle_curso.html',
        {
            'curso': curso,
            'ocupadas': ocupadas,
        }
    )
