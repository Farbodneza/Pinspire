from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from accounts.models import CustomUser
from rest_framework.response import Response
from rest_framework import viewsets, status
from accounts.serializers import CustomuserRegisterSerializer, CustomuserLoginSerializer, EditProfileSerializer
# Create your views here.

class RegisterUserAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomuserRegisterSerializer


class LoginUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomuserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)  
            return Response({
                'user_id': user.id,
                'username': user.username,
                'message': 'Login successful'
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
    

class LogoutUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_204_NO_CONTENT)
    

class ProfileManagmentAPIView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    def get_object(self):
        return self.request.user
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return EditProfileSerializer
        return CustomuserRegisterSerializer
    

class ViewProfile(generics.RetrieveAPIView):
    serializer_class = CustomuserRegisterSerializer
    queryset = CustomUser.objects.all()
    lookup_field = 'username'
    lookup_url_kwarg = 'username'

