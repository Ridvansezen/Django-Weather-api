# tasks.py

from celery import shared_task
import requests

@shared_task
def fetch_weather_data_async(city):
    api_key = 'ec415d880bf53898d7cea4e067bbfc15'

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperature = int(data['main']['temp'])
        weather_description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']

        city_name = city

        context = {
            'temperature': temperature,
            'weather_description': weather_description,
            'icon': icon,
            'city_name': city_name,
        }

        return context
    else:
        return None  # Eğer veri çekilemezse None döndür

@shared_task
def fetch_weather_bulk(cities):
    weather_data = []
    for city in cities:
        data = fetch_weather_data_async(city)
        if data:
            weather_data.append(data)
    return weather_data
