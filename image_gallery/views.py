"""Views for the ``image_gallery`` app."""
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, TemplateView
from django.views import View
from django.utils.text import slugify
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from filer.models import File, Image
from .app_settings import GALLERY_PAGINATION_AMOUNT, IMAGE_PAGINATION_AMOUNT
from .models import Gallery, GalleryCategory


class ImageDetailView(DetailView):
    model = Image
    template_name = 'image_gallery/image_detail.html'
    slug_field = 'name'

    def get_queryset(self):
        """ Filter the Image queryset for only images in the Gallery noted by `gallery_slug` """
        queryset = super().get_queryset()
        if self.kwargs['gallery_slug']:
            return queryset.filter(folder__gallery__title__iexact=self.kwargs['gallery_slug'])
        return queryset

    def get_object(self, queryset=None):
        """ Iterates over queryset of Images in a Gallery, matching passed in slug to an Image's slugified `name` or `original_filemane`
            NB: this is inefficient
        """
        if queryset is None:
            queryset = self.get_queryset()
        slug = self.kwargs.get(self.slug_url_kwarg, None)
        if slug is not None:
            # import ipdb;ipdb.set_trace()
            for q in queryset.iterator():
                if slug in [slugify(q.name), slugify(q.original_filename)]:
                    return q
        raise Http404(f"No {self.model._meta.verbose_name} found matching the query")


class GalleryDetailView(DetailView):
    """View to display a list of ``Images`` instances in a ``Gallery``."""
    template_name = 'image_gallery/gallery_detail.html'
    model = Gallery

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image_list = self.get_object().get_folder_image_list()
        paginator = Paginator(image_list, IMAGE_PAGINATION_AMOUNT)
        page = self.request.GET.get('page')
        try:
            images = paginator.page(page)
        except PageNotAnInteger:
            images = paginator.page(1)
        except EmptyPage:
            images = paginator.page(paginator.num_pages)

        context['images'] = images
        return context


class GalleryListView(ListView):
    """View to display a list of ``Gallery`` instances."""
    paginate_by = GALLERY_PAGINATION_AMOUNT
    template_name = 'image_gallery/gallery_list.html'
    model = Gallery

    def get_pagination_options(self):
        options = {
            'pages_start': 10,
            'pages_visible': 4,
        }
        pages_visible_negative = -options['pages_visible']
        options['pages_visible_negative'] = pages_visible_negative
        options['pages_visible_total'] = options['pages_visible'] + 1
        options['pages_visible_total_negative'] = pages_visible_negative - 1
        return options

    # returns list of Files in Galleries, instead of Gallery objects??
    # def get_queryset(self):
    #     return File.objects.filter(
    #         folder__gallery__isnull=False).prefetch_related(
    #         'folder__gallery_set').order_by('-modified_at')

    def get_context_data(self, **kwargs):
        ctx = super(GalleryListView, self).get_context_data(**kwargs)
        ctx.update({'categories': GalleryCategory.objects.all()})
        ctx.update({'pagination': self.get_pagination_options()})
        # import ipdb; ipdb.set_trace()
        return ctx


# def GalleryWrapper(request):#*args, **kwargs):
#     """ Loads GalleryListView or GalleryDetailView, depending on Page's apphook settings
#         if 'application_namespace' is namespaced, load the detail page for specified Gallery
#         otherwise load the standard list page
#         to-do: account for urls of photos in galleries
#     """
#     application_namespace = getattr(request.current_page, 'application_namespace', None)
#     if application_namespace and ':' in application_namespace:
#         return GalleryDetailView.as_view()(
#             request,
#             pk=Gallery.objects.get(slug__iexact=application_namespace.split(':')[1]).pk
#         )
#     return GalleryListView.as_view()(request)
