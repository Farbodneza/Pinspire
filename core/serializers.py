from rest_framework import serializers
from core.models import CustomUser, Pin, Board


class CustomuserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
    def create(self,validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            )
        user.set_password[validated_data['password']]
        user.save()
        return user
    # to repersetiotion
    # to internall valeu
    

class CustomuserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)


class ProfileManagmentserializer(serializers.Serializer):
    profile_picture = serializers.CharField()
    bio = serializers.CharField()


class PinSerializer(serializers.ModelSerializer):
    owner = CustomuserRegisterSerializer()
    class Meta:
        model = Pin
        fields = '__all__'


class BoardSerializer(serializers.ModelSerializer):
    owner = CustomuserRegisterSerializer()
    pins = PinSerializer()
    class Meta:
        model = Board
        fiels = "__all__"
