from django.urls import path
from home.views import index,edit_feedback,delete_feedback,get_data,add_data_flutter


urlpatterns = [
    path('', index,name='index'),
    path('edit_feedback', edit_feedback, name='edit_feedback'),
    path('delete_feedback', delete_feedback, name='delete_feedback'),
    path('get-data/',get_data,name='get_data'),
    path('add-data',add_data_flutter, name='add-data')
    # TODO Add friends path using friend_list Views
]
