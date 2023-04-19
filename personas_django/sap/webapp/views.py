from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def bienvenido(request): #request contiene informacion de la peticion que se envia desde el navegador al serv django
    return HttpResponse('Hola mundo desde Django')
def despedirse(request):
    return HttpResponse('Adios')