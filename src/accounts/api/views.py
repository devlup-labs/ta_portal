from rest_framework import viewsets
from accounts.api.serializers import TeachingAssistantProfileSerializer, UserSerializer, \
    TeachingAssistantCoordinatorProfileSerializer, TeachingAssistantSupervisorProfileSerializer

from accounts.models import TeachingAssistantProfile, TeachingAssistantCoordinatorProfile ,TeachingAssistantSupervisorProfile
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeachingAssistantViewSet(viewsets.ModelViewSet):
    serializer_class = TeachingAssistantProfileSerializer
    queryset = TeachingAssistantProfile.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AuthenticationCheckAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        authenticated = request.user.is_authenticated
        data = {
            'message': 'Authorized' if authenticated else 'Unauthorized'
        }
        status_code = status.HTTP_200_OK if authenticated else status.HTTP_401_UNAUTHORIZED
        return Response(data, status=status_code)


class TeachingAssistantCoordinatorViewSet(viewsets.ModelViewSet):
    serializer_class = TeachingAssistantCoordinatorProfileSerializer
    queryset = TeachingAssistantCoordinatorProfile.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class TeachingAssistantSupervisorViewSet(viewsets.ModelViewSet):
    serializer_class = TeachingAssistantSupervisorProfileSerializer
    queryset = TeachingAssistantSupervisorProfile.objects.all()