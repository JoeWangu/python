from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone
# from comments.models import Comment
# from django.contrib.contenttypes.models import ContentType
from django.utils.safestring import mark_safe


# super calls/inherits the PostManager manager then we filter to override its function
class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())

def upload_location(instance,filename):
    return '%s/%s' %(instance.id,filename)

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to = upload_location, null=True,blank=True,height_field='height_field',width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateTimeField(auto_now = False, auto_now_add = False)
    updated = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(auto_now_add = True)



        # safe method displays html content wherever you want it
    def safeContent(self):
        content = self.content
        return mark_safe(content)

        # ordering files(another way provided in views)
    class Meta:
        ordering = ('-timestamp','-updated')

        #if the same post is done over and over it will slugify ie.add - to name to prevent repetition
        #eg post the post again it becomes post-1 then post-1-1 etc
        #the - also helps posts be url ready
    
    # @property
    # def comments(self):
    #     instance = self
    #     qs = Comment.objects.filter_by_instance(instance)
    #     return qs

    # @property
    # def get_content_type(self):
    #     instance = self
    #     content_type = ContentType.objects.get_for_model(instance.__class__)
    #     return content_type

    objects = PostManager()


def create_slug(instance,new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    
    qs = Post.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender,instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver,sender=Post)