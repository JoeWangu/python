from django.db import models

# Create your models here.
class UserPermissions(models.Model):
    is_staff = models.BooleanField(default=False)
    is_manual_worker = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_gateway_mall_staff = models.BooleanField(default=False)
    is_two_rivers_mall_staff = models.BooleanField(default=False)