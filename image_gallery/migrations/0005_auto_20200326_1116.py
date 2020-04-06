# Generated by Django 2.2.11 on 2020-03-26 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.folder


class Migration(migrations.Migration):

    dependencies = [
        ('image_gallery', '0004_gallery_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='image_gallery.GalleryCategory', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='folder',
            field=filer.fields.folder.FilerFolderField(on_delete=django.db.models.deletion.PROTECT, to='filer.Folder', verbose_name='Folder'),
        ),
        migrations.AlterField(
            model_name='galleryimageextension',
            name='image',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='galleryplugin',
            name='gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image_gallery.Gallery', verbose_name='Gallery'),
        ),
    ]
