from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.


#UserManager 먼저 생성, BaseManager 를 상속받음
class UserManager(BaseUserManager):
    def create_user(self, email, password=None,name=None):
        if not email:
            raise ValueError('이메일을 입력하세요')
        email = self.normalize_email(email) #대소문자를 표준화
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    #superuser 만드는 함수
    def create_superuser(self, email, password=None, name=None):
        user = self.create_user(email, password=password, name=name)
        user.is_admin = True
        user.save(using=self._db)
        return user

#AbstractBaseUser 를 상속받음
class User(AbstractBaseUser):
 
    #unique=true 고유값이어야함
    email  = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    password = models.TextField() #Charfield 로 할 것
    name = models.CharField(max_length=100)



    # admin 에서 이메일 표시함
    def __str__(self):
        return self.email