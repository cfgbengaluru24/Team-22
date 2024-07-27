from django.urls import path
from . import views

urlpatterns = [
    path('', views.fetch_default, name='fetch_default'),
]
