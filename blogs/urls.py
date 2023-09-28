from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('my_blogs', myBlog, name='my_blog'),
    path('create_blog', createBlog, name='create_blog'),
    path('get_blogs/<str:pk>', getBlog, name='get_blog'),
    path('', blogs, name='blog'),
    path('update_blog/<int:pk>/', updateBlog, name='update_blog'),
    path('delete_blog/<int:pk>/', deleteBlog, name='delete_blog'),

]