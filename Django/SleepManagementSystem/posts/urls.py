from django.urls.conf import path
from .views import home, about , allposts, post, postlist, search
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('post/<slug>', post,name='post'),
    path('about/', about,name='about'),
    path('postlist/<slug>', postlist,name='postlist'),
    path('posts/', allposts, name='allposts'),
    path('search/', search, name = 'search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
