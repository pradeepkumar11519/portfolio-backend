from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from .helpers import getdate,gettime
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username','password')
    def create(self, data):
        user = User.objects.create(
            email=data.get('email'),
            password = data.get('password'),
            username=data.get('username'),
            )
        user.set_password(data.get('password'))
        user.save()
        return user
    def validate(seld,data):
        user_email = User.objects.filter(email=data.get('email')).exists()
        if user_email:
            raise serializers.ValidationError({'error':'Email Already Exists Try With Another'})
        else:
            return data 
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoComment
        fields = "__all__"
    def create(self,data):
        if data.get('parent'):
            parentname = data.get('parent').user.username
            parentcomment = data.get('parent').comment
        else:
            parentname = None
            parentcomment = None
        comment = VideoComment.objects.create(comment = data.get('comment'),user = data.get("user"),parent = data.get("parent"),datestamp = getdate(),timestamp=gettime(),parent_name = parentname,parent_comment = parentcomment)
        comment.save()
        return comment

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"