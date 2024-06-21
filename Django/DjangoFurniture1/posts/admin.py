from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display_links = ['title']
    list_display = ('title','content','updated','timestamp')
    # list_editable = ['content']
    list_filter = ['updated','timestamp']
    search_fields = ['title','content']


admin.site.register(Post,PostAdmin)