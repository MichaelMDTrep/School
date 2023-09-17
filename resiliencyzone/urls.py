"""resiliencyzone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django_serverless_cron import urls as django_serverless_cron_urls
from exception import handler404, handler500, handler400, handler403

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('curriculum/', include('curriculum.urls')),
    path('users/', include('userdata.urls')),
    path('contact/', include('contact.urls')),
    path('invite/', include('invites.urls')),
    re_path(r'^', include(django_serverless_cron_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
