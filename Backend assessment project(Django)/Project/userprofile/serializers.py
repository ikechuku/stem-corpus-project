from rest_framework import serializers
from . import models


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Details
        fields = '__all__'
    
class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bio
        fields = '__all__'
        
    