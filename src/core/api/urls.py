from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core.api.views import CourseViewSet, FeedbackViewSet, AssignmentViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'assignments', AssignmentViewSet)

urlpatterns = []
urlpatterns += router.urls
