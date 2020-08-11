from . import views
from django.urls import path

urlpatterns = [
    path('list/', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('confirm/', views.confirm, name='confirm'),
    # path('result/', views.result, name='result'),
]