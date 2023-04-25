from django.db import models
from applications.departamento.models import departamentoDB

# Create your models here.

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
    #imagen = models.ImageField()

    def __str__(self):
        return  str(self.id)+'-'+self.nombre+'-'+self.apellido+'-'+self.empleo +'-'+str(self.departamento)
