"""Template tags for the ``image_gallery`` app."""
from django import template
from django.utils.text import slugify
from filer.models import Image
from image_gallery.models import Gallery

register = template.Library()


@register.inclusion_tag('image_gallery/pictures.html', takes_context=True)
def render_pictures(context, selection='recent', amount=3):
    """Template tag to render a list of pictures."""
    pictures = Image.objects.filter(
        folder__id__in=Gallery.objects.filter(is_published=True).values_list(
            'folder__pk', flat=True))
    if selection == 'recent':
        context.update({
            'pictures': pictures.order_by('-uploaded_at')[:amount]
        })
    elif selection == 'random':
        context.update({
            'pictures': pictures.order_by('?')[:amount]
        })
    else:
        return None
    return context


@register.simple_tag()
def get_slug(img):
    name = img.name or img.original_filename
    return slugify(name)
