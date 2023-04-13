"""FOLLYJAY URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('pages.urls')),
    path('meat_vegetable/',include('meat_vegetable.urls')),
    path('tuber/',include('tuber.urls')),
    path('species_oil/',include('species_oil.urls')),
    path('grain_flour/',include('grain_flour.urls')),
    path('drinks/', include('drinks.urls')),
    path('confectioneries/', include('confectioneries.urls')),
    path('untensils/',include('untensils.urls')),
    path('beauty_health/',include('beauty_health.urls')),
    path('private/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
