from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm # 내장되어있는 form
from django.contrib import messages
from .forms import UserRegisterForm # UserCreationForm 상속
from django.contrib.auth.decorators import login_required # 로그인 되었을 때만 url에 접근이 가능하도록 함

def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST) # 내장되어있는 form을 사용하려면
        form = UserRegisterForm(request.POST) # users/forms.py 에 있는 form을 사용하려면 (UserCreationForm 상속)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!')
            return redirect('login') # 회원가입이 완료되면 login 페이지로 redirect
    else:
        # form = UserCreationForm() # 내장되어있는 form을 사용하려면
        form = UserRegisterForm() # users/forms.py 에 있는 form을 사용하려면 (UserCreationForm 상속)
    return render(request, 'users/register.html', {'form':form})


@login_required # 로그인이 되어있지 않으면 error -> settings.py 에서 LOGIN_URL을 추가함으로써 error 대신 login을 먼저 시킴
def profile(request):
    return render(request, 'users/profile.html')