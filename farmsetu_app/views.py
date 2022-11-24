from django.shortcuts import render
from farmsetu_app.utils import get_weather_data
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class WeatherView(APIView):
    def get(self,request):
        header,data=get_weather_data()
        context={
            'header':header,
            'weather_data':data
        }
        return Response(data=context,status=status.HTTP_200_OK)



# def home(request):
#     header,data=get_weather_data()
#     context={
#         'header':header,
#         'weather_data':data
#     }
#     return render(request, 'home.html', { 'context':context})