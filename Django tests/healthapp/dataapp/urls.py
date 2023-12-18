from django.urls import path
from django.contrib.auth import views as auth_views
from dataapp.views import index, create, retrieve, update, delete, register

urlpatterns = [
    path('', index, name = 'index'),
    path('create/', create, name = 'create'),
    path('retrieve/', retrieve, name='retrieve'),
    path('update/<str:pk>/', update, name='update'),
    path('delete/<str:pk>/', delete, name='delete'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name = 'register'),
]
