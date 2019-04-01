from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm): # 회원가입을 위한 입력 폼
    class Meta:
        model = User
        fields = ['username', 'password']