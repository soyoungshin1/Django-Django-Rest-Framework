from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer

'''
json 형식의 샘플데이터 
{
    "email": "user@example.com",
  	"name": "John Doe",
    "password": "securepassword"
    
}
'''
#초기 화면
def index(request):
    return render(request, 'users/index.html')

#회원가입
@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#회원정보 조회    
@api_view(['GET'])
def get_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#회원정보 수정
@api_view(['PUT'])
def update_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(user, data=request.data, partial=True)  # partial=True allows partial updates
    if serializer.is_valid():
        if 'password' in request.data:
            user.set_password(request.data['password'])
            user.save()
        else:
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#회원정보 삭제
@api_view(['DELETE'])
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)    
        
    

'''
두가지 방법이 있나봄.
이렇게 하려면 urls.py 에
path('signup/',views.signup.as_view(), name='signup') 이렇게 해야함.
class UserView(APIView):
    def signup(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "가입완료"})
        return Response({"message" : "가입 불가"})'''      