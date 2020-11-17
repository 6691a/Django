from django.urls import path
from .views import *
from django.views.generic.detail import DetailView
from .models import Photo
# 2차 URL 파일
app_name = 'photo'

urlpatterns = [
    path('', photo_list, name='photo_list'),

    # views.py에 안만들고 아래와 같이 만들 수도 있음
    path('detail/<int:pk>', DetailView.as_view(model=Photo,
                                               template_name='photo/detail.html'), name='photo_detail'),

    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    # int형인 값인지 검사하고 pk 라는 이름으로 뷰로 전달
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),

]
