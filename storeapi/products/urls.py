from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views

urlpatterns = [
    # Swagger UI
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema')),

    path('', views.getData, name='get-products'),
    path('add/', views.addProduct, name='add-product'),
    path('update/<int:pk>/', views.updateProduct, name='update-product'),
    path('delete/<int:pk>/', views.productDelete, name='delete-product'),
    path('details/<int:pk>/', views.productDetail, name='product-detail'),
]