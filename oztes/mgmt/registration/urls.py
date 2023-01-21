from django.urls import path

from . import views

urlpatterns = [
    path('', views.anonymous, name='anonymous registration'),
    path('<uuid:pk>/', views.view_profile, name='known user registration'),
]