import requests, json
import datetime
api_key = "Enter Api Key"
base_url = "https://api.openweathermap.org/data/2.5/weather?q="
city = input("Enter city Name : ")
complete_Url= base_url + city  + "&appid="  + api_key
response =requests.get(complete_Url)
data_formate  = response.json()
kelvin = data_formate["main"]["temp"]
Celsius = (kelvin - 273.15 ) 
humidity = data_formate["main"]["humidity"]
vist = data_formate["visibility"]
dist = data_formate["weather"][0]["description"]

print(f"The current weather Report the tempearture is {Celsius }celsius, humidity is {humidity} visibility is {vist}  and the  \n{dist} ")