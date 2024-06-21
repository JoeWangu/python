# from django.contrib import admin
# from .models import Comment


# admin.site.register(Comment)

from django.contrib import admin
from .models import Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on','name')
    search_fields = ('name', 'email', 'body')
