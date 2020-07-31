from . import views
from django.urls import path

urlpatterns = [
    path('list/', views.list, name='list'),
    path('create/', views.create, name='create'),
    # path('result/', views.result, name='result'),
]