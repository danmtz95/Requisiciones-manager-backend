from django.conf.urls import url, include
from authentication import views
from rest_framework import routers
from requisiciones.views import RequisicionesViewSet

router = routers.SimpleRouter()
router.register(r"requisiciones", RequisicionesViewSet, "requisiciones")

urlpatterns = [
    url("/", include(router.urls))
]
