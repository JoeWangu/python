from django.urls import path
from mpesa.views import home, index

urlpatterns = [
    path('', home, name='home'),
    path('index', index, name='index')
]
