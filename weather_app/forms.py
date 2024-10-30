from django import forms

class WeatherPreferencesForm(forms.Form):
    show_temperature = forms.BooleanField(required=False, initial=True)
    show_humidity = forms.BooleanField(required=False, initial=True)
    show_wind = forms.BooleanField(required=False, initial=True)
    show_description = forms.BooleanField(required=False, initial=True)