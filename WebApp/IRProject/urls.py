"""IRProject URL Configuration

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
from django.urls import path
from IRWebApp.views import keywords_party, similarities_members, keywords_member, search_speeches, quick_search_speeches, home

urlpatterns = [
    path('', home, name = 'home'),
    path("admin/", admin.site.urls),
    path('keywords_party/', keywords_party, name='my-view'),
    path('similarities/', similarities_members, name = 'similarities_members'),
    path('keywords_member/', keywords_member, name = 'keywords_member'),
    path('search/', search_speeches, name = 'search'),
    path('quicksearch/', quick_search_speeches, name = 'quicksearch')
]