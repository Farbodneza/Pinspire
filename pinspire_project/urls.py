from django.contrib import admin
from django.urls import path, include
from accounts.urls import urlspatterns as AcountAPI
from core.urls import urlpatterns as CoreAPI
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from test.urls import urlpatterns as shop
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(title="pinspire",
                 default_version='v1',
                 description='pinspire api address'),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(AcountAPI)),
    path('api/', include(CoreAPI)),
    path('api/', include(shop)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]