from django.urls import path
from rest_framework.routers import DefaultRouter
from core.api.views import CourseViewSet, FeedbackViewSet, AssignmentViewSet, FeedbackCountView
from core.views import PDFRenderView

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'assignments', AssignmentViewSet)

urlpatterns = [
    path("feedback-count/<int:month>/<int:year>/", FeedbackCountView.as_view(), name='feedback-count'),
    path('pdf/<int:month>/<int:year>/<int:program>/', PDFRenderView.as_view(), name='pdf'),
]
urlpatterns += router.urls
