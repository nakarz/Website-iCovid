from django.urls import path, re_path
from django.conf.urls import url
from .views import *

app_name = 'forum'

urlpatterns = [
    path('', index, name='Forum'),
    path('postToForum/',post_to_forum,name='postToForum'),
    path('posts/<str:slug>/', forum_post_detail, name="detail"),
    path('api/ForumHome/', get_forum_list, name="getForumList"),
    path('api/addForum/', add_new_forum_flutter, name="addNewForum"),
]
