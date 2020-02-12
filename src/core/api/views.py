from django.urls import reverse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Course, Feedback, Assignment
from accounts.models import TeachingAssistantProfile

from core.api.serializers import CourseSerializer, FeedbackListSerializer, FeedbackSerializer, AssignmentSerializer, \
    SubmitFeedbackSerializer, ApproveFeedbackSerializer, AssignTaSerializer

from datetime import date


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self, queryset=None):
        if self.action == 'current':
            return self.queryset.filter(supervisor__user=self.request.user)
        else:
            return super().get_queryset()

    @action(methods=['get'], detail=False)
    def current(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    def get_queryset(self, queryset=None):
        if self.action == 'assign':
            return TeachingAssistantProfile.objects.all()
        else:
            return super().get_queryset()

    def get_serializer_class(self):
        if self.action == 'assign':
            return AssignTaSerializer
        else:
            return self.serializer_class

    @action(methods=['get'], detail=False)
    def assign(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get_serializer_class(self):
        if self.action == 'current' or self.action == 'past':
            return FeedbackListSerializer
        if self.action == 'submit':
            return SubmitFeedbackSerializer
        if self.action == 'approval_current':
            return ApproveFeedbackSerializer
        else:
            return self.serializer_class

    def get_queryset(self, queryset=None):
        today = date.today()
        if self.action == 'past':
            return self.queryset.filter(
                assignment__teaching_assistant__user=self.request.user).exclude(
                date_submitted__month=today.month, date_submitted__year=today.year)
        elif self.action == 'current':
            return self.queryset.filter(
                assignment__teaching_assistant__user=self.request.user,
                date_submitted__month=today.month, date_submitted__year=today.year)
        elif self.action == 'submit':
            return Assignment.objects.filter(
                teaching_assistant__user=self.request.user
            ).exclude(id__in=Feedback.objects.filter(
                assignment__teaching_assistant__user=self.request.user,
                date_submitted__month=today.month, date_submitted__year=today.year).values_list('assignment'))
        elif self.action == 'approval_current':
            return self.queryset.filter(
                assignment__course__supervisor__user=self.request.user,
                date_submitted__month=today.month, date_submitted__year=today.year,
                status="1"
            )
        else:
            return super().get_queryset()

    @action(methods=['get'], detail=False)
    def past(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    @action(methods=['get'], detail=False)
    def current(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    @action(methods=['get'], detail=False)
    def submit(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

    @action(methods=['get'], detail=False)
    def approval_current(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)


class FeedbackCountView(APIView):
    def get(self, request, month, year):
        feedback_summary_list = [
            self.count_feedbacks('1', month, year),
            self.count_feedbacks('2', month, year),
            self.count_feedbacks('3', month, year)
        ]
        return Response(feedback_summary_list)

    @staticmethod
    def count_feedbacks(program, month, year):
        kwargs = {
            'date_submitted__month': month,
            'date_submitted__year': year,
            'assignment__teaching_assistant__program': program
        }
        return {
            'program': dict(TeachingAssistantProfile.PROGRAMS).get(program, program),
            'submitted': Feedback.objects.filter(**kwargs).count(),
            'pending': Feedback.objects.filter(status='1', **kwargs).count(),
            'approved': Feedback.objects.filter(status='2', **kwargs).count(),
            'rejected': Feedback.objects.filter(status='3', **kwargs).count(),
            'link': reverse('api:pdf', kwargs={'month': month, 'year': year, 'program': program})
        }
