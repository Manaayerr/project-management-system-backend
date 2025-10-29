from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Project, Task, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'role', 'phone', 'bio']

    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_authenticated:
            validated_data['user'] = user
        else:
            raise serializers.ValidationError("User must be logged in to create profile.")
        return super().create(validated_data)
        
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  
    class Meta:
        model = Comment
        fields = ['task', 'content', 'author']

    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_authenticated: 
            validated_data['author'] = user
        else:
            validated_data['author'] = None  
        return super().create(validated_data)
    
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