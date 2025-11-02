from django.contrib.auth.models import User
from rest_framework import generics,viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Project,Task,Comment,UserProfile
from.serializers import(
    ProjectSerializer,
    TaskSerializer,
    CommentSerializer,
    UserProfileSerializer,
    RegisterSerializer,
)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    
    
class ProjectViewSet(viewsets.ModelViewSet):
    queryset= Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        project_pk =self.kwargs.get('project_pk')
        
        if project_pk:
            return Task.objects.filter(project_id=project_pk)
        return Task.objects.all()
    
    def perform_create(self, serializer):
        if not self.request.data.get('assigned_to_id')and not self.request.data.get('assigned_to'):
            serializer.save(assigned_to=self.request.user) 
        else:
            serializer.save()
    
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = IsAuthenticated

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context