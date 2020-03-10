from django.urls import path

from .views import new_link, get_shortener, get_url_rank

urlpatterns = [
    path('', new_link, name='new_link'),
    path('rank/', get_url_rank, name='get_url_rank'),
    path('<str:short_url>/', get_shortener, name='get_shortener'),
    ]