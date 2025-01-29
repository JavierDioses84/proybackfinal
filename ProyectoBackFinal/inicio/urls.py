from rest_framework import routers, viewsets

from inicio.models import Servicios
from inicio.serializar import ServSerializer

class ServViewSet(viewsets.ModelViewSet):
    queryset = Servicios.objects.all()
    serializer_class = ServSerializer


router = routers.DefaultRouter()
router.register(r'servsr', ServViewSet, basename='servr')

urlpatterns = router.urls