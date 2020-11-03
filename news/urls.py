from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from django.contrib.auth.views import LoginView
from wagtail.admin.views.account import LogoutView
from search import views as search_views
from news.apps.core.forms import AppLoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.SearchView.as_view(), name='search'),

    path('login/', LoginView.as_view(template_name=settings.WAGTAIL_FRONTEND_LOGIN_TEMPLATE,
                                     form_class=AppLoginForm, redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('post/', include('posts.urls')),

]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r"", include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r"^pages/", include(wagtail_urls)),
]
