from django.shortcuts import render
from farmsetu_app.utils import get_weather_data


def home(request):
    header,data=get_weather_data()
    context={
        'header':header,
        'weather_data':data
    }
    return render(request, 'home.html', { 'context':context})