# Generated by Django 5.1 on 2024-08-27 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricing',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]