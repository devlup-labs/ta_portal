from django.urls import path
from rest_framework.routers import DefaultRouter
from accounts.api.views import TeachingAssistantViewSet, UserViewSet, TeachingAssistantCoordinatorViewSet, \
    TeachingAssistantSupervisorViewSet, OfficeViewSet, ChangePasswordView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r"ta-profiles", TeachingAssistantViewSet)
router.register(r"tac-profiles", TeachingAssistantCoordinatorViewSet)
router.register(r'tas-profiles', TeachingAssistantSupervisorViewSet)
router.register(r'office-profiles', OfficeViewSet)

urlpatterns = [
    path('change-password/', ChangePasswordView.as_view(), name='change-password')
]

urlpatterns += router.urls
