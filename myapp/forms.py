from django import forms
from .models import dates

class DatesForm(forms.ModelForm):
    class Meta:
        model = dates
        fields = ['date']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

class NextDateForm(forms.ModelForm):
    class Meta:
        model = dates
        fields = ['date']  # Assuming 'date' is the field name in your model
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

class LastDateForm(forms.ModelForm):
    class Meta:
        model = dates
        fields = ['date']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

class UpdateBothDatesForm(forms.Form):
    first_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))
    second_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))