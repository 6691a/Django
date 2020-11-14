from django.urls import path
from .views import *
# from .views import BookmarkListView, BookmarkCreateView
urlpatterns = [
    # http://127.0.0.1/bookmark
    # .as_view() 클래스형을 함수형으로 바꿈
    # 클래스 형일 경우 꼭 사용할 것
    # 내부적으론 함수형으로 처리함
    # 함수형일 경우 이름만 적으면 댐


    # 관례적으로 templates/앱 이름/C,R,U,D 파일 생성
    # 모든 앱마다 CRUD가 존재할수  있음
    # 그래서 앱안에 templates를 생성 함


    # READ
    path("", BookmarkListView.as_view(), name='list'),
    # name='list' 화면 템플릿 이름, url패턴의 이름

    # CREATE
    path("add/", BookmarkCreateView.as_view(), name='add'),

    # <int:pk> pk = primary_key // int형 pk 값을 넣어라
    # <pk> 비울 경우 String형

    # READ from key
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),

    # UPDATE
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name='update'),

    # delete
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name='delete'),


]
