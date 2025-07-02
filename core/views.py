from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from core.models import Pin, Board
from core.serializers import PinSerializer, BoardSerializer
from rest_framework.response import Response
from rest_framework import viewsets, filters
from core.permissions import IsPonOwnerPermission, IsBoardOwner
from rest_framework.permissions import IsAuthenticated , AllowAny


class PinAPIViewset(viewsets.ModelViewSet):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    search_fields = ['title', 'tags']
    lookup_field = "pk"
    lookup_url_kwarg = 'pk'

    
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsPonOwnerPermission, IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    

    def searh(self, request, *args, **kwargs):
        queryset = self.get_queryset
        filter = filters.SearchFilter()
        result = filter.filter_queryset(request, queryset, self)
        serializer = PinSerializer(result, many=True)
        return Response(serializer.data)


class BoardAPIViewset(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    lookup_field = "pk"
    lookup_url_kwarg = 'pk'


    def get_permissions(self):
        if self.action in ['list', 'crate']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsBoardOwner]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]