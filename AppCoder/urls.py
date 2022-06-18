from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name = "Inicio"),
    path('cursos', views.cursos, name = "Cursos"),
    path('profesores', views.profesores, name = "Profesores"),
    path('estudiantes', views.estudiantes, name = "Estudiantes"),
    path('entregables', views.entregables, name = "Entregables"),
    #path('cursoFormulario', views.cursoFormulario, name = "CursoFormularios"),
    path('alta_curso', views.cursoFormulario, name = "altacurso"),
    path('buscar_curso', views.buscar_curso, name = "buscarcurso"),
    path('buscar', views.buscar),
    path('formularioprofesor', views.formularioprofesor),
]


