"""telemedycyna URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from myapp.views import *
from telemedycyna import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^$', home, name = 'base.html'),
    url(r'^drugs/$', lek, name = 'drugs.html'),
    url(r'^doctor/$', doktor, name = 'doctor.html'),
    url(r'^calculate/$', main_drug, name = 'calculate.html'),
]
