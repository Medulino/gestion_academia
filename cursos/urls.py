from django.urls import path
from .views import lista_cursos,detalle_curso
urlpatterns = [
    path('',lista_cursos,name='lista_cursos'),
    path('',lista_cursos),
    path('<slug:slug>/',detalle_curso,name='detalle_curso'),
]