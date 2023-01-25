from django.urls import path, include

from . import views, views_registration

urlpatterns = [
    path('', views.index, name='index'),
    #path('profile/', include('oztes.mgmt.registration.urls')),
    #path('profile/', views_registration.anonymous, name='anonymous registration'),
    path('profile/', views_registration.agent_list, name='anonymous profile'),
    path('profile/<uuid:pk>/', views_registration.agent_detail, name='known user registration'),
    path('emp/', views_registration.emp_list, name='anonymous profile'),
]