# Generated by Django 4.0.6 on 2022-07-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_delete_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.AddField(
            model_name='product',
            name='photos',
            field=models.ImageField(default=7112022, upload_to='pics'),
            preserve_default=False,
        ),
    ]
