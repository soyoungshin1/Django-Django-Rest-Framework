from .serializers import BookSerializer
from rest_framework.decorators import *
from rest_framework import response,generics
from rest_framework.response import Response
from rest_framework import viewsets, filters
from rest_framework.viewsets import ViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination




@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


class BookViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        pagination_class = PageNumberPagination
        filter_backends = [SearchFilter,OrderingFilter]
        search_fields = ['title', 'author']
        ordering_fields = ['publication_date', 'price']
        return Response(serializer.data)
    
    
    def retrieve(self, request, pk=None):
        book = Book.objects.get(pk=pk)
        serializer =BookSerializer(book)
        pagination_class = PageNumberPagination
        return Response(serializer.data)
    
    
    
    def mark_as_read(self,request,pk=None):
            book = Book.objects.get(pk=pk)
            pagination_class = PageNumberPagination
            book.mark_as_read()
            return Response({'status' : 'book marked as read'})
        
        
class MyViewSet(ViewSet):

    # 기본 CRUD 작업

    def list(self, request):
        # 리소스 목록을 반환하는 구현
        pass

    def create(self, request):
        # 새로운 리소스를 생성하는 구현
        pass

    def retrieve(self, request, pk=None):
        # 특정 ID의 리소스를 반환하는 구현
        pass

    def update(self, request, pk=None):
        # 특정 ID의 리소스를 업데이트하는 구현
        pass

    def destroy(self, request, pk=None):
        # 특정 ID의 리소스를 삭제하는 구현
        pass

    # @action 데코레이터를 사용한 사용자 정의 작업

    @action(detail=False, methods=['GET'])
    def my_custom_action(self, request):
        # 사용자 정의 작업의 구현
        # 이 작업은 특정 리소스에 대해 동작하지 않음 (detail=False)
        # GET 요청에 응답함 (methods=['GET'])
        pass        

class UserSerializer(generics.CreateAPIView):
    serializer_class = UserSerializer
    
class UserLoginView(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs)   :
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        
        refresh = RefreshToken.for_user(user)
        Response = {
            'refresh' : str(refresh),
            'access' : str(refresh.access_token),
        }     
        return Response(response)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    #보호된 뷰를 여기에 쓰기
    return Response({'massage' : 'This is a protected view.'})    