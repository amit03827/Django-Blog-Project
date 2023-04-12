from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('search', views.search, name='search'),
    path('post/<id>', views.single_post, name="single_post")
]
