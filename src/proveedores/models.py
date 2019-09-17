from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proveedor(models.Model):
    nombre_fiscal = models.CharField(max_length=150)
    rfc = models.CharField(max_length=20)
    direccion = models.CharField(max_length=150 ,default='')
    nombre_comercial = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.CharField(max_length=150)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_creacion = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre_fiscal