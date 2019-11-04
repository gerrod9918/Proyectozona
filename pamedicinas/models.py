from django.db import models
from django.contrib import admin
from django.utils import timezone


class Medicina(models.Model):
    nombre  =   models.CharField(max_length=30)
    descripcion = models.CharField(max_length=1000)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):

        return self.nombre


class Notificacion(models.Model):
    paciente = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo    = models.CharField(max_length=60)
    descripcion      = models.CharField(max_length=1000)
    medicinas   = models.ManyToManyField(Medicina, related_name="get_medicinas", through='Tiene')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_compra = models.DateTimeField(blank=True, null=True)

    def confirmado(self):
        self.fecha_compra = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo


class Tiene (models.Model):
    medicina = models.ForeignKey(Medicina, on_delete=models.CASCADE)
    notificacion = models.ForeignKey(Notificacion, on_delete=models.CASCADE)



class TieneInLine(admin.TabularInline):
    model = Tiene
    extra = 1


class MedicinaAdmin(admin.ModelAdmin):
    inlines = (TieneInLine,)


class NotificacionAdmin (admin.ModelAdmin):
    inlines = (TieneInLine,)
