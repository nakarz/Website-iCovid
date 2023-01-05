from django.urls import path
from .views import make_announcement, get_announcement, see_log

urlpatterns = [
    path('make-announcement', make_announcement, name='make_announcement'),
    path('get-announcement', get_announcement, name='get_announcement'),
    path('', see_log, name='see_log'),
]
