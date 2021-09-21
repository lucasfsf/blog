"""Defines URLS patterns for blogs."""

from django.urls import path

from . import views

app_name= 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page for adding a new Blog Post
    path('new_post/', views.new_post, name='new_post'),
]