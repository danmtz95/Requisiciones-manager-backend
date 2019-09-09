from django.contrib import admin
from requisiciones.models import Requisicion, RequesicionEstatus, RequesicionTipo, Cotizacion
# Register your models here.
admin.site.register(Requisicion)
admin.site.register(RequesicionEstatus)
admin.site.register(RequesicionTipo)
admin.site.register(Cotizacion)