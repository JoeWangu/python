from django.urls import path
# from .views import home,SignUp
from .views import home,signup_login

urlpatterns = [
    path('', home, name='home'),
    # path('signup_login/', SignUp.as_view(), name='signup' ),
    path('signup_login/', signup_login, name='signup_login')
]
