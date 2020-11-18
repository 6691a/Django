from django.db import models

# Create your models here.


class Address(models.Model):
    name = models.CharField(max_length=50, verbose_name='사용자 이름')
    # verbose_name= admin에서 보이는 컬럼명
    email = models.EmailField(max_length=255)
    address = models.TextField(blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created', 'name']
        db_table = "my_user"
