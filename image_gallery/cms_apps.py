"""CMS apphook for the ``image_gallery`` app."""
from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from .cms_menus import ImageGalleryMenu


@apphook_pool.register
class ImageGalleryApphook(CMSApp):
    name = _("Image Gallery Apphook")
    app_name = "image_gallery"
    urls = ["image_gallery.urls", ]

    def get_urls(self, page=None, language=None, **kwargs):
        return self.urls

    def get_menus(self, page=None, language=None, **kwargs):
        return [ImageGalleryMenu]
