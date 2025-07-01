from django.contrib import admin
from django.urls import path, include
from accounts.urls import urlspatterns as AcountAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(AcountAPI)),
]