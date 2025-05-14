from django.contrib import admin
from django.urls import path,include
from configapp.urls import *

urlpatterns = [
    path('', include('configapp.urls')),
    path('admin/', admin.site.urls),
    ]
