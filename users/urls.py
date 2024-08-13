from rest_framework.routers import DefaultRouter
from .views import UserRegisterView

router = DefaultRouter()
router.register(r'users', UserRegisterView, basename='users')

urlpatterns = router.urls