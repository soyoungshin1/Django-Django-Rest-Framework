from rest_framework import viewsets
from .models import WineReview
from .serializers import WineReviewSerializer

class WineReviewViewSet(viewsets.ModelViewSet):
    queryset = WineReview.objects.all()
    serializer_class = WineReviewSerializer
