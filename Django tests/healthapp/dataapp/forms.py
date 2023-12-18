from django import forms
from dataapp.models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['blood_pressure', 'blood_sugar']
