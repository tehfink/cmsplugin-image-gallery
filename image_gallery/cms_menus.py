from django.urls import reverse
from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu
from .templatetags.image_gallery_tags import get_slug
from .models import Gallery


class ImageGalleryMenu(CMSAttachMenu):

    name = _("Image Gallery menu")

    # import ipdb; ipdb.set_trace()

    def get_nodes(self, request):
        """ creates parent-child list for extending django-cms navigation (menu & breadcrumb) """

        nodes = []
        galleries = list(Gallery.objects.filter(is_published=True))

        menu_id = 1
        for gallery in galleries:
            gallery_menu_id = menu_id
            nodes.append(
                NavigationNode(
                    gallery.title,
                    gallery.get_absolute_url(),
                    gallery_menu_id,
                )
            )
            menu_id += 1

            for img in gallery.get_folder_image_list():
                nodes.append(
                    NavigationNode(
                        img.name or img.original_filename,
                        get_slug(img, gallery),
                        menu_id,
                        parent_id=gallery_menu_id
                    )
                )
                menu_id += 1

        # print("*"*20)
        # for n in nodes:
        #     print(f"Node: {n}, url: {n.url}, id: {n.id}, parent: {n.parent_id}")

        return nodes

menu_pool.register_menu(ImageGalleryMenu)