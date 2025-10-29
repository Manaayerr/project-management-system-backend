from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, permissions
from .models import Project, Task, Comment, UserProfile
from .serializers import ProjectSerializer, TaskSerializer, CommentSerializer, UserProfileSerializer

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    queryset= Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(owner_id=1)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]
    
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context