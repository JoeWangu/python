from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.
class HandleMedia(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media',height_field='image_height',width_field='image_field',blank=True,null=True)
    caption = models.CharField(max_length=150,default='',blank=True,null=True)
    content = models.TextField(max_length=500) 
    image_height = models.IntegerField(default=0)
    image_width = models.IntegerField(default=0)
    title = models.CharField(max_length=150,default='',blank=True,null=True)
    slug = models.SlugField(max_length=150, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField()
    updated_on = models.DateTimeField(auto_now=True)
    draft = models.BooleanField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.author
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.title)