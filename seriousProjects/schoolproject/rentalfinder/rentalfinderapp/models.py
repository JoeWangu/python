from PIL import Image
from user.models import UserModel
from django.db import models


def get_default_img():
    img = Images.objects.get(image="default.jpg")
    return img


class Images(models.Model):
    image = models.ImageField(upload_to='', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.image.name

    def save_image(self, *args, **kwargs):
        super(Images, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path, quality=100, optimize=True)
        return super().save()


LOCATION = [('N', 'Ngomongo'), ('D', 'Diaspora'), ('M', 'Mjini')]


class Rental(models.Model):
    # user = models.ManyToManyField(UserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ForeignKey(Images, on_delete=models.SET_DEFAULT, max_length=255, default=get_default_img, null=True,
                              blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    type = models.CharField(max_length=100)
    location = models.CharField(max_length=100, choices=LOCATION)
    available = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=1, decimal_places=0)
    total_units = models.IntegerField()
    date_posted = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
