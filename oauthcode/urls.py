from django.urls import path
from . import views

urlpatterns = [
    path('get_code', views.get_code, name='get_code'),
    path('get_github_url', views.get_github_url, name='get_github_url'),
]