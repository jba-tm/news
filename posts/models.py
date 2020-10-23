# import pytz
from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.search import index
from django.utils.translation import ugettext_lazy as _
from wagtail.admin.widgets import AdminDateTimeInput
from wagtail.contrib.forms.models import AbstractForm
from news.apps.core.models import SoftDeletionModel
# Create your models here.


class PostDetailPage(Page, SoftDeletionModel):
    parent_page_types = ['home.HomePage']
    subpage_types = []

    body = RichTextField(verbose_name=_('Body'), help_text=_('Content body'),)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    class Meta:
        verbose_name_plural = _("Post pages")
        verbose_name = _("Post page")
        permissions = (
            ('save_post_as_pdf', _('Can export post as pdf')),
        )
