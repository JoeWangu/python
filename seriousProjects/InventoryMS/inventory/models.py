from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import os

# IMAGE_CHOICES = [(filename, filename) for filename in os.listdir(os.path.join(settings.BASE_DIR, 'media'))]
DC = 'DC'
NY = 'NewYork'
TX = 'Texas'

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank= True, default='not provided')

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    # brand = models.CharField(max_length=255)
    # model = models.CharField(max_length=255)
    model_number = models.CharField(max_length=255)
    specifications = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True)
    IMAGE_CHOICES = [(filename, filename) for filename in os.listdir(settings.MEDIA_ROOT)]
    image = models.CharField(max_length=100, choices=IMAGE_CHOICES)
    


    def __str__(self):
        return self.name
    
class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    last_sales_date = models.DateField(auto_now=True)
    quantity_sold = models.IntegerField(null=False,blank=False)
    sales = models.DecimalField(max_digits=19,decimal_places=2,null=False,blank=False)
    stock_date = models.DateField(auto_now_add=True)
    quantity_in_stock = models.IntegerField()
    minimum_quantity = models.IntegerField()

class Customer(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=255)
    address = models.CharField(max_length=200)
    extra_info = models.TextField(null=True, blank=True, default='none')

    def __str__(self):
        return self.name

class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    status = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order #{self.id}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    # price = models.DecimalField(max_digits=8, decimal_places=2)

# track the movement of inventory, such as when items are received from suppliers, sold to customers, or transferred between locations. 
class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('IN', 'Incoming'),
        ('OUT', 'Outgoing'),
        ('TRANSFER', 'Transfer'),
    ]

    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPES)
    transaction_date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Location(models.Model):
    LOCATION_CHOICES = [
    (DC, 'Washington, D.C.'),
    (NY, 'New York City'),
    (TX, 'Austin'),
    ]
    name = models.CharField(max_length=255)
    address = models.CharField(choices=LOCATION_CHOICES, default=DC)
    capacity = models.IntegerField(null=True, blank=True, default='none provided')
    contact_information = models.CharField(max_length=255, null=True, blank=True, default='none provided')

    def __str__(self):
        return self.name

class OnlineBuyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Shipments(models.Model):
    shipment_date = models.DateTimeField()
    tracking_number = models.IntegerField()
    recipient_information = models.CharField(max_length=255)

class Employees(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True, default='none provided')
    contact_info = models.CharField(max_length=255, null=True, blank=True, default='none provided')