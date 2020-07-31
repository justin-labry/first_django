from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('select/', views.select, name='select'),
    path('result/', views.result, name='result'),
]