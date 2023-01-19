from .models import HH
from django.forms import ModelForm, DateTimeInput


class HHForm(ModelForm):
    class Meta:
        model = HH
        fields = ["date"]
        widgets = {
            "date": DateTimeInput(attrs={
                'class': 'form-control custom-date-control',
                'id': 'date_day',
                'type': 'date'
            })
        }