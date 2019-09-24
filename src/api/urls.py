from django.urls import path, include

from api.views import AuthenticationCheckAPIView, LoginAPIView, LogoutAPIView, CsrfTokenAPIView

app_name = 'api'

urlpatterns = [
    path('token/', CsrfTokenAPIView.as_view(), name='token'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('accounts/', include('accounts.api.urls')),
    path('core/', include('core.api.urls')),
    path('auth-check/', AuthenticationCheckAPIView.as_view(), name='auth-check')
]
