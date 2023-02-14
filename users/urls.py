from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logut/', views.user_logout, name='logout'),
    path('registration/', views.user_register, name='register'),
    path('profile/', views.user_profile, name='profile'),
]
