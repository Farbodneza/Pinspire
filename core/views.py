from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from core.models import Pin, Board, Likes, Wishlist
from core.serializers import PinSerializer, BoardSerializer, LikeSerializer, WishlistSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from core.permissions import IsPonOwnerPermission, IsBoardOwner
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.decorators import action


class PinAPIViewset(viewsets.ModelViewSet):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    

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

    # TODO view ha bar asaase perm haa jodaa
    def get_permissions(self):
        if self.action in ['list', 'crate']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            # TODO IsAuthenticated dakhel IsBoardOwner check shavad
            permission_classes = [IsAuthenticated, IsBoardOwner] 
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    

class LikeAPIViewset(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
    lookup_url_kwarg = 'id'


class WishlistViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user
        wishlist_pins = Pin.objects.filter(wishlist__user=user)
        serializer = PinSerializer(wishlist_pins, many=True)
        return Response(serializer.data)
    

    @action(detail=True, methods=['post', 'delete'])
    def wishlist(self, request, pk=None):
        if request.method == 'POST':
            user = request.user
            pin = Pin.objects.get(pk=pk)
            Wishlist.objects.create(user=user, pin=pin)
            return Response({'detail': 'Pin added to wishlist'}, status=status.HTTP_201_CREATED)

        elif request.method == 'DELETE':
            deleted= Wishlist.objects.filter(user=user, pin=pin).delete()
            return Response({'detail': 'Pin removed from wishlist'}, status=status.HTTP_204_NO_CONTENT)