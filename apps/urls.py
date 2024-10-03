from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from .views import (
    UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView,
    ProductListAPIView, CategoryListAPIView, ProductDetailAPIView, ProductCreateAPIView
)


urlpatterns = [
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Users
    path('users/', UserListCreateAPIView.as_view(), name='user_list'),
    path('user-rud/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user_rud'),

    # Products
    path('products/', ProductListAPIView.as_view(), name='product_list'),
    path('product-detail/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('product-create/', ProductCreateAPIView.as_view(), name='product_create'),

    # Categories
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),

]