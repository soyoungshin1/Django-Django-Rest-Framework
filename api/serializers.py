from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
        
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )  
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    
class Meta:
    model = User
    fields = ['username', 'email', 'passwore']
              