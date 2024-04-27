import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile
from .serializers import (ProfileSerializer,
                          PasswordUpdateSerializer,
                          AvatarSerializer,
                          UserSerializer)


class ProfileDetails(APIView):
    def get(self, request: Request, ) -> Response:
        user = request.user.pk
        profile = Profile.objects.get(user_id=user)
        serialized = ProfileSerializer(profile, many=False)
        return Response(serialized.data)

    def post(self, request: Request, ) -> Response:
        user = request.user.pk
        profile = Profile.objects.get(user_id=user)
        profile.fullName = request.data.get('fullName')
        profile.phone = request.data.get('phone')
        profile.email = request.data.get('email')
        profile.save()
        serialized = ProfileSerializer(profile, many=False)
        return Response(serialized.data)


class PasswordUpdate(GenericAPIView, UpdateModelMixin):
    serializer_class = PasswordUpdateSerializer

    def get_object(self):
        return self.request.user

    def post(self, *args, **kwargs):
        return self.update(self.request, *args, **kwargs)

    def update(self, request: Request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(request.data)

        if not self.object.check_password(
                serializer.data.get("currentPassword")
        ):
            return Response(
                {'Error': 'Wrong Current Password'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        self.object.set_password(serializer.data.get('newPassword'))
        self.object.save()
        return Response(
            'Update successful',
            status=status.HTTP_200_OK,
        )


class AvatarUpdate(APIView):
    serializer_class = AvatarSerializer

    def post(self, request: Request, ) -> Response:
        new_avatar = request.FILES["avatar"]
        user = request.user.pk
        profile = Profile.objects.get(user_id=user)
        profile.avatar = new_avatar
        profile.save()

        return Response(
            'Update successful',
            status=status.HTTP_200_OK,
        )


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('profiles:login')


# {"username":"admin",
#  "password": "12345"}
class UserLoginView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request: Request) -> Response:

        user_auth_data = json.loads(list(request.data.dict().keys())[0])
        print(user_auth_data['username'])
        print(user_auth_data['password'])

        user_auth = authenticate(
            username=user_auth_data['username'],
            password=user_auth_data['password']
        )

        if user_auth:
            login(request, user_auth)
            return Response(
                'Login successful',
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                'Login failed',
                status=status.HTTP_401_UNAUTHORIZED,
            )


class UserRegisterView(APIView):
    def post(self, request: Request) -> Response:
        user_register_data = json.loads(list(request.data.dict().keys())[0])
        username = user_register_data.get('username')
        name = user_register_data.get('name')
        password = user_register_data.get('password')

        if User.objects.filter(username=username).exists():
            return Response(
                'Username is already taken',
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            new_user = User.objects.create_user(
                username=username,
                password=password,
            )
            Profile.objects.create(
                user=new_user,
                fullName=name,
            )
            user_auth = authenticate(
                username=username,
                password=password
            )
            login(request, user_auth)

            return Response(
                'Successful registration',
                status=status.HTTP_201_CREATED,
            )
