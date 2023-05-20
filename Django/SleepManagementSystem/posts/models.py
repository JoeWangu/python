from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
User = get_user_model()
def upload_to(instance, filename):
    return 'profile-pic/{0}{1}'.format(instance.id, filename)

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to=upload_to, default='/profile.png')

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    thumbnail = models.ImageField()
    slug = models.SlugField(max_length=150, unique=True,blank=True)

    def __str__(self):
        return self.title
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     if not self.slug:
    #         self.slug = slugify(self.title)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("postlist", kwargs={"slug": self.slug})

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True,blank=True)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    # def get_absolute_url(self):
    #     return reverse("post_detail", args=[str(self.id)])
    def get_absolute_url(self):
        return reverse("allposts", kwargs={"slug": self.slug})