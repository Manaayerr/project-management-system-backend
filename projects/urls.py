from rest_framework import routers
from .views import ProjectViewSet, TaskViewSet, CommentViewSet, UserProfileViewSet

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('tasks', TaskViewSet)
router.register('comments', CommentViewSet)
router.register('profiles', UserProfileViewSet)

urlpatterns = router.urls
