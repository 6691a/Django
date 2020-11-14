from django.contrib import admin

# Register your models here.
from .models import Photo


# admin_page customizing


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created', 'updated']
    raw_id_fields = ['author']
    list_filter = ['created', 'updated', 'author']
    # author은 포린키라 정확한 값 이메일, 이름 등과 같은걸로 지정 해야함
    search_fields = ['test', 'created,[author__username']
    ordering = ['-updated', '-created']


admin.site.register(Photo, PhotoAdmin)
