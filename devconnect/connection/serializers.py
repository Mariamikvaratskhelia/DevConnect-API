from rest_framework import serializers
from .models import Profile, Post, Follow, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']        

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'bio', 'skills', 'experience']

class PostSerializer(serializers.ModelSerializer):  
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at'] 

class FollowSerializer(serializers.ModelSerializer):
    follower = UserSerializer(read_only=True)
    following = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following', 'created_at']
        

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']  
        