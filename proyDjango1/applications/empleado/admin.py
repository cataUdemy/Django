from django.contrib import admin

from applications.empleado.models import EmpleadoDB, Habilidades

# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'apellido',
        'departamento',
        'empleo',
    )

admin.site.register(EmpleadoDB, EmpleadoAdmin)