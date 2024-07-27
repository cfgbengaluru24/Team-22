# onboarding/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ensure this matches your view
    path('identify/', views.identify, name='identify'),
    path('save_data', views.save_data, name='save_data')
]
