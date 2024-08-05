from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    #write_only=True 입력시에만 사용되고, 응답데이터에는 보여지지 않게함
    
    class Meta:
        model = User
        fields = '__all__'  # 모든 필드를 포함하도록 명시
        
  
    def create(self,validated_data):
        user = User(
            email=validated_data['email'],
            name=validated_data['name']
        )    
        user.set_password(validated_data['password']) #비밀번호를 해시화
        user.save()
        return user