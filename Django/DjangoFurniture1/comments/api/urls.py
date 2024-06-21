from django.urls import path
from comments.api import views

app_name = 'comments'

urlpatterns = [
    path('', views.CommentListAPIView.as_view(), name='list'),
    path('<int:pk>/', views.CommentDetailAPIView.as_view(), name='detail'),
    # path('<id>/del/', views.comment_delete, name='del'),
]

