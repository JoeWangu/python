from django.contrib import admin
from .models import Category, Supplier, Product, Inventory, Customer, Order, OrderItem, Transaction, Location, OnlineBuyer, Shipments, Employees

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Transaction)
admin.site.register(Location)
admin.site.register(OnlineBuyer)
admin.site.register(Shipments)
admin.site.register(Employees)