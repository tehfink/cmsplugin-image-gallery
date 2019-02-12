"""Simple admin registration for ``image_gallery`` models."""
from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from filer.admin.imageadmin import ImageAdmin
from .models import Gallery, GalleryCategory, GalleryImageExtension


@admin.register(Gallery)
class GalleryAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    """Custom admin for the ``Gallery`` model."""
    list_display = ('title', 'slug', 'date', 'location', 'folder', 'category')
    list_filter = ['category', ]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    """Custom admin for the ``GalleryCategory`` model."""
    list_display = ('name', 'slug')


class GalleryImageInline(admin.TabularInline):
    model = GalleryImageExtension
ImageAdmin.inlines = ImageAdmin.inlines[:] + [GalleryImageInline]
