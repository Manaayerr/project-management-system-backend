from rest_framework import routers
from .views import ProjectViewSet, TaskViewSet, CommentViewSet, UserProfileViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'profiles', UserProfileViewSet)

urlpatterns = router.urls
