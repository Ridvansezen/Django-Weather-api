# weather/views.py

from django.shortcuts import render
from .tasks import fetch_weather_data_async

def weather(request):
    error_message = None
    city = request.POST.get('city', '')

    if city:
        result = fetch_weather_data_async.delay(city)  # Asenkron görevi başlat
        context = result.get()  # Görev tamamlandığında sonucu al

        if isinstance(context, dict):
            return render(request, 'weather.html', context)
        else:
            error_message = context
    else:
        error_message = "Lütfen bir şehir adı girin."

    return render(request, 'weather.html', {'error_message': error_message})

turkish_translations = {
    "broken clouds": "parçalı bulutlu",
    "clear sky": "açık hava",
    "overcast clouds" : "çok bulutlu",
    "few clouds":"az bulutlu",
    "scattered clouds": "bulutlu"
    # Diğer hava durumu çevirilerini buraya ekleyin
}
