from django.urls import path
from trackingapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('addexpense/', views.addexpense, name='addexpense'),
    path('addbudget/', views.add_budget, name='addbudget'),
    path('manage/', views.manage, name='manage'),
    path('edit/<pk>/', views.edit, name='edit'),
    path('delete/<pk>/', views.delete, name='delete'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
