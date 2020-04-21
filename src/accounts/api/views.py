from rest_framework import viewsets, status
from rest_framework.response import Response

from accounts.api.serializers import TeachingAssistantProfileSerializer, UserSerializer, \
    TeachingAssistantCoordinatorProfileSerializer, TeachingAssistantSupervisorProfileSerializer, \
    OfficeProfileSerializer, ChangePasswordSerializer

from accounts.models import TeachingAssistantProfile, TeachingAssistantCoordinatorProfile, \
    TeachingAssistantSupervisorProfile, OfficeProfile
from django.contrib.auth.models import User
from rest_framework.generics import get_object_or_404, UpdateAPIView
from rest_framework.decorators import action
from django.contrib.auth import update_session_auth_hash

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return get_object_or_404(User,
                                 id=self.request.user.id) if self.action == 'current' else super().get_object()

    @action(methods=['get'], detail=False)
    def current(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    @action(methods=['get'], detail=False)
    def profile(self, request, *args, **kwargs):
        ta_profile = TeachingAssistantProfile.objects.filter(user=self.request.user)
        ta_supervisor_profile = TeachingAssistantSupervisorProfile.objects.filter(user=self.request.user)
        ta_coordinator_profile = TeachingAssistantCoordinatorProfile.objects.filter(user=self.request.user)
        office_profile = OfficeProfile.objects.filter(user=self.request.user)
        if ta_profile.exists():
            data = {
                'type': 'ta'
            }
            return Response(data=data, status=status.HTTP_200_OK)
        if ta_supervisor_profile.exists():
            data = {
                'type': 'ta-supervisor'
            }
            return Response(data=data, status=status.HTTP_200_OK)
        if ta_coordinator_profile.exists():
            data = {
                'type': 'ta-coordinator'
            }
            return Response(data=data, status=status.HTTP_200_OK)
        if office_profile.exists():
            data = {
                'type': 'office'
            }
            return Response(data=data, status=status.HTTP_200_OK)
        return Response('', status=status.HTTP_204_NO_CONTENT)


class TeachingAssistantViewSet(viewsets.ModelViewSet):
    serializer_class = TeachingAssistantProfileSerializer
    queryset = TeachingAssistantProfile.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_object(self):
        return get_object_or_404(TeachingAssistantProfile,
                                 user=self.request.user) if self.action == 'current' else super().get_object()

    @action(methods=['get'], detail=False)
    def current(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)


class TeachingAssistantCoordinatorViewSet(viewsets.ModelViewSet):
    serializer_class = TeachingAssistantCoordinatorProfileSerializer
    queryset = TeachingAssistantCoordinatorProfile.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TeachingAssistantSupervisorViewSet(viewsets.ModelViewSet):
    serializer_class = TeachingAssistantSupervisorProfileSerializer
    queryset = TeachingAssistantSupervisorProfile.objects.all()


class OfficeViewSet(viewsets.ModelViewSet):
    serializer_class = OfficeProfileSerializer
    queryset = OfficeProfile.objects.all()


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            update_session_auth_hash(request, self.object)
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
