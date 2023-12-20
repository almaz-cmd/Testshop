from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import include
from django.urls import path, include


urlpatterns = [
    path('api/products/', views.get_products, name='products'),
    path('api/products/export/', views.export_products, name='export_products'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('products/', include('products.urls')),
    path('api/', include('users.urls')),
    path('api/', include('products.urls')),
]


