from tkinter import *
import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()


master_window  = Tk()
master_window.geometry("400x400")
master_window.resizable(0,0)
master_window.title('Weather App')

city_value = StringVar()

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

def showWeather():
    API_KEY = os.environ.get('API_KEY')
    city_name = city_value.get()
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+API_KEY
    response = requests.get(weather_url)
    #response.delete("1.0", "end")
    weather_info = response.json()
    if weather_info['cod'] == 200:
    
        city = weather_info['name']
        temp = int(weather_info['main']['temp'] - 273) 
        feels_like = int(weather_info['main']['feels_like'] - 273) 
        clouds = weather_info['weather'][0]['description']
        icon = weather_info['weather'][0]['icon']
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        sunrise_time = time_format_for_location(sunrise)
        sunset_time = time_format_for_location(sunset)

        weather = f"\nWeather of: {city}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like}°\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {clouds}%\nIcon: {icon}"

    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!!"



    tfield.insert(INSERT, weather)

city_head= Label(master_window, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10) #to generate label heading
 
inp_city = Entry(master_window, textvariable = city_value,  width = 24, font='Arial 14 bold').pack()
 
 
Button(master_window, command = showWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
weather_now = Label(master_window, text = "The Weather is:", font = 'arial 12 bold').pack(pady=10)
tfield = Text(master_window, width=46, height=10)
tfield.pack()

master_window.mainloop()
