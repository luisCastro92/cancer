from django.http import response
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import TejidoMama

# Create your views here.
def inicio(request):
    #print("Mi Primer Hola Mundo En Django")
    return render(request, 'cancerWebApp/inicio.html')

def grafos(request):
    #lista = [1,2,3,4,5]
    #return render(request, 'cancerWebApp/grafos.html', {'miMensaje': lista}) #diccionario de contexto
    listaDatos = TejidoMama.objects.all()
    return render(request, 'cancerWebApp/grafos.html', {'datos': listaDatos }) #diccionario de contexto

def gramaticas(request):
    return render(request, 'cancerWebApp/gramaticas.html')