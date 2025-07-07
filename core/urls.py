from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import PinAPIViewset, BoardAPIViewset, WishlistViewSet, LikeAPIViewset



router = DefaultRouter()
router.register(r'pins', PinAPIViewset, basename='pin')
router.register(r'boards', BoardAPIViewset, basename='board')
router.register(r'wishlist', WishlistViewSet, basename='wishlist')
router.register(r'likes', LikeAPIViewset, basename='likes')

urlpatterns = [
    path('', include(router.urls)),
]

