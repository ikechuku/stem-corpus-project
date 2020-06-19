from rest_framework import serializers
from . import models


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Info
        fields = '__all__'
    
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'
        # '__all__'
class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Portfolio
        fields = '__all__'