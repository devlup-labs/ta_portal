from django.conf import settings
from rest_framework import serializers

from core.models import Course, Feedback, Assignment
from accounts.models import TeachingAssistantProfile
from datetime import datetime
from django.db.models import Sum


class CourseSerializer(serializers.ModelSerializer):
    supervisor_name = serializers.CharField(source='supervisor.user.get_full_name')
    assigned_ta = serializers.SerializerMethodField()

    class Meta:
        model = Course
        exclude = ['supervisor', ]

    def get_assigned_ta(self, instance):
        return instance.assignment_set.filter(is_active=True).count()


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'
        read_only_fields = ['is_active', ]

    def create(self, validated_data):
        assignment, created = Assignment.objects.update_or_create(
            course=validated_data.get('course'),
            teaching_assistant=validated_data.get('teaching_assistant'),
            is_active=True,
            defaults={'assigned_hours': validated_data.get('assigned_hours')}
        )
        return assignment


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class FeedbackListSerializer(serializers.ModelSerializer):
    course_code = serializers.CharField(source='assignment.course.code')
    course_name = serializers.CharField(source='assignment.course.name')
    ta_supervisor = serializers.CharField(source='assignment.course.supervisor')
    status = serializers.SerializerMethodField()
    due_by = serializers.ReadOnlyField(default="--")

    def get_status(self, value):
        return value.get_status_display()

    class Meta:
        model = Feedback
        exclude = ['assignment', ]


class SubmitFeedbackSerializer(serializers.ModelSerializer):
    course_code = serializers.CharField(source='course.code')
    course_name = serializers.CharField(source='course.name')
    ta_supervisor = serializers.CharField(source='course.supervisor')
    status = serializers.ReadOnlyField(default="Submit TA Release Request")
    due_by = serializers.ReadOnlyField(default="{} {}".format(datetime.now().strftime("%b"), 20))

    class Meta:
        model = Assignment
        exclude = ['course', 'teaching_assistant', 'is_active', 'assigned_hours']


class ApproveFeedbackSerializer(serializers.ModelSerializer):
    course_code = serializers.CharField(source='assignment.course.code')
    name = serializers.CharField(source='assignment.teaching_assistant.user.get_full_name')
    roll_no = serializers.CharField(source='assignment.teaching_assistant.roll_no')

    class Meta:
        model = Feedback
        exclude = ['assignment', 'date_approved', 'status']


class CourseTaSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.get_full_name')
    availability = serializers.SerializerMethodField()
    assigned_hours = serializers.SerializerMethodField()

    class Meta:
        model = TeachingAssistantProfile
        fields = ['id', 'roll_no', 'availability', 'name', 'program', 'assigned_hours']

    def get_availability(self, instance):
        return settings.MAX_TA_HOURS - (instance.assignment_set.filter(
            is_active=True).aggregate(Sum('assigned_hours'))['assigned_hours__sum'] or 0)

    def get_assigned_hours(self, instance):
        code = self.context.get("code")
        try:
            return instance.assignment_set.get(is_active=True, course__code=code).assigned_hours
        except Exception:
            return 0
