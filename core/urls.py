from django.urls import path
from . import views

# app name used in url tag for example {% url 'appname:path_name' %}

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<slug:slug>', views.post, name='post')
]