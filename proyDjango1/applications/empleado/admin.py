from django.contrib import admin

from applications.empleado.models import EmpleadoDB, Habilidades

# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin): #para mostrar tabla de empleados
    list_display = (
        'id',
        'nombre',
        'apellido',
        'departamento',
        'empleo',
        'full_name', #no existe en empleado, debo crearlo con una fn
    )

    #funcion para full_name
    def full_name(self, obj): #obj es el objeto que se esta iterando
        return obj.nombre + ' ' + obj.apellido
    #para que se pueda buscar por nombre y apellido
    search_fields = ('nombre','apellido')
    list_filter = ('departamento','habilidades') #aparece como filtro, la , es pq es una tupla

    #para que se pueda editar desde la tabla
    list_editable = ('empleo',)

    #para que se pueda paginar
    list_per_page = 4

    #para que se pueda ordenar por nombre y apellido
    ordering = ('apellido',)

    #para que se pueda filtrar por habilidades
    filter_horizontal = ('habilidades',)


admin.site.register(EmpleadoDB, EmpleadoAdmin)