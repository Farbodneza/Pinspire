from django.urls import path
from accounts.views import RegisterUserAPIView, LoginUserAPIView, LogoutUserAPIView, ProfileManagmentAPIView, ViewProfile


urlspatterns = [
    path('auth/register/', RegisterUserAPIView.as_view()),
    path('auth/login/', LoginUserAPIView.as_view()),
    path('auth/logout/', LogoutUserAPIView.as_view()),
    path('users/me/', ProfileManagmentAPIView.as_view()),
    path('users/<username>/', ViewProfile.as_view()),
]