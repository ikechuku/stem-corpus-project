from  .models import Details, Bio
from rest_framework import viewsets, permissions
from .serializers import DetailsSerializer, BioSerializer

#Details Viewset
class DetailsViewSet(viewsets.ModelViewSet):
    queryset = Details.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    # related_name = 'Details_code'
    serializer_class = DetailsSerializer

# Bio viewsets
class BioViewSet(viewsets.ModelViewSet):
    queryset = Bio.objects.all()
    permission_classes = [
        permissions.AllowAny,
        # related_name = 'Bio_code',
    ]
    
    serializer_class = BioSerializer