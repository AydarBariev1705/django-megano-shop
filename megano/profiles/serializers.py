from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id',
            'user',
            'fullName',
            'email',
            'avatar',
            'phone',
        )

    avatar = serializers.SerializerMethodField()

    def get_avatar(self, instance):
        return {'src': f'/media/{instance.avatar.name}',
                'alt': f'{instance.fullName}'}


class PasswordUpdateSerializer(serializers.Serializer):
    currentPassword = serializers.CharField(required=True,)
    newPassword = serializers.CharField(required=True,)
    # newPassword_repeat = serializers.CharField(required=True,)


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = 'avatar',


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )
