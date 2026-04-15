from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Swagger UI
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema')),

    # Authentication endpoints
    path('register/', views.register, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Product endpoints
    path('', views.getData, name='get-products'),
    path('add/', views.addProduct, name='add-product'),
    path('update/<int:pk>/', views.updateProduct, name='update-product'),
    path('delete/<int:pk>/', views.productDelete, name='delete-product'),
    path('details/<int:pk>/', views.productDetail, name='product-detail'),
]