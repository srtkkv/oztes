from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', include('oztes.mgmt.registration.urls')),
]