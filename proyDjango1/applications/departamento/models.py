from django.db import models

# Create your models here.

class departamentoDB(models.Model):
    name = models.CharField('Nombre', max_length=50, blank=True) #editable=False -> no podran editarlo desde el navegador
    short_name = models.CharField('Nombre Corto', max_length=20, unique=True) #, null=True -> si no se ingresa nada, se guarda como null
    anulate = models.BooleanField('Anulado',default=False)
    fecha = models.DateField()

    def __str__(self):
        return str(self.id)+'-'+self.name+'-'+self.short_name+'-'+str(self.fecha) +'-'+str(self.anulate)
