from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Requisicion(models.Model):
    fecha_correo = models.DateTimeField()
    nota = models.CharField(max_length=250)
    usuario_creacion = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)