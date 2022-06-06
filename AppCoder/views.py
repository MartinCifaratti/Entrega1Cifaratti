import http
from http.client import HTTPResponse
from django.shortcuts import render
from django.template import Template, context
from django.template import loader


# Create your views here.
def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    return render(request, 'AppCoder/cursos.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')
