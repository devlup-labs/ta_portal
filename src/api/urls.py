from django.urls import path, include

from api.views import AuthenticationCheckAPIView

app_name = 'api'

urlpatterns = [
    path("auth/", include("rest_framework.urls")),
    path('accounts/', include('accounts.api.urls')),
    path('auth-check/', AuthenticationCheckAPIView.as_view(), name='auth-check')
]
