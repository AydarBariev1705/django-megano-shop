from django.urls import path
from .views import (ProfileDetails,
                    PasswordUpdate,
                    AvatarUpdate,
                    UserLoginView,
                    UserLogoutView,
                    UserRegisterView)

urlpatterns = [
    path('api/profile', ProfileDetails.as_view(), name='profile_details'),
    path('api/profile/password', PasswordUpdate.as_view(), name='pas_update'),
    path('api/profile/avatar', AvatarUpdate.as_view(), name='avatar_update'),
    path('api/sign-in', UserLoginView.as_view(), name='login'),
    path('api/sign-out', UserLogoutView.as_view(), name='logout'),
    path('api/sign-up', UserRegisterView.as_view(), name='register'),

]
