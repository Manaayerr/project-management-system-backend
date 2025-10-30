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
router.register('tasks', TaskViewSet)
router.register('comments', CommentViewSet)
router.register('profiles', UserProfileViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'), 
]

urlpatterns += router.urls
