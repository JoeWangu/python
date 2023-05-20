from django.contrib import admin
from .models import Author,Category,Post

class AuthorModel(admin.ModelAdmin):
    list_display = ['user']

class CategoryModel(admin.ModelAdmin):
    list_display = ['title','slug']
    prepopulated_fields = {"slug": ("title",)}

class PostModel(admin.ModelAdmin):
    list_display = ['title','slug']
    prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(Author, AuthorModel)
admin.site.register(Category, CategoryModel)
admin.site.register(Post, PostModel)