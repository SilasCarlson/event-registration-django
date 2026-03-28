from django import forms
from .models import Registration


# A ModelForm generates form fields automatically from the Registration model.
# Only 'name' and 'email' are shown and the event is attached in the view, not by the user.
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email']
        widgets = {
            # Placeholder text shown inside the input before the user types.
            'name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
        }
