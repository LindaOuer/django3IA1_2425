from django import forms
from .models import Conference

class ConferenceModelForm(forms.ModelForm):
    class Meta:
        model=Conference
        fields = '__all__'
    start_date=forms.DateField(
        label="Conference Start Date",
        widget=forms.DateInput(
            attrs={
                'type' : 'date',
                'class' :'form-control date-input'
            }
        ))
    end_date=forms.DateField(
        label="Conference End Date",
        widget=forms.DateInput(
            attrs={
                'type' : 'date',
                'class' :'form-control date-input'
            }
        ))