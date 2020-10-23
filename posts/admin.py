from django.contrib import admin
from .models import PostDetailPage

# Register your models here.


class PostDetailPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', )
    list_display_links = ['title']
    search_fields = ('title', 'body', )


admin.site.register(PostDetailPage, PostDetailPageAdmin)
