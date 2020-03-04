from django.urls import path

urlpatterns = [
    path('', views.new_link, name='new_link')
]
