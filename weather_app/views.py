from django.shortcuts import render
from .forms import WeatherPreferencesForm
from .weather_service import get_location_from_ip, get_weather_data

def index(request):
    location = get_location_from_ip()
    weather_data = get_weather_data(location['latitude'], location['longitude'])
    
    form = WeatherPreferencesForm(request.POST or None)
    
    context = {
        'weather': weather_data,
        'location': location,
        'form': form
    }
    return render(request, 'weather_app/index.html', context)
