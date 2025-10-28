from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Project, Task, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']
        

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model =UserProfile
        fields = ['id','user','role','phone','bio']
        
class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'task', 'author']

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'title', 'due_date', 'status', 'project', 'assigned_to', 'created_at', 'updated_at', 'comments']

class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'status', 'owner', 'created_at', 'updated_at', 'tasks']