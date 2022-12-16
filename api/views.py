import random
from re import M
from xml.etree.ElementTree import Comment
from django.shortcuts import render
from rest_framework.generics import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .helpers import *
from .models import *
# Create your views here.


# Create your views here.
class Signup(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Login(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        email = request.data['email']

        # checking for errors
        user = User.objects.filter(username=username).first()
        
        print(user)
        if user is None:
                    return Response({'error': 'invalid username or password'}, status=status.HTTP_404_NOT_FOUND)
        if not user.check_password(password):
                    return Response({'error': 'invalid username or password'},status=status.HTTP_404_NOT_FOUND)
        else:
            if email == user.email:
                    refresh = RefreshToken.for_user(user)
                    user.last_login = datetime.datetime.now()
                    user.save()
                    return Response({
                        'message': 'login successfull',
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'username':user.username,
                        'last_login_date':getdate(),
                        'last_login_time':gettime(),
                        'email':user.email},
                        status=status.HTTP_200_OK)
                    
                    
            else:
                return Response({'errors':'email not matched'},status=status.HTTP_404_NOT_FOUND)


class Contact(CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactSerializer


class ListComment(ListAPIView):
    serializer_class = CommentSerializer
    queryset = VideoComment.objects.all()

class CreateComment(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = VideoComment.objects.all()
    

class DeleteUpdateComment(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = VideoComment.objects.all()
    serializer_class = CommentSerializer