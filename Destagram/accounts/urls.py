from django.urls import path
from django.contrib.auth import views as auth_view
from .views import *

urlpatterns = [
    # name ='login' = html에서 해당 페이지로 이동 시키기 위함
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', register, name='register'),
]
