from django.urls import path

from . import views

urlpatterns = [
    path('', views.new_link, name='new_link')
]
