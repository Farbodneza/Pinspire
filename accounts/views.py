from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from accounts.models import CustomUser
from rest_framework.response import Response
from rest_framework import viewsets, status
from accounts.serializers import CustomuserRegisterSerializer, CustomuserLoginSerializer
# Create your views here.

class RegisterUserAPIView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomuserRegisterSerializer


class LoginUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomuserLoginSerializer
        serializer.is_valid(data=request.data)

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
