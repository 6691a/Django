from django.db import models

# Create your models here.

# 1. 모델 : DB에 저장될 데이터가 있다면 데이터 묘사
# 2. 뷰(기능) : 계산, 처리, 기능, 화면 등을 구현
# 3. URL 맵핑 : 라우팅 테이블에 기록 urls.py에 주소 지정
# 4. 화면 출력이 필요하다면 : 템플릿을 작성한다.


# 장고의 기본 유저 모델 커스텀 필요 시baseUsermodel, baseUser 등
from django.contrib.auth.models import User
from django.urls import reverse

# 장고의 orm 기능이 있음 DB에 넣고 뺴고를 구현안해도 사용이 가능해짐
# ForeignKey 외래키 - 다른 테이블에서의  PrimaryKey
# PrimaryKey 주된 키 - 테이블 생성 시 설정한 고유한  값


class Photo(models.Model):
    # User의 PrimaryKey 사용하겠다

    # CASCADE = 연결된 개체 삭제 시 하위 개체도 삭제
    # PROTECT = 하위 개체가 존재 시 삭제 불가
    # SET_NULL = 연결된 개체만 삭제 필드값 NULL 설정
    # SETDEFAULT = 연결된 개체 삭제 필드 값 기본 값으로 설정
    # SET() = 연결된 객체 삭제 후 지정한 값으로 변경
    # DO_NOTHING = 아무것도 안함

    # related_name='user_photos' user가 작성한 목록을 가져옴 Photo_set이 기본 이름임
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_photos')

    # django에 추가된 이미지필드 file, image는 어디에 업로드 할지 정해아함
    # photos아래 해당 년, 월, 일 밑에 저장한다.
    # upload_to에 함수도 들어갈 수 있음
    # default 값이 없다면 필수 필드가 됨
    photo = models.ImageField(
        upload_to='photos/%y/%m/%d')  # ,default='photos/no_image.png')

    # text만 예외로 default없이도 필수 필드가 아님
    text = models.TextField()

    # auto_now_add = 등록 시 현재 시간을 설정 / auto_now = 등록, 수정 등의 작업 시 고쳐 적음
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # inner class
    class Meta:
        # updated 기준으로 내림차순 정렬
        ordering = ['-updated']

    # str = print or 관리자 페이지에서 확인 시
    def __str__(self):
        # authot가 ForeignKey여서 user의 정보도 가져옴
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        # update, create 이후 이동할 페이지 지정하는 곳
        return reverse('photo:photo_detail', args=self.id)
