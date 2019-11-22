from django.urls import path
from rest_framework.routers import DefaultRouter
from core.api.views import CourseViewSet, FeedbackViewSet, AssignmentViewSet, FeedbackCountView

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'assignments', AssignmentViewSet)

urlpatterns = [
    path("feedback-count/", FeedbackCountView.as_view(), name='feedback-count')
]
urlpatterns += router.urls
