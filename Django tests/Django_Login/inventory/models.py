from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=100, null=False,blank=False)
    cost_per_item = models.DecimalField(max_digits=19,decimal_places=2,null=False,blank=False)
    quantity_in_stock = models.IntegerField(null=False,blank=False)
    quantity_sold = models.IntegerField(null=False,blank=False)
    sales = models.DecimalField(max_digits=19,decimal_places=2,null=False,blank=False)
    stock_date = models.DateField(auto_now_add=True)
    last_sales_date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name



    # user = models.ManyToManyField(User)
    # tables = models.CharField(max_length=255, blank=True,null=True)
    # chairs = models.CharField(max_length=255, blank=True,null=True)
    # sofas = models.CharField(max_length=255, blank=True,null=True)
    # stools = models.CharField(max_length=255, blank=True,null=True)
    # tables = models.CharField(max_length=255, blank=True,null=True)
    # beds = models.CharField(max_length=255, blank=True,null=True)
    # price = models.DecimalField(max_digits=10, decimal_places=5)
    # created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    # updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    # # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    # image = models.ImageField(upload_to="uploads/%Y/%m/%d/", max_length=255)