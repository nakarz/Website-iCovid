from django.urls import path
from .views import index, updateFilterApi, getFilterApi

urlpatterns = [
    path('', index, name='index'),
    path('api/update/', updateFilterApi, name='updateapi'),
    path('api/get/', getFilterApi, name='getapi'),
]