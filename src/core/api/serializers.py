from rest_framework import serializers

from core.models import Course, Feedback, Assignment


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    course_code = serializers.CharField(source='assignment.course.code')
    course_name = serializers.CharField(source='assignment.course.name')
    ta_supervisor = serializers.CharField(source='assignment.course.supervisor')
    status = serializers.SerializerMethodField()

    def get_status(self, value):
        return value.get_status_display()

    class Meta:
        model = Feedback
        exclude = ["assignment", ]
