from django.urls import path, include

from api.views import AuthenticationCheckAPIView

app_name = 'api'

urlpatterns = [
    path('accounts/', include('accounts.api.urls')),
    path('core/', include('core.api.urls')),
    path('auth-check/', AuthenticationCheckAPIView.as_view(), name='auth-check')
]
