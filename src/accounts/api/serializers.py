from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import TeachingAssistantProfile, TeachingAssistantSupervisorProfile,\
    TeachingAssistantCoordinatorProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


class TeachingAssistantProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachingAssistantProfile
        fields = '__all__'


class TeachingAssistantCoordinatorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachingAssistantCoordinatorProfile
        fields = '__all__'


class TeachingAssistantSupervisorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachingAssistantSupervisorProfile
        fields = '__all__'
