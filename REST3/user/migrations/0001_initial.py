# Generated by Django 3.1.3 on 2020-11-19 15:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Primary Key')),
                ('email', models.EmailField(max_length=64, unique=True, verbose_name='email')),
                ('created', models.DateField(auto_now_add=True, verbose_name='생성일')),
                ('is_active', models.BooleanField(default=True, verbose_name='계정 활성화')),
                ('is_admin', models.BooleanField(default=False, verbose_name='관리자 활성화')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'user',
            },
        ),
    ]