from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.timezone import now
from django.views.generic import DetailView

from .models import PostDetailPage

# Create your views here.
from django_weasyprint import WeasyTemplateResponseMixin
from news.settings import base


class PostDetailView(SuccessMessageMixin, DetailView):
    model = PostDetailPage

    # def get_context_data(self, **kwargs):


class PostDetailPrintView(LoginRequiredMixin, PermissionRequiredMixin, WeasyTemplateResponseMixin, PostDetailView):
    permission_required = ('post.save_post_as_pdf', )
    pdf_filename = 'example.pdf'
    template_name = 'posts/post_detail_print.html'
    # output of MyModelView rendered as PDF with hardcoded CSS
    pdf_stylesheets = [
        base.BASE_DIR + '/news/static/css/weasyprint.css',
    ]
    # show pdf in-line (default: True, show download dialog)
    # pdf_attachment = False

    def get_pdf_filename(self):
        today = now().today().strftime("%d.%m.%Y")
        self.pdf_filename = f'{today}.pdf'
        return super().get_pdf_filename()
