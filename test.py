import requests, json
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

def timestamp(timestamp):
    local_time = datetime.utcfromtimestamp(timestamp)
    return local_time

def show_weather():
    API_KEY = os.environ.get('API_KEY')
    city = input('city ')
    weather_url = requests.get('https://api.openweathermap.org/data/2.5/forecast?q=' + city + '&appid=' + API_KEY + '&units=metric')

    weather_info = weather_url.json()
    http_status = weather_info['cod']
    print(http_status)
 
    if http_status == 200:
        city_value =  weather_info['city']['name']
        feels_like = weather_info['list'][0]['main']['feels_like']
        max_temp = weather_info['list'][0]['main']['feels_like']
        min_temp = weather_info['list'][0]['main']['feels_like']
        clouds = weather_info['list'][0]['weather'][0]['description']
        precipitation = weather_info['list'][0]['pop']
        sunrise = timestamp(weather_info['city']['sunrise'])
        sunset = timestamp(weather_info['city']['sunset'])
        timezone = timestamp(weather_info[city]['timezone']).time()
        
        weather = f"\nCity Name: {city_value}\nFeels Like: {feels_like} °C\nMin Temp:  {min_temp } °C\nMax Temp:  {max_temp } °C\nPrecipitation: {precipitation}%\nClouds: {clouds}\nSunrise: {sunrise}\nSunset: {sunset}\nTimezone: {timezone} GMT" 
        return (1)
    else:
        weather = f"\n\tWeather for '{city}' not found!\n\tKindly Enter valid City Name!"  
        return 0
    
 
  
 

  

print(show_weather())