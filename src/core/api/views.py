from rest_framework import viewsets
from rest_framework.decorators import action

from core.models import Course, Feedback, Assignment

from core.api.serializers import CourseSerializer, FeedbackListSerializer,FeedbackSerializer, AssignmentSerializer

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

    def get_serializer_class(self):
        return FeedbackListSerializer if self.action == 'current' or self.action == 'past' else self.serializer_class

    def get_queryset(self, queryset=None):
        today = date.today()
        if self.action == 'past':
            return self.queryset.filter(
                assignment__teaching_assistant__user=self.request.user).exclude(
                date_submitted__month=today.month)
        elif self.action == 'current':
            return self.queryset.filter(
                assignment__teaching_assistant__user=self.request.user,
                date_submitted__month=today.month)
        else:
            return super().get_queryset()

    @action(methods=['get'], detail=False)
    def past(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    @action(methods=['get'], detail=False)
    def current(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
