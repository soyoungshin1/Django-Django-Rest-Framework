from django.urls import path,include
from .views import ReviewView,ReviewDetailView


urlpatterns = [
    path('', ReviewView.as_view(), name='review_list_create'),
    path('detail/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    ]
