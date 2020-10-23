from django.contrib import admin
from .models import PostDetailPage

# Register your models here.


class PostDetailPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'datetime_on_site', )
    list_display_links = ['title']
    search_fields = ('title', 'body', 'datetime_on_site', )


admin.site.register(PostDetailPage, PostDetailPageAdmin)
