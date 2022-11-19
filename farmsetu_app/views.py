from django.shortcuts import render
import requests
import json
import urllib.request as ur
# 5bae36be-dfe7-4884-9ec1-dfc584fe64c7

def get_weather_data_by_id(id):
    api_string=f"http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/{id}?res=3hourly&key=5bae36be-dfe7-4884-9ec1-dfc584fe64c7"
    api_response=requests.get(api_string)
    city_data=api_response.json()
    # city_param=city_data.get('SiteRep').get('Wx')
    city_data=city_data.get('SiteRep').get('DV').get('Location').get('Period')[0]
    rep_data=city_data.get('Rep')[0]
    temperature=rep_data.get('T')
    wind_speed=rep_data.get('S')
    weather_type=rep_data.get('W')
    weather_data={"temperature":temperature,"wind_speed":wind_speed,"weather_type":weather_type}
    # print(weather_data)
    return weather_data


def home(request):
    weather_req=requests.get("http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/sitelist?key=5bae36be-dfe7-4884-9ec1-dfc584fe64c7")
    # weather_req=ur.urlopen("http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/3840?res=3hourly&key=5bae36be-dfe7-4884-9ec1-dfc584fe64c7")
    # response = urllib3.request.urlopen('http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/**YourLocationID**?res=3hourly&key=**your_api_key**')
    # FCData = weather_req.read()
    # print(FCDataStr)
    # FCData_Dic  = json.loads(weather_req)
    # FCData_Dic  = weather_req.json()
    weather_data=[]
    if weather_req:
        api_data=weather_req.json()
        u=api_data.get('Locations').get('Location')
        cities={}
        count=0
        for location in u:
            id=location.get('id')
            name=location.get('name')
            cities[id]=name
            count+=1
            if count==10:
                break
        for id,name in cities.items():
            city_weather_data=get_weather_data_by_id(id)
            city_weather_data['name']=name
            weather_data.append(city_weather_data)
    else:
        api_data={} 
    # print(cities)   
    return render(request, 'home.html', { 'weather':weather_data})