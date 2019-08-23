from django.contrib import admin
from .models import TeachingAssistantProfile, TeachingAssistantSupervisorProfile, TeachingAssistantCoordinatorProfile


@admin.register(TeachingAssistantProfile)
class TeachingAssistantAdmin(admin.ModelAdmin):

    class Meta:
        model = TeachingAssistantProfile
        fields = '__all__'


@admin.register(TeachingAssistantSupervisorProfile)
class TeachingAssistantSupervisorAdmin(admin.ModelAdmin):

    class Meta:
        model = TeachingAssistantSupervisorProfile
        fields = '__all__'


@admin.register(TeachingAssistantCoordinatorProfile)
class TeachingAssistantCoordinatorAdmin(admin.ModelAdmin):

    class Meta:
        model = TeachingAssistantCoordinatorProfile
        fields = '__all__'
