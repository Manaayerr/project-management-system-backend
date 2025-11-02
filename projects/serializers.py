from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Project, Task, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        
# -----------------------------------------------------------------

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True,min_length=6)
    
    class Meta: 
        model =User
        fields = ['id','username','email','password']
        
    def create(self,validated_data):
        user= User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email',''),
            password=validated_data['password']
        )
        return user
        
        
# ---------------------------------------------------------------------
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
    
# ----------------------------------------------------------------------------------------------------
        
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  
    class Meta:
        model = Comment
        fields = ['id', 'task', 'content', 'author', 'created_at']

    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_authenticated: 
            validated_data['author'] = user
        else:
            validated_data['author'] = None  
        return super().create(validated_data)
    
# ---------------------------------------------------------------------------------------------------------
    
class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    assigned_to_id = serializers.PrimaryKeyRelatedField(
        source ='assigend_to',queryset=User.objects.all(), write_only=True, required=False
    )
    
    project_id = serializers.PrimaryKeyRelatedField(
        source='project', queryset=Project.objects.all(), write_only=True
    )
    
    class Meta:
        model = Task
fields = [
            'id', 
            'title', 
            'due_date', 
            'status', 
            'project_id',     
            'assigned_to',    
            'assigned_to_id', 
            'created_at', 
            'updated_at', 
            'comments'
        ]        
# -------------------------------------------------------------------------------------------------------------------------

class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'status', 'owner', 'created_at', 'updated_at', 'tasks']