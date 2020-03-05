from django.urls import path

from .views import new_link

urlpatterns = [
    path('', new_link, name='new_link'),
    ]