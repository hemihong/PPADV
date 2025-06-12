
from django.contrib import admin
from django.urls import path
from my_app import  views
from my_app.templates.Views import category_views

urlpatterns = [
    path("",views.home),
    path("content",views.content),
    #----------------categories-----------------
    path("category/index",category_views.index),
]
