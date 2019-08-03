"""Settings of the ``image_gallery``` application."""
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

GALLERY_DISPLAY_TYPE_CHOICES_DEFAULT = (
    ('default', _('Default')),
    ('teaser', _('Teaser')),
)

GALLERY_PAGINATION_AMOUNT = getattr(settings, 'GALLERY_PAGINATION_AMOUNT', 10)
IMAGE_PAGINATION_AMOUNT = getattr(settings, 'IMAGE_PAGINATION_AMOUNT', GALLERY_PAGINATION_AMOUNT)

DISPLAY_TYPE_CHOICES = getattr(
    settings,
    'GALLERY_DISPLAY_TYPE_CHOICES',
    GALLERY_DISPLAY_TYPE_CHOICES_DEFAULT
)
