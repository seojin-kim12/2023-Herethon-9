from django.contrib import admin
from django.urls import path
from .views import create, post_list, post_detail

urlpatterns = [
    path('create/<int:customUser_id>/', create, name="create"),
    path('list/', post_list, name='post_list'),
    path('<int:post_id>/<int:customUser_id>', post_detail, name='post_detail'),
]