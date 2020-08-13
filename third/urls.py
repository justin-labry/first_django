from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('test/', views.test, name='test'),
    path('create/', views.create, name='restaurant-create'),
    path('update/<int:restaurant_id>', views.update, name='restaurant-update'),
    # path('detail/', views.detail, name='restaurant-detail'),
    path('delete/<int:restaurant_id>', views.delete, name='restaurant-delete'),

    path('restaurant/<int:restaurant_id>/review/create/', views.review_create, name='review-create'),
    path('restaurant/<int:restaurant_id>/', views.detail, name='restaurant-detail'),

    path('restaurant/<int:restaurant_id>/review/delete/<int:review_id>', views.review_delete, name='review-delete'),
    path('review/list/', views.review_list, name='review-list'),
]