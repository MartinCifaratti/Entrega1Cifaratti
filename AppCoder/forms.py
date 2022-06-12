from socket import fromshare
from django import forms

class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()