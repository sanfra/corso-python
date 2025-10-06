from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
    path('helloPost/', views.hello_world_post, name='helloPost'), 
]