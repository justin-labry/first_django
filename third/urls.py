from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('test/', views.test, name='test'),
    path('create/', views.create, name='restaurant-create'),
    path('update/', views.update, name='restaurant-update'),
    path('detail/', views.detail, name='restaurant-detail'),
    path('delete/', views.delete, name='restaurant-delete'),
]