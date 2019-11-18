"""Houston URL Configuration

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
from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import admin
from django.views.generic import TemplateView

from Houston import views

urlpatterns = [
    url(r'^record-view$', views.record_page_view, name='record-page-view'),
    url(r'^view-counts$', views.view_counts, name='view-counts'),
    url(r'^dashboard$',
        staff_member_required(
            TemplateView.as_view(template_name='Houston/dashboard.html')),
        name='dashboard'),
]
