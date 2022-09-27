"""helloworld URL Configuration

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
from helloworldapp.views import foo, foo2, foo3, foo4, foo5, foo6, foo7, foo8, formsearch, formresult

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('helloworld/', foo, name='helloworld'),
    path('helloworld2/', foo2),
    path('helloworld3/<int:name>/', foo3),
    path('helloworld4/<name>/', foo4),
    path('helloworld5/', foo5, name='helloworld5'),
    path('helloworld6/', foo6),
    path('helloworld7/', foo7),
    # SEANCE 3
    path('helloworld8/', foo8),  # datatable
    path('formsearch/', formsearch),
    path('formresult/<str:name>/', formresult),
]
