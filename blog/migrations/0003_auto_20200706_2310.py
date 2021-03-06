# Generated by Django 3.0.8 on 2020-07-06 15:10

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpagegalleryimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpagegalleryimage',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='blog.BlogPage'),
        ),
    ]
