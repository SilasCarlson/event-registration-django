from django.db import models


# An Event is one entry in the database representing something users can sign up for.
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)  # optional
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField(default=50)  # max number of registrants

    def spots_left(self):
        # Count existing registrations and subtract from capacity.
        # 'registrations' refers to the related_name on the Registration model below.
        return self.capacity - self.registrations.count()

    def is_full(self):
        # Used in templates to disable the registration form when capacity is reached.
        return self.spots_left() <= 0

    def __str__(self):
        # Shown in the admin panel and anywhere the object is printed.
        return self.name


# A Registration links one person (by name and email) to one Event.
class Registration(models.Model):
    # If the event is deleted, all its registrations are deleted too (CASCADE).
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    registered_at = models.DateTimeField(auto_now_add=True)  # set automatically on creation

    class Meta:
        # Prevents the same email from registering for the same event twice.
        unique_together = ('event', 'email')

    def __str__(self):
        return f"{self.name} -> {self.event.name}"
