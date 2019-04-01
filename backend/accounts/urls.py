from django.urls import path, include
from . import views

urlpatterns = [
    path('join/', views.signup), # /accounts/join 으로 들어오면 views의 signup 메소드로
    path('login/', views.signin),
    path('logout/', views.signout)
]