from django.urls import path
from .views import index, read, postArticle, load_more, get_article, post_flutter
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name = 'index'),
    path('add/', postArticle, name = 'postArticle'),
    path('read/<str:id>/', read, name = 'read'),
    path('load-more', load_more,name='load-more'),
    path('get-article', get_article, name='get-article'),
    path('post-flutter', post_flutter, name='post-flutter')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)