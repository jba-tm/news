from django.utils.translation import ugettext_lazy as _
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from wagtail.core.models import Page


class HomePage(Page):
    max_count_per_parent = 0

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = self.get_children().live().order_by('-first_published_at')
        # Paginate all posts by 2 per page
        paginator = Paginator(all_posts, 25)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            content_pages = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            content_pages = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            content_pages = paginator.page(paginator.num_pages)

        # "posts" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle
        context['posts'] = content_pages
        return context

    class Meta:
        verbose_name = _('Home')
