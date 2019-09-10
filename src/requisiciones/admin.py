from django.contrib import admin
from requisiciones.models import Requisicion, RequesicionEstatus, RequesicionTipo, Cotizacion, CategoriaEstado
# Register your models here.
admin.site.register(Requisicion)
admin.site.register(RequesicionEstatus)
admin.site.register(RequesicionTipo)
admin.site.register(Cotizacion)
admin.site.register(CategoriaEstado)