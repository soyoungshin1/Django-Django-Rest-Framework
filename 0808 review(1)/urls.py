from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WineReviewViewSet

router = DefaultRouter()
router.register(r'wine_reviews', WineReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

'''
#router 사용
이로 인해 WineReviewViewSet에 대해 자동으로 다음과 같은 URL 패턴이 생성됩니다:
GET /wine_reviews/ : 모든 리뷰 목록 조회
POST /wine_reviews/ : 새로운 리뷰 생성
GET /wine_reviews/{id}/ : 특정 리뷰 조회
PUT /wine_reviews/{id}/ : 특정 리뷰 수정
DELETE /wine_reviews/{id}/ : 특정 리뷰 삭제
'''

