"""URLs for the ``image_gallery`` app."""
from django.conf.urls import url
from django.views.generic import DetailView

from .models import Gallery
from .views import GalleryListView, ImageDetailView, GalleryDetailView


app_name = 'image_gallery'
urlpatterns = [

    url(
        r'^(?P<gallery_slug>[\w-]+)/(?P<slug>[0-9A-Za-z-_.//]+)/$',
        ImageDetailView.as_view(),
        name='image_detail'
    ),

    url(
        r'^(?P<slug>[\w-]+)/$',
        GalleryDetailView.as_view(),
        name='image_gallery_detail'
    ),

    url(
        r'^$',
        GalleryListView.as_view(),
        name='image_gallery_list'
    ),

]
