from django.urls import path,include
from . import views

app_name = 'posts'

urlpatterns = [
    path('create/', views.posts_create),
    path('<id>/', views.posts_detail, name = 'detail'),
    path('<id>/edit/', views.posts_update, name = 'update'),
    path('<id>/delete/', views.posts_delete),
    path('<id>/comments/', include('comments.urls')),
    path('', views.posts_list, name='list'),
]
