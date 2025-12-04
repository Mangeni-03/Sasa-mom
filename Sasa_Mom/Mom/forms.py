from django import forms
from .models import Mother

class MotherRegistrationForm(forms.ModelForm):
    class Meta:
        model = Mother
        fields = ['name', 'phone', 'language', 'consent', 'hospital']

def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Lightweight validation — adapt to your country rules
        if not phone or len(phone) < 6:
            raise forms.ValidationError('Enter a valid phone number')
        return phone