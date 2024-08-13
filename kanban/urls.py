from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet, SubtaskViewSet

router = DefaultRouter()
router.register(r'project', ProjectViewSet, basename='project')
router.register(r'task', TaskViewSet, basename='task')
router.register(r'subtask', SubtaskViewSet, basename='subtask')

urlpatterns = router.urls