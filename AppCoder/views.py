from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import *
from django.template import loader
# Create your views here.
def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HTTPResponse( documento)

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

def alta_curso(request, nombre):
    curso = Curso(nombre= nombre , camada= 287318)
    curso.save()
    texto = f"Se guardo en la BD el Curso: {curso.nombre} Camada: {curso.camada}"
    return HTTPResponse (texto)

def cursoFormulario(request):
    if request .method == "POST":
        mi_formulario = CursoFormulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
        
        curso= Curso(nombre=datos['nombre'], camada= datos['camada'])
        curso.save()
        
        return render(request, "AppCoder/cursoFormulario.html")
    return render(request, "AppCoder/cursoFormulario.html")

def buscar_curso(request):
    return render(request, "AppCoder/buscar_curso.html")

def buscar(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render( request, "AppCoder/resultado_busqueda.html", {"cursos": cursos} )
    else:
        return HTTPResponse("Campo vacio")