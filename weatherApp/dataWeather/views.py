import requests
from django.shortcuts import render

def weather(request):
    api_key = 'ec415d880bf53898d7cea4e067bbfc15'
    city = 'Mugla'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    data = response.json()
    response_data = response.json()  # API yanıtını alıyoruz
    print(response_data)

    if response.status_code == 200:
        temperature = int(response_data['main']['temp'])
        weather_description = response_data['weather'][0]['description']
        icon = response_data['weather'][0]['icon']

        city_name = city

        context = {
            'temperature': temperature,
            'weather_description': weather_description,
            'icon': icon,   
            'city_name': city_name,
        }

    temperature = int(response_data.get('main', {}).get('temp'))
    weather_description = response_data.get('weather', [])[0].get('description')
    weather_conditions = response_data.get('weather', [])
    if len(weather_conditions) > 0:
        weather_description = weather_conditions[0].get('description')
    icon = data['weather'][0]['icon']

    context = {
        'temperature': temperature,
        'weather_description': weather_description,
        'icon': icon,
        'city_name': city_name,
    }

    return render(request, 'weather.html', context)



