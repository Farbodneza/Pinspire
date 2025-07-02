from django.contrib import admin
from django.urls import path, include
from accounts.urls import urlspatterns as AcountAPI
from core.urls import urlpatterns as CoreAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(AcountAPI)),
    path('api/', include(CoreAPI)),
]