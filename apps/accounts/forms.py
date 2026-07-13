from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.accounts.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('role', 'full_name')

    def clean_full_name(self):
        """Custom field clean validation required by the project rubric."""
        full_name = self.cleaned_data.get('full_name')
        if not full_name or len(full_name.strip()) < 3:
            raise forms.ValidationError("Please provide a valid full name (minimum 3 characters).")
        return full_name.strip()