import requests, json
import datetime
api_key = "516e5492d88e639900a36168fff7d4e6"
base_url = "https://api.openweathermap.org/data/2.5/weather?q="
city = input("Enter city Name : ")
complete_Url= base_url + city  + "&appid="  + api_key
response =requests.get(complete_Url)
data_formate  = response.json()
kelvin = data_formate["main"]["temp"]
Celsius = (kelvin - 273.15 ) 
wind_speed = data_formate["wind"]["speed"]
humidity = data_formate["main"]["humidity"]
vist = data_formate["visibility"]
clouds=data_formate["clouds"]["all"]
dist = data_formate["weather"][0]["description"]

print(f"The current weather Report the tempearture is {Celsius }celsius, humidity is {humidity} visibility is {vist}  and the  {dist} and the speed is {round(wind_speed*5)} km/h  cloud is {clouds} ")  