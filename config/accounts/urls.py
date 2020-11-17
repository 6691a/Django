from django.urls import path, include

from django.contrib.auth import views

urlpatterns = [

    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(template_name='registration/logout.html'), name="logout"),
]
