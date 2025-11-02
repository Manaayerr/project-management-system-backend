from django.urls import path, include
from rest_framework import routers
from .views import (
    ProjectViewSet,
    TaskViewSet,
    CommentViewSet,
    UserProfileViewSet,
    RegisterView,
)

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('comments', CommentViewSet)
router.register('profiles', UserProfileViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('projects/<int:project_pk>/tasks',TaskViewSet.as_view({'get':'list','post': 'create'}),
        name='project-tasks-list'),
    
    path('projects/<int:project_pk>/tasks/<int:pk>/',TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), 
        name='project-task-detail'
    ),
]

urlpatterns += router.urls
