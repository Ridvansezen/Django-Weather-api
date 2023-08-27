import requests
from django.shortcuts import render

def weather(request):
    error_message = None
    api_key = 'ec415d880bf53898d7cea4e067bbfc15'
    city = request.POST.get('city', '')

    if city:
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

            turkish_translations = {
                "broken clouds": "parçalı bulutlu",
                "clear sky": "açık hava",
                "overcast clouds" : "çok bulutlu",
                "few clouds":"az bulutlu",
                "scattered clouds": "bulutlu"
                # Diğer hava durumu çevirilerini buraya ekleyin
            }
            if weather_description in turkish_translations:
                context['weather_description'] = turkish_translations[weather_description]

            return render(request, 'weather.html', context)
        else:
            error_message = "Belirtilen şehir bulunamadı."
    else:
        error_message = "Lütfen bir şehir adı girin."

    return render(request, 'weather.html', {'error_message': error_message})
