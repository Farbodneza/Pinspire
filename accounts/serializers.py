from rest_framework import serializers
from accounts.models import CustomUser


class CustomuserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
            )
        user.set_password(validated_data['password'])
        user.save()
        return user
    # to repersetiotion
    # to internall valeu
    
class CustomuserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)


class EditProfileSerializer(serializers.Serializer): 
    profile_picture = serializers.CharField()
    bio = serializers.CharField()