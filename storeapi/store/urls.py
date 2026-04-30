from django.urls import path
from . import views

urlpatterns = [
    path('stores/', views.getStores, name='get-stores'),
    path('stores/<int:pk>/', views.storeDetail, name='store-detail'),
    path('stores/add/', views.addStore, name='add-store'),
    path('stores/update/<int:pk>/', views.updateStore, name='update-store'),
    path('stores/delete/<int:pk>/', views.deleteStore, name='delete-store'),
]