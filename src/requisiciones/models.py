from django.db import models
from django.contrib.auth.models import User
from clientes.models import Cliente

# Create your models here.
class RequesicionTipo(models.Model):
    concepto = models.CharField(max_length=250)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_creacion = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.concepto


class RequesicionEstatus(models.Model):
    EN_ESPERA = 1
    ACEPTADO = 2
    RECHAZADO = 3

    concepto = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)
    tiempo = models.CharField(max_length=250)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_creacion = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.concepto


class Cotizacion(models.Model):
    fecha = models.DateTimeField()
    folio = models.CharField(max_length=250)
    monto = models.FloatField()
    orden_proveedor = models.CharField(max_length=250)
    usuario_creacion = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Requisicion(models.Model):
    fecha_correo = models.DateTimeField()
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE
    )
    tipo = models.ForeignKey(
        RequesicionTipo, on_delete=models.CASCADE
    )
    estatus = models.ForeignKey(
        RequesicionEstatus, on_delete=models.CASCADE
    )
    cotizacion = models.ForeignKey(
        Cotizacion, on_delete=models.CASCADE, blank=True, null=True
    )
    nota = models.CharField(max_length=250)
    usuario_creacion = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)