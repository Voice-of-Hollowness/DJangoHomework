from django.urls import path
from .views import user_list, user_detail, add_users

urlpatterns = [
    path('users/', user_list, name='user_list'),
    path('users/<int:user_id>/', user_detail, name='user_detail'),
    path('users/add/', add_users, name='add_users'),
]
