from django.shortcuts import get_object_or_404, redirect, render
from decouple import config
import requests
from pprint import pprint
from django.contrib import messages

from weatherapp.models import City


def home(request):
    API_key = config('API_KEY')
    u_city = request.GET.get('name')  #cityName model den geldi
    # print(u_city)
    if u_city:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={u_city}&appid={API_key}&units=metric&'
        response = requests.get(url)
        if response.ok:  # 400 ün altında true olarak döner
            cityInfo = response.json()  # python dict e döndürmek için
            r_city = cityInfo['name']   # cityInfo içindeki  name api denn geldi 
            if City.objects.filter(name=r_city):
                messages.warning(request, 'city already existts!')
            else:
                City.objects.create(name=r_city)
                messages.success(request, 'city addded')
        else:
            messages.error(request, 'There is no city')

        return redirect('home')
    # pprint(cityInfo)

    # pprint(cityInfo['name'])
    # pprint(cityInfo['main']['temp'])
    # pprint(cityInfo['weather'][0]['description'])
    # pprint(cityInfo['weather'][0]['icon'])



    #! db den çekip frontend e gönderme kısmı aşağısı
    all_city_data = []
    cities = City.objects.all() # db deki tüm şehirleri çek

    for each_city in cities:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={each_city}&appid={API_key}&units=metric&' # db deki bütün cityleri döngüye aldık
        response = requests.get(url)
        cityInfo = response.json()
        data = {
            # 'city' : cityInfo['name'],
            'city' : each_city,
            'temp' : cityInfo['main']['temp'],
            'desc' : cityInfo['weather'][0]['description'],
            'icon' : cityInfo['weather'][0]['icon']
        }
        all_city_data.append(data)
        # pprint(all_city_data)
    
    context = {
        'all_city_data':all_city_data,
    }
    return render(request, 'weatherapp/home.html',context)

def delete_city(request,id):
    city = get_object_or_404(City,id=id)
    city.delete()
    messages.success(request, 'city deleted')
    return redirect('home')