from django.urls import path
from . import views

app_name = 'Yatube'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.group_posts, name='group'),
    path('group/<slug:slug>', views.group_posts, name='group_list'),
] 