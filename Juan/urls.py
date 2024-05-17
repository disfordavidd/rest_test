from rest_framework import routers
from .api import ProjectViewSetLampara

router = routers.DefaultRouter()

router.register('api/lampara', ProjectViewSetLampara, 'lampara')

#urlpatterns = []

urlpatterns = router.urls