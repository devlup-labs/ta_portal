from django.contrib import admin

from .models import TeachingAssistantProfile, TeachingAssistantSupervisorProfile, TeachingAssistantCoordinatorProfile, OfficeProfile


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

@admin.register(OfficeProfile)
class OfficeAdmin(admin.ModelAdmin):

    class Meta:
        model = OfficeProfile
        fields = '__all__'
