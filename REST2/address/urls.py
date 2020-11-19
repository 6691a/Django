from django.urls import path

from .views import *
# Create your tests here.


urlpatterns = [

    path('user/', address_list),
    path('user/<int:pk>/', address_pk),
    path('user/login/', address_login),
]
