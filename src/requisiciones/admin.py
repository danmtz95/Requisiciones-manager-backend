from django.contrib import admin
from requisiciones.models import Requisicion, RequisicionEstado, RequesicionEstatus, RequesicionTipo, Cotizacion, CategoriaEstado, ReporteCompras, CotizacionCompras, EstatusCompras, CompraRapida
# Register your models here.
admin.site.register(Requisicion)
admin.site.register(RequesicionEstatus)
admin.site.register(RequesicionTipo)
admin.site.register(RequisicionEstado)
admin.site.register(Cotizacion)
admin.site.register(CategoriaEstado)
admin.site.register(ReporteCompras)
admin.site.register(CotizacionCompras)
admin.site.register(EstatusCompras)
admin.site.register(CompraRapida)