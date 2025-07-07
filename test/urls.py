from django.urls import path, include
from rest_framework.routers import DefaultRouter
from test.views import ProductViewSet, CategoryViewSet


router = DefaultRouter()
router.register('products', ProductViewSet, 'product')
router.register('categories', CategoryViewSet, 'category')


urlpatterns = [
    path('', include(router.urls))
]