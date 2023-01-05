"""icovid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import index
from django.conf.urls.static import static
from django.conf import settings
from .views import index
import news.urls as news
import tracker.urls as tracker
from django.conf import settings
import forum.urls as forum
import utilities.urls as utilities


urlpatterns = [
    path('', index),
    path('forum/', include(forum)),
    path('admin/', admin.site.urls),
    path('administrator/', include('utilities.urls')),
    path('profileapp/',include('profileapp.urls')),
    path('', index),
    path('forum/', include(forum)),
    path('tracker/', include(tracker)),
    path('auth/', include(('authentication.urls', 'authentication'), namespace='authentication')),
    path('news/', include(('news.urls', 'news'), namespace='news')),
    path('home/', include(('home.urls', 'home'), namespace='home/')),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
