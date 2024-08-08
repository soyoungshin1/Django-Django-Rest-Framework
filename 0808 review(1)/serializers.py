from rest_framework import serializers
from .models import WineReview

class WineReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = WineReview
        fields = ['id', 'wine_name', 'title', 'comment', 'rating']
