from django.db import models
from applications.departamento.models import departamentoDB
from ckeditor.fields import RichTextField

# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad',max_length=50)

    class Meta:
        verbose_name='Habilidad' #Como quiero que se llame en la web
        verbose_name_plural='Habilidades de los empleados' #nombre en plural
        unique_together=('habilidad',) #no se puede repetir el nombre

    def __str__(self):
        return str(self.id)+'-'+self.habilidad

class EmpleadoDB(models.Model):

    JOB_CHOICES=(
        ('0','Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )

    nombre = models.CharField('Nombre',max_length=50)
    apellido = models.CharField( 'apellido',max_length=50)
    empleo = models.CharField(max_length=1, choices=JOB_CHOICES, blank=True)
    departamento = models.ForeignKey(departamentoDB, on_delete=models.CASCADE, default=1)
    #imagen = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida= RichTextField()
    class Meta:
        verbose_name='Empleado' #Como quiero que se llame en la web
        verbose_name_plural='Empleados de la empresa' #nombre en plural
        ordering=['apellido'] #ordenar por nombre de forma descendente con -
        unique_together=('nombre','apellido') #no se puede repetir el nombre y el short_name

    def __str__(self):
        return  str(self.id)+'-'+self.nombre+'-'+self.apellido+'-'+self.empleo +'-'+str(self.departamento)
