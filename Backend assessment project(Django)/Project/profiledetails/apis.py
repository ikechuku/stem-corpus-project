from  .models import Info, Article, Portfolio
from rest_framework import viewsets, permissions
from .serializers import InfoSerializer, ArticleSerializer , PortfolioSerializer

#Details Viewset
class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    # related_name = 'Details_code'
    serializer_class = InfoSerializer

# Bio viewsets
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    permission_classes = [
        permissions.AllowAny,
        # related_name = 'Bio_code',
    ]
    
    serializer_class = ArticleSerializer

# Portfolio viewsets

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    permission_classes = [
        permissions.AllowAny,
        # related_name = 'Bio_code',
    ]
    
    serializer_class = PortfolioSerializer