from django.urls import path
from .views import inventory, per_product_view, add_product, delete_product, update_product, dashboard

urlpatterns = [
    path('', inventory, name='inventory'),
    path('product/<int:pk>', per_product_view, name='per_product'),
    path('add_product/', add_product, name='add_product'),
    path('delete/<int:pk>', delete_product, name='delete_product'),
    path('update/<int:pk>', update_product, name='update_product'),
    path('dashboard/', dashboard, name='dashboard'),
]