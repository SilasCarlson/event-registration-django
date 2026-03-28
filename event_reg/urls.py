from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),       # built-in Django admin panel
    path('', include('events.urls')),      # hand off all other URLs to the events app
]
