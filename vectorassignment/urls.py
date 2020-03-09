"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from vectorassignment.api import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^country/$', views.CountryAddView.as_view()),
    url(r'^country/(?P<id>.+)/$', views.CountryAddView.as_view()),
    url(r'^city/$', views.CityAddView.as_view()),
    url(r'^city/(?P<id>.+)/$', views.CityAddView.as_view()),
    url(r'^continent/$', views.ContinentAddView.as_view()),
    url(r'^continent/(?P<id>.+)/$', views.ContinentAddView.as_view())
]
urlpatterns += staticfiles_urlpatterns()
