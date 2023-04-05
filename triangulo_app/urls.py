from rest_framework import routers
from .viewsets import transformadorviewset, nombreviewset

router = routers.SimpleRouter()
router.register('transformadores', transformadorviewset)
router.register('nombre', nombreviewset)

urlpatterns = router.urls
