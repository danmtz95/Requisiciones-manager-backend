from django.conf.urls import url, include
from authentication import views
from rest_framework import routers
from clientes.views import ClientesViewSet

router = routers.SimpleRouter()
router.register(r"clientes", ClientesViewSet, "clientes")

urlpatterns = [
    url("/", include(router.urls))
]
