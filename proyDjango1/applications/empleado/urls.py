from django.urls import path
from . import views

urlpatterns = [
    path('empleado/', views.IndexView.as_view()),
    path('lista/',views.PruebaListaView.as_view()),
    path('empleados/', views.empleadoListView.as_view())
]

