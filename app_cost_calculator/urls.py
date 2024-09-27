# app_cost_calculator/urls.py
from django.contrib import admin
from django.urls import path
from calculator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('calculate-cost/', views.calculate_cost, name='calculate_cost'),
]
