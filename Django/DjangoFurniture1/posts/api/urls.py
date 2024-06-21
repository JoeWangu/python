from django.urls import path,include
from . import views

app_name = 'posts'

urlpatterns = [
    # path('create/', views.posts_create),
    # path('<id>/', views.posts_detail, name = 'detail'),
    # path('<id>/edit/', views.posts_update, name = 'update'),
    # path('<id>/delete/', views.posts_delete),
    # path('<id>/comments/', include('comments.urls')),
    # path('', views.posts_list, name='list'),
    path('', views.PostListAPIView.as_view()),
    path('create/', views.PostCreateAPIView.as_view(), name='create'),
    path('<int:pk>', views.PostDetailAPIView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.PostUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PostDeleteAPIView.as_view(), name='delete'),
    # path('<int:pk>/comments/', include('comments.api.urls')),
]
