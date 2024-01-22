from django.urls import path
from user.views.api import CreateUser, LoginUser

urlpatterns = [
    path('', LoginUser.as_view(), name='login-api'),
    path('create-user-api/', CreateUser.as_view(), name='create-user-api'),
]
