from django.contrib import admin

from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from usuarios.views import get_csrf_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('produtos.urls')),
    path('api/', include('funcionarios.urls')),

    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('get_csrf_token/', get_csrf_token, name='get_csrf_token')
]
