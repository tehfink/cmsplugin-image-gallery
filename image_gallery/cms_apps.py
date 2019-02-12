"""CMS apphook for the ``image_gallery`` app."""
from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class ImageGalleryApphook(CMSApp):
    name = _("Image Gallery Apphook")
    app_name = "image_gallery"


    def get_urls(self, page=None, language=None, **kwargs):
        return ["image_gallery.urls"]
