from rest_framework import serializers
from accounts.serializers import CustomuserRegisterSerializer
from core.models import  Pin, Board


class PinSerializer(serializers.ModelSerializer):
    owner = CustomuserRegisterSerializer()
    class Meta:
        model = Pin
        fields = '__all__'


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'
