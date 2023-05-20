from django.contrib import admin
from .models import HandleMedia

# Register your models here.
class MediaAdmin(admin.ModelAdmin):
    list_display = ['author','title','created_on']
    list_filter = ['title']
    search_fields = ['title','author']
    

admin.site.register(HandleMedia, MediaAdmin)