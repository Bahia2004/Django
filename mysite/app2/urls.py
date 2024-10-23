from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app2_index'),
    path('services/', views.services, name='app2_services'),
]
