# Generated by Django 5.1 on 2024-08-28 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_product_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='file_link',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
