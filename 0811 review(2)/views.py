from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Review
from .serializers import ReviewSerializer



# 리뷰 조회, 작성
class ReviewView(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        serializser = ReviewSerializer(data=request.data)
        if serializser.is_valid():
            serializser.save()
            return Response(serializser.data, status=status.HTTP_201_CREATED)
        
        return Response(serializser.errors, status=status.HTTP_400_BAD_REQUEST)

    
# 특정 리뷰 조회, 수정, 삭제    

class ReviewDetailView(APIView):
    def get(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    def put(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        serializer = ReviewSerializer(Review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
                                    
        