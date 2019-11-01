from rest_framework import serializers

from core.models import Course, Feedback, Assignment
from datetime import datetime


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'


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
        exclude = ['course', 'teaching_assistant']
