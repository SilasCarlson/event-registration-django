from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Event
from .forms import RegistrationForm


# Shows a list of all events ordered by date (soonest first).
def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'events/event_list.html', {'events': events})


# Shows a single event and handles the registration form submission.
def event_detail(request, pk):
    # 404 if the event does not exist.
    event = get_object_or_404(Event, pk=pk)
    form = RegistrationForm()

    # For when the form is submitted
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if event.is_full():
                messages.error(request, 'Sorry, this event is full.')
            else:
                # Attach the event to the registration before saving.
                registration = form.save(commit=False)
                registration.event = event
                try:
                    registration.save()
                    messages.success(request, f"You're registered for {event.name}!")
                    # Redirect back to the same page to prevent form resubmission on refresh.
                    return redirect('event_detail', pk=pk)
                except Exception:
                    # unique_together on the model will raise an error for duplicate emails.
                    messages.error(request, 'You are already registered for this event.')

    return render(request, 'events/event_detail.html', {'event': event, 'form': form})
