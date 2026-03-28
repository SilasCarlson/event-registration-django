from django.contrib import admin
from .models import Event, Registration


# Registering models here makes them visible and editable in the Django admin panel.
# Visit /admin/ after creating a superuser to add and manage events.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # Columns shown in the event list view inside the admin panel.
    list_display = ['name', 'date', 'location', 'capacity', 'spots_left']

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'event', 'registered_at']
