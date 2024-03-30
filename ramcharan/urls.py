"""
URL configuration for ramcharan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from chirutha.views import * 
from orange.views import *
from gamechanger.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chirutha/',chirutha,name='chirutha'),
    path('orange/',orange,name='orange'),
    path('gamechanger/',gamechanger,name='gamechanager'),
    path('chirutha_s/',chirutha_s,name='chirutha_s')
    

]
