from tkinter import *
import requests, json
from PIL import ImageTk, Image
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

#window
master = Tk()
master.title("Weather App")
master.geometry("400x400")
master.resizable(0, 0)


def timestamp(timestamp):
    local_time = datetime.utcfromtimestamp(timestamp)
    return local_time

city_name = StringVar()

def show_weather():
    API_KEY = os.environ.get('API_KEY')
    city = city_name.get()
    weather_url = requests.get('https://api.openweathermap.org/data/2.5/forecast?q=' + city + '&appid=' + API_KEY + '&units=metric')
    weather_info = weather_url.json()
    tfield.delete("1.0", "end")
    if weather_info['cod'] == 200:
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
    
    else:

        weather = f"\n\tWeather for '{city}' not found!\n\tKindly Enter valid City Name!"   
    
    tfield.insert(INSERT, weather)
bg = ImageTk.PhotoImage(Image.open("weatherImage.png"))
label = Label(master, image=bg)
label.place(x = 0,y = 0)

label2 = Label(master, text = "Enter City Name", background='white',
               font= 'Arial 12 bold').pack(pady = 10)
cityNameEntry = Entry(master, textvariable=city_name, width=24, font='Arial 14 bold').pack()
Button(master, command = show_weather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20) 
tfield = Text(master, width=46, height=10)
tfield.pack()   

master.mainloop()