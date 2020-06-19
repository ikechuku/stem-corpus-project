from rest_framework import routers
from .apis import InfoViewSet, ArticleViewSet, PortfolioViewSet

router = routers.DefaultRouter()
router.register('stem/details', InfoViewSet, 'Info')
router.register('stem/bio', ArticleViewSet, 'Bio')
router.register('stem/portfolio', PortfolioViewSet, 'Portfolio')



urlpatterns = router.urls