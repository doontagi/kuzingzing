from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm # 내장되어있는 form
from django.contrib import messages
from .forms import UserRegisterForm # UserCreationForm 상속

def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST) # 내장되어있는 form을 사용하려면
        form = UserRegisterForm(request.POST) # users/forms.py 에 있는 form을 사용하려면 (UserCreationForm 상속)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!')
            return redirect('/')
    else:
        # form = UserCreationForm() # 내장되어있는 form을 사용하려면
        form = UserRegisterForm() # users/forms.py 에 있는 form을 사용하려면 (UserCreationForm 상속)
    return render(request, 'users/register.html', {'form':form})