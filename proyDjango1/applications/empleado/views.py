from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from applications.empleado.models import EmpleadoDB


# Create your views here.

class IndexView(TemplateView):
    template_name= 'home/home.html'

class PruebaListaView(ListView):
    template_name='home/lista.html'
    queryset=['A','B','C']
    context_object_name = 'lista_prueba'

class empleadoListView(ListView):
    model = EmpleadoDB
    template_name = "home/empleadodb.html"
    context_object_name = 'lista_empleado'

