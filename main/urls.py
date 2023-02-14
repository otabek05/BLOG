from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    
    path('complete/<str:pk>/', views.complete_todo, name='complete'),
    path('delete/<str:pk>/', views.delete_todo, name='delete'),
]

