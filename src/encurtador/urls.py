from django.urls import path

from .views import new_link, get_shortener

urlpatterns = [
    path('', new_link, name='new_link'),
    path('<str:short_url>/', get_shortener, name='get_shortener')
    ]