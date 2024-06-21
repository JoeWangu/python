from django.urls import path
from . import views

urlpatterns = [
    path('', views.comment_list, name='list'),
    path('<id>/', views.comment_detail, name = 'det'),
    path('<id>/del/', views.comment_delete, name='del'),
]
