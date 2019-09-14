from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import TeachingAssistantProfile, TeachingAssistantCoordinatorProfile


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