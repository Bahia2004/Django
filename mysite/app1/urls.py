from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app1_index'),
    path('about/', views.about, name='app1_about'),
    path('contact/', views.contact, name='app1_contact'),
    path('home/', views.home, name='app1_home'),  # Add home URL
]
