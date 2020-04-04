from django.urls import path

from hola_docker import views

urlpatterns = [
    path('hola/', views.hola, name='hola'),
]