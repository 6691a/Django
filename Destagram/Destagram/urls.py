"""Destagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # 나머지를 전부다 넘겨줌 ex) 127.0.0.1:8000/abc 이 경로도 ''로 넘겨줌
    path('', include('photo.urls')),
    path('accounts/', include('accounts.urls')),
]

# 디버깅 확인용
# 1.미디어 파일 서버를 별도로 두고 사용한다.
# 2.Web 서버에서 별도로 서빙을 설정한다.

# MEDIA_URL 형태로 들어오면 document_root에서 파일을 찾아라
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
