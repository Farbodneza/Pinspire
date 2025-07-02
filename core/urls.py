from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import PinAPIViewset  

router = DefaultRouter()
router.register(r'pins', PinAPIViewset, basename='pin')

urlpatterns = [
    path('', include(router.urls)),
]
