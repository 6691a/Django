from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid
# Create your models here.


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("이메일을 입력해주세요.")

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)

        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password,  **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        return self._create_user(email, password, **kwargs)


class User(AbstractBaseUser):

    # 범용 고유 식별자
    uuid = models.UUIDField(primary_key=True, unique=True,
                            editable=False, default=uuid.uuid4, verbose_name='Primary Key')
    email = models.EmailField(verbose_name='email',
                              max_length=64, unique=True)
    # username = models.CharField(max_length=30)
    created = models.DateField(auto_now_add=True, verbose_name='생성일')
    # updated = models.DateTimeField(auto_now=True, verbose_name='수정일')
    is_active = models.BooleanField(default=False, verbose_name='계정 활성화')
    # email을 아이디로 사용하기 위한 명시
    USERNAME_FIELD = 'email'
    # createsuperuser 커맨드로 유저를 생성할 때 나타날 필드 이름 목록
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
