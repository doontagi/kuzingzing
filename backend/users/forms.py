from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# 사용자 회원가입 form의 내용을 추가하기 위함
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']