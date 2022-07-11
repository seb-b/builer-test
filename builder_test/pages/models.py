from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.search import index

from builder_test.pages import blocks as pages_blocks


class HomePage(Page):
    class Meta:
        verbose_name = "Homepage"


class ContentPage(Page):
    subtitle = models.TextField(verbose_name="Subtitle", blank=True, default="")
    body = StreamField(
        block_types=[
            ("card", pages_blocks.CardBlock()),
            ("image", pages_blocks.ImageBlock()),
            ("paragraph", pages_blocks.ParagraphBlock()),
        ],
        default="",
        verbose_name="Body",
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("body"),
    ]

    parent_page_types = [
        "pages.ContentPage",
        "pages.HomePage",
    ]

    class Meta:
        verbose_name = "Content Page"
