from django.urls import path
from .views import PostDetailPrintView


urlpatterns = [
    path('<str:slug>/pdf', PostDetailPrintView.as_view(), name='post-detail-pdf'),
]
