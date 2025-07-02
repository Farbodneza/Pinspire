from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import PinAPIViewset, BoardAPIViewset

router = DefaultRouter()
router.register(r'pins', PinAPIViewset, basename='pin')
router.register(r'boards', BoardAPIViewset, basename='board')

urlpatterns = [
    path('', include(router.urls)),
]
