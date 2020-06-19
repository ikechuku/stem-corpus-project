from rest_framework import routers
from .crud import DetailsViewSet, BioViewSet

router = routers.DefaultRouter()
router.register('crud/details', DetailsViewSet, 'Details')
router.register('crud/bio', BioViewSet, 'Bio')


urlpatterns = router.urls