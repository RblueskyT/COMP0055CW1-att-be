from django.urls import path
from . import views

urlpatterns = [
    # /example_api/
    # path('', views.index, name='index'),
    # /example_api/post_demo/
    # path('get_code', views.get_code, name='get_code'),
    path('get_github_url', views.get_github_url, name='get_github_url'),
]