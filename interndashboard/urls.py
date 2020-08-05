from django.urls import path
from . import views

urlpatterns = [
    path('', views.retail, name='retail_report'),
    path('marketing/', views.marketing, name='marketing_report'),
]