"""ta_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.auth.views import LogoutView

from ta_portal.views import VueView

urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    path('logout/', LogoutView.as_view(next_page='/login'), name='logout'),
    path('admin/', admin.site.urls),
    path('api/', include("api.urls"))
]

urlpatterns += [
    re_path(r'.*', VueView.as_view(), name='vue-js')    # Catch all URL to send all urls to VueJS
]
