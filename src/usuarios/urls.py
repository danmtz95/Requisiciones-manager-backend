from django.conf.urls import url, include
from authentication import views
from rest_framework import routers
from usuarios.views import UsuariosViewSet

router = routers.SimpleRouter()
router.register(r"usuarios", UsuariosViewSet, "usuarios")

urlpatterns = [
    url("/", include(router.urls))
]
