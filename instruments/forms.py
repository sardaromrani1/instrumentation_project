from django import forms
from .models import Instrument

class InstrumentForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = ['manufacturer', 'model', 'part_number', 'range']