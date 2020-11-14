from django.db import models


# 모델 안에선 reverse  클래스 뷰 안에서 필드값은 reverse_lazy
# views에 reverse_laze
from django.urls import reverse

# Create your models here.

# SQL 사용 없이 데이터베이스를 다루기 위해 만듬
# 데이터를 개체화 하여 다루기 위해 만듬

# 모델 = 테이블 (액셀의 시트)
# 모델의 필드(변수) = 테이블의 컬럼 (열)
# 인스턴스 = 테이블의 레코드 (행)
# 필드값(인스턴스 값) = 레코드의 컬럼 값 (셀 안의 값)


class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    # admin에서 데이터를 보여줄 이름 설정
    def __str__(self):
        return self.site_name  # + " url: " + self.url
    # 필드의 종류가 결정하는 것
    # 1. DB의 컬럼 종류
    # 2. 제약 사항
    # 3. From의 종류
    # 4. From의 제약 사항

    # 장고에서만 제공해줌
    def get_absolute_url(self):
        # revers에 pk 값이 필요함

        # return reverse('list')
        return reverse('detail', args=[self.id])
        # return reverse('detail', args=[str(self.id)])


# 모델을 생성 했다 = DB에 어떤 값을 넣을지 설정만 함
# makemigrations = 모델의 변경사항을 추적해 기록함
# migrate = DB에 실제 반영시킨다.
