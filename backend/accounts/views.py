from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here.

##########################################
################  회원가입  ################
##########################################
def signup(request): # 회원가입
    if request.method == "POST": # POST로 reqest 할 경우 (제출한 경우)
        signup_form = UserForm(request.POST)
        if signup_form.is_valid():
            new_user = User.objects.create_user(**signup_form.cleaned_data)
            login(request, new_user)
            return redirect('login') # 회원가입 후 로그인 페이지로 리다이렉션
    else: # url을 통해 들어왔을 경우 (GET 방식)
        form = UserForm()
        return render(request, 'registration/signup.html', {'form': form}) # 회원가입 템플릿 렌더링



##########################################
################# 로그인 ###################
##########################################
def signin(request):
    if request.method == 'POST': # POST로 request 할 경우 (제출한 경우)
        login_form = UserForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            # db에 존재할 경우 user변수에는 User인스턴스가 할당,
            # 없으면 None
            user = authenticate(
                username = username,
                password = password
            )
            if user:
                login(request, user)
                return redirect('/')
            else:
                login_form.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다.')
    else: # url을 통해 들어왔을 경우 (GET 방식)
        login_form = UserForm()
    context = {
        'login_form': login_form,
    }
    return render(request, 'registration/login.html', context)



##########################################
################  로그아웃  ################
##########################################
def signout(request):
    logout(request)
    return redirect('/')