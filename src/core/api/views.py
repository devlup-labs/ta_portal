from rest_framework import viewsets
from rest_framework.decorators import action

from core.models import Course, Feedback, Assignment

from core.api.serializers import CourseSerializer, FeedbackSerializer, AssignmentSerializer

from datetime import date


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get_queryset(self, queryset=None):
        today = date.today()
        return self.queryset.filter(
            assignment__teaching_assistant__user=self.request.user).exclude(
            date_submitted__month=today.month) if self.action == 'past' else super().get_queryset()

    @action(methods=['get'], detail=False)
    def past(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
