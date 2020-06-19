from rest_framework import routers
from .restapi import ProfileViewSet

router = routers.DefaultRouter()
router.register('restapi/Profile', ProfileViewSet, 'Profile')

urlpatterns = router.urls