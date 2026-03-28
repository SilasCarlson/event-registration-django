from django.urls import path
from . import views

# URL patterns for the events app.
# These are included by the root urls.py in event_reg/.
urlpatterns = [
    path('', views.event_list, name='event_list'),                     # home page, lists all events
    path('event/<int:pk>/', views.event_detail, name='event_detail'),  # detail page for one event
]
