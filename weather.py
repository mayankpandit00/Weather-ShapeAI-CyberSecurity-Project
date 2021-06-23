import requests
from datetime import datetime
import sys

api_key = '574276225b8b0d801e92e35cf4e5a7ea'
location = input("Enter the city name: ")
file_name = location+'.txt'

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

city_temp = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
humidty = api_data['main']['humidity']
wind_speed = api_data['wind']['speed']
min_temp = ((api_data['main']['temp_min']) - 273.15)
max_temp = ((api_data['main']['temp_max']) - 273.15)
date_time = datetime.now().strftime("%d %b %Y  ||  %I:%M:%S %p")

print("-------------------------------------------------------------")
print("Weather Stats for :  {}  ||  {}".format(location.upper(), date_time))
print("-------------------------------------------------------------")
print("Current Temperature                   : {:.2f}° C".format(city_temp))
print("Current Weather Description           :", weather_desc)
print("Current Humidity                      :", humidty, '%')
print("Current Wind Speed                    :", wind_speed, 'kmph')
print("Today's Minimum Temperature           : {:.2f}° C".format(min_temp))
print("Today's Maximum Temperature           : {:.2f}° C".format(max_temp))

print("\n=============================================================")
print("Data saved successfully as: " + file_name)

with open(file_name, 'w') as file:
    sys.stdout = file

    print("-------------------------------------------------------------")
    print("Weather Stats for :  {}  ||  {}".format(location.upper(), date_time))
    print("-------------------------------------------------------------")
    print("Current Temperature                   : {:.2f}° C".format(city_temp))
    print("Current Weather Description           :", weather_desc)
    print("Current Humidity                      :", humidty, '%')
    print("Current Wind Speed                    :", wind_speed, 'kmph')
    print("Today's Minimum Temperature           : {:.2f}° C".format(min_temp))
    print("Today's Maximum Temperature           : {:.2f}° C".format(max_temp))

    file.close()