from django.urls import path
from testapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('insert', views.insertData, name='insert'),
    path('update/<id>', views.updateData, name='update'),
    path('delete/<id>', views.deleteData, name='delete'),
]
