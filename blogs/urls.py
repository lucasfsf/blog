"""Defines URLS patterns for blogs."""

from django.urls import path

from . import views

app_name= 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page for adding a new Blog Post
    path('new_post/', views.new_post, name='new_post'),
    # Page for editing a Blog Post
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]