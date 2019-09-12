from django.urls import include, path
from rest_framework.routers import DefaultRouter
from accounts.api.views import TeachingAssistantViewSet, UserViewSet, AuthenticationCheckAPIView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r"ta-profiles", TeachingAssistantViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('auth-check/', AuthenticationCheckAPIView.as_view(), name='auth-check')
]
