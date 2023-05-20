# Generated by Django 4.2.1 on 2023-05-19 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HandleMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, height_field='image_height', null=True, upload_to='media', width_field='image_field')),
                ('caption', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('content', models.TextField(max_length=500)),
                ('image_height', models.IntegerField(default=0)),
                ('image_width', models.IntegerField(default=0)),
                ('title', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('publish_date', models.DateTimeField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('draft', models.BooleanField()),
                ('is_active', models.BooleanField(default=True)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
