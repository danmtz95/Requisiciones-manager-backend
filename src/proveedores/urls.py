from django.conf.urls import url, include
from authentication import views
from rest_framework import routers
from proveedores.views import ProveedoresViewSet

router = routers.SimpleRouter()
router.register(r"proveedores", ProveedoresViewSet, "proveedores")

urlpatterns = [
    url("/", include(router.urls))
]
