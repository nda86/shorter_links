from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from shortener.views import UrlHandler


urlpatterns = [
    path('admin/', admin.site.urls),
    path('links/', include('shortener.urls'))
]
