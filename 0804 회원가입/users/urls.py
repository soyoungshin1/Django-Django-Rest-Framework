from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('signup/',views.signup, name='signup'),
    path('<int:pk>/', views.get_user, name='get_user'), #조회
    path('<int:pk>/update/', views.update_user, name='update_user'), #수정
    path('<int:pk>/delete/', views.delete_user, name='delete_user'), #삭제
    #path('login/', views.login, name='login'), # 로그인
   
]