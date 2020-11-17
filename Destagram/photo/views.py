from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect
# Create your views here.


# 클래스형 뷰가 아닌 함수형 뷰로 만듬

from .models import Photo


def photo_list(request):
    # 보여줄 사진(데이터)
    # orm 관련 메니져 이름이 objects임
    # Photo모델에 objects의 전부 다 가져와라 << 이의미 아님
    photos = Photo.objects.all()
    # app/templates/photo/list.html 의미임   / 템플릿 변수 할당
    # 템플릿 안에선 'photos'라는 이름의로 우리가 만든 photos 변수를 사용 하겠다. (기본 이름은 'ojbect_list'임)
    return render(request, 'photo/list.html', {'photos': photos})


class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    # 데이터가 올바른지 판단하는 함수
    # 로그인을 했다고 전재 함
    def form_valid(self, form):
        # 작성자 매칭
        form.instance.author_id = self.request.user.id

        # 데이터가 올바르다면
        if form.is_valid():
            form.instance.save()
            # 메인 사이트를 의미
            return redirect('/')
        else:
            # 응답을 다시 돌려준다.
            return self.render_to_response({'form': form})


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = "/"
    template_name = "photo/delete.html"


class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'
