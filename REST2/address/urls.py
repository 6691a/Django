from django.urls import path

from .views import address_list
# Create your tests here.


urlpatterns = [

    path('user/', address_list),
]
