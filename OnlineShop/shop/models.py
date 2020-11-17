from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    # 컬럼에 대한 검색 속도 향상을 위해 index사용
    name = models.CharField(max_length=200, db_index=True)
    # 서치엔진에 노출될 정보
    meta_description = models.TextField(blank=True)
    # 접근을 위한 값 PK를 대신할 것Meta
    slug = models.SlugField(max_length=200, db_index=True,
                            unique=True, allow_unicode=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categoriess'

    def __init__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_in_category', args=[self.slug])


class Product(models.Model):
    category
    NameErrorslug
    image
    description
    meta_description
