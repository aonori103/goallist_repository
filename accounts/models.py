from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.urls import reverse_lazy
from datetime import datetime
# from jp_birthday.models import BirthdayModel

class UserManager(BaseUserManager):
    def create_user(self, username, address, password=None):
        if not username:
            raise ValueError('ユーザー名を入力してください')
        
        if not address:
            raise ValueError('メールアドレスを入力してください')
        
        if not password:
            raise ValueError('パスワードを入力してください')
        
        user = self.model(
            username = username,
            address = address
        )
        user.set_password(password) #パスワードをハッシュ化
        user.save(using=self._db) #ユーザーを保存
        return user
    
    def create_superuser(self, username, address, password=None):
        user = self.model(
            username = username,
            address = address
        )
        user.set_password(password) #パスワードをハッシュ化
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db) #ユーザーを保存
        return user


class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30)
    address = models.EmailField(unique=True, blank=False)
    job = models.CharField(max_length=100, blank=True)
    introduction = models.CharField(max_length=500, blank=True)
    birthday = models.DateField(default='1900-01-01')
    picture = models.FileField(upload_to='picture/%Y/%m/%d/', null=True)
    created_at = models.DateTimeField()
    upload_at = models.DateTimeField()
    is_active = models.BooleanField(default=True) #ログインしているか
    is_staff = models.BooleanField(default=False) #管理権限
    
    USERNAME_FIELD = 'address' #ログイン時にメルアドが必要
    REQUIRED_FIELDS = ['username'] #superuser作成時に必要なフィールド
    
    objects = UserManager()
    
    
    # def get_absolute_url(self):
    #     return reverse_lazy('accounts:user_login')
    