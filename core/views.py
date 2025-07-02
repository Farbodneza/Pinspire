from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from core.models import Pin
from core.serializers import PinSerializer
from rest_framework.response import Response
from rest_framework import viewsets, filters


class PinAPIViewset(viewsets.ModelViewSet, generics.GetOrRaiseMixin):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    search_fields = ['title', 'tags']
    lookup_field = "pk"
    lookup_url_kwarg = 'pk'
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = ["AllowAny"]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classe = ['Owner-only']
        else:
            permission_classes = ["IsAuthenticated"]
    
    
    def searh(self, request, *args, **kwargs):
        queryset = self.get_queryset
        filter = filters.SearchFilter()
        result = filter.filter_queryset(request, queryset, self)
        serializer = PinSerializer(result, many=True)
        return Response(serializer.data)

