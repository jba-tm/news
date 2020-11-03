from django.urls import path

from .views import PostDetailPrintView
from .api import api_router

urlpatterns = [
    path('<str:slug>/pdf', PostDetailPrintView.as_view(), name='post-detail-pdf'),
    path('api/v2/', api_router.urls),
]
