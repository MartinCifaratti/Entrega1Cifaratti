from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name = "Inicio"),
    path('curso', views.cursos, name = "Cursos"),
    path('profesores', views.profesores, name = "Profesores"),
    path('estudiantes', views.estudiantes, name = "Estudiantes"),
    path('entregables', views.entregables, name = "Entregables"),
    path('cursoFormulario', views.cursoFormulario, name = "CursoFormularios"),
    path('alta_curso', views.cursoFormulario),
    path('buscar_curso', views.buscar_curso),
    path('buscar', views.buscar),
]


