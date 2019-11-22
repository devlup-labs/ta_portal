from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Course, Feedback, Assignment

from core.api.serializers import CourseSerializer, FeedbackListSerializer, FeedbackSerializer, AssignmentSerializer, \
    SubmitFeedbackSerializer, ApproveFeedbackSerializer

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
                date_submitted__month=today.month)
        elif self.action == 'current':
            return self.queryset.filter(
                assignment__teaching_assistant__user=self.request.user,
                date_submitted__month=today.month)
        elif self.action == 'submit':
            return Assignment.objects.filter(
                teaching_assistant__user=self.request.user
            ).exclude(id__in=Feedback.objects.filter(
                assignment__teaching_assistant__user=self.request.user,
                date_submitted__month=today.month).values_list('assignment'))
        elif self.action == 'approval_current':
            return self.queryset.filter(
                assignment__course__supervisor__user=self.request.user,
                date_submitted__month=today.month,
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

    def get(self, request, format=None):
        today = date.today()
        mtech_submitted = Feedback.objects.filter(date_submitted__month=today.month,
                                                  assignment__teaching_assistant__program="1").count()
        mtech_approved = Feedback.objects.filter(date_submitted__month=today.month,
                                                 assignment__teaching_assistant__program="1", status="2").count()
        mtech_rejected = Feedback.objects.filter(date_submitted__month=today.month,
                                                 assignment__teaching_assistant__program="1", status="3").count()
        mtech_pending = Feedback.objects.filter(date_submitted__month=today.month,
                                                assignment__teaching_assistant__program="1", status="1").count()

        phd_mhrd_submitted = Feedback.objects.filter(date_submitted__month=today.month,
                                                     assignment__teaching_assistant__program="2").count()
        phd_mhrd_approved = Feedback.objects.filter(date_submitted__month=today.month,
                                                    assignment__teaching_assistant__program="2", status="2").count()
        phd_mhrd_rejected = Feedback.objects.filter(date_submitted__month=today.month,
                                                    assignment__teaching_assistant__program="2", status="3").count()
        phd_mhrd_pending = Feedback.objects.filter(date_submitted__month=today.month,
                                                   assignment__teaching_assistant__program="2", status="1").count()

        phd_vss_submitted = Feedback.objects.filter(date_submitted__month=today.month,
                                                    assignment__teaching_assistant__program="3").count()
        phd_vss_approved = Feedback.objects.filter(date_submitted__month=today.month,
                                                   assignment__teaching_assistant__program="3", status="2").count()
        phd_vss_rejected = Feedback.objects.filter(date_submitted__month=today.month,
                                                   assignment__teaching_assistant__program="3", status="3").count()
        phd_vss_pending = Feedback.objects.filter(date_submitted__month=today.month,
                                                  assignment__teaching_assistant__program="3", status="1").count()

        content = [
            {
                "programme": 'M.Tech',
                "submitted": mtech_submitted,
                "approved": mtech_approved,
                "rejected": mtech_rejected,
                "pending": mtech_pending,
                "link": 'localhost:8000/pdf/1/'
            },
            {
                "programme": 'Ph.D MDRH',
                "submitted": phd_mhrd_submitted,
                "approved": phd_mhrd_approved,
                "rejected": phd_mhrd_rejected,
                "pending": phd_mhrd_pending,
                "link": 'localhost:8000/pdf/2/'
            },
            {
                "programme": 'Ph.D VSS',
                "submitted": phd_vss_submitted,
                "approved": phd_vss_approved,
                "rejected": phd_vss_rejected,
                "pending": phd_vss_pending,
                "link": 'localhost:8000/pdf/3/'
            }
        ]
        return Response(content)
