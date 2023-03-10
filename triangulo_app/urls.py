from rest_framework import routers
from .viewsets import transformadorviewset

router = routers.SimpleRouter()
router.register('transformadores', transformadorviewset)

urlpatterns = router.urls
