from haystack import indexes
from .models import Gallery


class GalleryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True)

    index_title = True

    def get_model(self):
        return Gallery

    def get_title(self, obj):
        return obj.title

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(is_published=True)

    def get_search_data(self, obj):
        return obj.image_catalog

    def prepare_text(self, obj):
        return obj.title + "\n" + obj.image_catalog
