from django.urls import path
from . import views
from . import views 
urlpatterns = [
    path('', views.main),          
    path('create/',views.create,name='create'),
    path('detail/<int:pk>/',views.detail,name='detail'),
    path('update/<int:pk>/',views.update,name='update'),
    path('delete/<int:pk>/',views.delete,name='delete')
]