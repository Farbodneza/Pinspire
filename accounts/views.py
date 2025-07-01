from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from accounts.models import CustomUser
from accounts.serializers import CustomuserRegisterSerializer, CustomuserLoginSerializer
# Create your views here.

class RegisterUserAPIView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomuserRegisterSerializer



