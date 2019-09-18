from rest_framework.routers import DefaultRouter
from accounts.api.views import TeachingAssistantViewSet, UserViewSet
from accounts.api.views import TeachingAssistantCoordinatorViewSet, TeachingAssistantSupervisorViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r"ta-profiles", TeachingAssistantViewSet)
router.register(r"tac-profiles", TeachingAssistantCoordinatorViewSet)
router.register(r'tas-profiles', TeachingAssistantSupervisorViewSet)

urlpatterns = []

urlpatterns += router.urls
