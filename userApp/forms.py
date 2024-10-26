from django import forms
from .models import Participant

class ParticipantCreationForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['username', 'email', 'first_name', 'last_name', 'cin', 'password','participant_category']  # Ajoute les champs nécessaires

    def save(self, commit=True):
        user = super().save(commit=False)
        print(user)
        user.set_password(self.cleaned_data['password'])  # Hash le mot de passe
        if commit:
            user.save()
        return user