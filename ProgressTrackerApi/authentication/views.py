from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import ProfileSerializer, RegisterUserSerializer
from rest_framework.response import Response
from .models import UserProfile
from django.contrib.auth.models import User
# Create your views here.

class UserDetails(GenericAPIView):
    serializer_class = ProfileSerializer

    def get(self, request):
        profile = UserProfile.objects.get(user=self.request.user)
        user_data = self.get_serializer(profile)
        return Response(user_data.data)


class RegisterUser(GenericAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request):
        user_serializer = self.get_serializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        first_name = user_serializer.validated_data['first_name']
        last_name = user_serializer.validated_data['last_name']
        username = user_serializer.validated_data['username']
        password = user_serializer.validated_data['password']
        email = user_serializer.validated_data['email']
        User.objects.create_user(username=username, password=password, last_name=last_name, first_name=first_name, email=email)
        #'username', 'password', 'first_name', 'last_name', 'email'
        return Response({
            'status': 'success'
        })
