from rest_framework import serializers
from accounts.serializers import CustomuserRegisterSerializer
from core.models import  Pin, Board, Likes, Wishlist


class PinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pin
        fields = '__all__'


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'
        # depth = 1


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'


class WishlistSerializer(serializers.Serializer):
    class Meta:
        model = Wishlist
        fields = '__all__'
    # def validate_pins(self, value):
        