from django.contrib import admin
from news.apps.core.models import OnlineUserActivity

# Register your models here.

################
# Online users #
################


class OnlineUserActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_activity', 'ip_address')
    search_fields = ['user__username', 'ip_address']
    list_filter = ['last_activity']

    def get_ordering(self, request):
        return ['last_activity']


admin.site.register(OnlineUserActivity, OnlineUserActivityAdmin)

