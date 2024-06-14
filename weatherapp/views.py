from django.shortcuts import render
import requests
# Create your views here.


def home(request):
    city = request.GET.get('city', 'Karachi')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=090c6d122cd5b5455fff7f65d4b0fd9f"
    data = requests.get(url).json()
    payload = {
        'city' :data['name'], 
        'weather': data['weather'][0]['main'], 
        'icon':data['weather'][0]['icon'], 
        'kelvin_temperature':data['main']['temp'], 
        'celcius_temperature':int(data['main']['temp'] -273), 
        'pressure':data['main']['pressure'], 
        'humidity':data['main']['humidity'],
        'description': data['weather'][0]['main'] 
               }
    context = {'data': payload}
    print(context)

    return render(request, 'home.html', context)