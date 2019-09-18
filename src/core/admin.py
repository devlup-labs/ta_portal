from django.contrib import admin

from .models import Course, Feedback, Assignment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    class Meta:
        model = Course
        fields = '__all__'


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    class Meta:
        model = Assignment
        fields = '__all__'


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    class Meta:
        model = Feedback
        fields = '__all__'
