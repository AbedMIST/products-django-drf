from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addProduct),
    path('update/<int:pk>/', views.updateProduct),
    path('delete/<int:pk>/', views.productDelete),
    path('details/<int:pk>/', views.productDetail),
]