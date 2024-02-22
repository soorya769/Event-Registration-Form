from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_form, name='registration_form'),
    path('register/', views.register, name='register'),
]
