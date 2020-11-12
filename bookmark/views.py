from django.shortcuts import render

# ctrl + 클릭 코드보기
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

from .models import Bookmark
# Create your views here.

# CRUD : Create, Read, Update, Delete
# List(Read)
# 클래스형 뷰, 함수형 뷰
# 클래스형 지정된 형식을 사용시 사용
# 함수형 마음대로 만들고 싶을때


# 웹 페이지 접속
# URL 입력 -> 웹 서버가 뷰를 찾아 동작 -> 응답
# ListView가 기본으로 이쪽으로 보냄 @_list.html
class BookmarkListView(ListView):
    # 기본 문법
    model = Bookmark
    fields = [
        'site_name'
        'url',
    ]


# Create, Update는 @_form으로 보냄
class BookmarkCreateView(CreateView):

    model = Bookmark
    fields = ['site_name', 'url']
    # 기존 설정된 _from을 _create로 변경

    template_name_suffix = "_create"
    success_url = reverse_lazy('list')
    #success_url = '/bookmark/'


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    template_name = 'bookmark/bookmark_delete.html'
    success_url = reverse_lazy('list')
