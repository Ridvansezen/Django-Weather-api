import requests
from django.shortcuts import render

def weather(request):
    api_key = 'ec415d880bf53898d7cea4e067bbfc15'
    city = 'Mugla'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    data = response.json()

    temperature = int(data['main']['temp'])
    weather_description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']

    city_name = city

    context = {
        'temperature': temperature,
        'weather_description': weather_description,
        'icon': icon,
        'city_name' : city_name,
    }

    return render(request, 'weather.html', context)
