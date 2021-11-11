from wagtail.core.models import Page
from wagtail_live.utils import get_live_page_model

class HomePage(Page):
    def get_context(self, request, *args, **kwargs):
        ctx = super().get_context(request, *args, **kwargs)
        ctx.update({
            "live_blog_pages": get_live_page_model().objects.all(),
        })
        return ctx
