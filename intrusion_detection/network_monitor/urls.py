from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Set this as the homepage
    path('network/', views.index, name='network'),
]