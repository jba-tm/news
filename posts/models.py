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
    datetime_on_site = models.DateTimeField(null=True, verbose_name=_('Content datetime'),
                                            help_text=_('Published datetime on the site'))

    # site = ParentalKey('Site', null=True, on_delete=models.SET_NULL,
    #                    verbose_name=_('Site'), help_text=_('Published on the site'))

    site = models.CharField(null=True, blank=True, max_length=255,
                            verbose_name=_('Site'), help_text=_('Published on the site'))

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.SearchField('site'),
        index.FilterField('datetime_on_site'),
    ]

    content_panels = Page.content_panels + [
        # FieldPanel('title', widget=AdminAutoHeightTextInput(attrs={'autocomplete': 'off', })),
        MultiFieldPanel([
            FieldPanel('site', help_text=_('Site name')),
            FieldPanel('datetime_on_site', widget=AdminDateTimeInput(attrs={'autocomplete': 'off', },)),
        ], heading=_('Post information'), help_text=_('Post information')),

        FieldPanel('body', classname="full"),
    ]

    class Meta:
        verbose_name_plural = _("Post pages")
        verbose_name = _("Post page")
        permissions = (
            ('save_post_as_pdf', _('Can export post as pdf')),
        )
