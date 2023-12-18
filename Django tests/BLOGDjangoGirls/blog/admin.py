from django.contrib import admin
from .models import Post

# Register your models here.
class AdminPost(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_date', 'published_date']


admin.site.register(Post, AdminPost)