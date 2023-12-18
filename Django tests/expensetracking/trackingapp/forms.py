from django import forms
from django.contrib.admin.widgets import AdminTimeWidget
from trackingapp.models import Expense


class ExpenseForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)
    description = forms.CharField(
        label='description',
        widget=forms.Textarea(attrs={'placeholder': 'describe your expense in a few words'})
    )

    class Meta:
        model = Expense
        fields = ['date', 'time', 'category', 'amount', 'description']
