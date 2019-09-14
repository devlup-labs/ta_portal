from django.urls import include, path
from rest_framework.routers import DefaultRouter
from accounts.api.views import TeachingAssistantViewSet, UserViewSet, AuthenticationCheckAPIView

from accounts.api.views import TeachingAssistantCoordinatorViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r"ta-profiles", TeachingAssistantViewSet)
router.register(r"tac-profiles", TeachingAssistantCoordinatorViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('auth-check/', AuthenticationCheckAPIView.as_view(), name='auth-check')
]
