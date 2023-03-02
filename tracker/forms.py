from django import forms
from django.forms import fields, Textarea, TextInput
from .models import TrackerFilter

class FilterForm(forms.Form):
    CHOICES = [(1, "Data Kumulatif"), (2, "Data Harian")]
    chart_type = forms.IntegerField(label="Dataset", widget=forms.RadioSelect(choices=CHOICES))
    number_of_data = forms.IntegerField(label="Jumlah Hari", min_value=7, max_value=30)