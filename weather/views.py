from django.shortcuts import render
import requests
import pprint

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city'].title()
        if city != '':
            response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_ID}')
            response.raise_for_status()
            weather_data = response.json()
            data = {
                'country_code': str(weather_data['sys']['country']),
                'coordinate': str(weather_data['coord']['lon']) + ' ' + str(weather_data['coord']['lat']),
                'temp': str(weather_data['main']['temp']),
                'pressure': str(weather_data['main']['pressure']),
                'humidity': str(weather_data['main']['humidity']),
                }
            
            return render(request, 'index.html', {'city':city, 'data':data})
    else:
        city = ''
    return render(request, 'index.html', {'city':city})