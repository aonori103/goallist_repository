from django import forms
from datetime import datetime
from .models import Users
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm

class RegistForm(forms.ModelForm):
    username = forms.CharField(label='ユーザー名', help_text='30字以内で入力してください', max_length=30)
    address = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', help_text='30字以内で入力してください', max_length=30, widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード', help_text='30字以内で入力してください', max_length=30, widget=forms.PasswordInput())
    
    class Meta:
        model = Users
        fields = ['username', 'address', 'password']
        
    def clean(self): #再入力したパスワードが合っているか
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('パスワードが異なります')
    
    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='メールアドレス') #ログイン時にメルアド必須のため
    password = forms.CharField(label='パスワード', help_text='30字以内で入力してください', max_length=30, widget=forms.PasswordInput())
    remember = forms.BooleanField(label='ログイン状態を保持する', required=False)


# ユーザー編集用画面とフォーム作る。jobとかintroductionとかを追加する
class UserEditForm(forms.ModelForm):
    username = forms.CharField(label='名前', initial=Users.username, max_length=30)
    address = forms.EmailField(label='メールアドレス', initial=Users.address)
    job = forms.CharField(label='職業', initial=Users.job, max_length=100, required=False)
    introduction = forms.CharField(label='自己紹介', initial=Users.introduction, max_length=500, required=False)
    birthday = forms.DateField(label='誕生日', initial=Users.birthday)
    # picture = forms.FileField(upload_to='picture/', required=False)
    # password = forms.CharField(label='パスワード', help_text='30字以内で入力してください', max_length=30, widget=forms.PasswordInput(), required=False)
    # confirm_password = forms.CharField(label='パスワード', help_text='30字以内で入力してください', max_length=30, widget=forms.PasswordInput(), required=False)
    
    class Meta:
        model = Users
        fields = ['username', 'address', 'job', 'introduction', 'birthday']
        
    
    def save(self, *args, **kwargs):
        obj = super(UserEditForm, self).save(commit=False)
        obj.upload_at = datetime.now()
        obj.save()
        return obj
