from rest_framework.routers import DefaultRouter
from accounts.api.views import TeachingAssistantViewSet, UserViewSet, TeachingAssistantCoordinatorViewSet, \
    TeachingAssistantSupervisorViewSet, OfficeViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r"ta-profiles", TeachingAssistantViewSet)
router.register(r"tac-profiles", TeachingAssistantCoordinatorViewSet)
router.register(r'tas-profiles', TeachingAssistantSupervisorViewSet)
router.register(r'office-profiles', OfficeViewSet)

urlpatterns = []

urlpatterns += router.urls
