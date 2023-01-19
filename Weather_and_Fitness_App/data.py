#Open weather API account info
#Username:testCase
#Email: ecwong636@gmail.com
#Password: LmGBrain%7
#API Key:83de7d4de2ee846880d190a66a5bda0e
#Distance 5k only

import requests
from requests.structures import CaseInsensitiveDict
api_key1 = '83de7d4de2ee846880d190a66a5bda0e'
limit=2

#Set the variables with useful data
#print("Please enter location data")
#user_city = input("Enter city: ")
#user_state = input("Enter state code aka NY, NJ, CT : ")
#user_zip = input("Enter zip code: ")
#user_country = input("Enter your country code: ").upper()
#print("In order to calculate your percieved outdoor exercise intensity we require some user data.")
#user_sec = input("How many additional seconds does it take to run 1 mile?: ")
##user_comfort = input("Do you prefer running in -20,-10,0,10,20,30,40,50,60,70,80,90,100,110 degree weather?:")
user_city = "Brooklyn"
user_state = "NY"
user_zip = 11217
user_country = "US"
#Functions to get data
def getUser_city(user_city):
    return user_city
def getUser_state(user_state):
    return user_state
def getUser_zip(user_zip):
    return user_zip
def getUser_country(user_country):
    return user_country
def getLocation_data(user_zip,user_country):
    location_data = requests.get(f"http://api.openweathermap.org/geo/1.0/zip?zip={user_zip},{user_country}&appid={api_key1}")
    return location_data.json()
def getLocation_lat(user_zip,user_country):
    location_data = requests.get(f"http://api.openweathermap.org/geo/1.0/zip?zip={user_zip},{user_country}&appid={api_key1}")
    location_lat = location_data.json()['lat']
    return location_lat
def getLocation_lon(user_zip,user_country):
    location_data = requests.get(f"http://api.openweathermap.org/geo/1.0/zip?zip={user_zip},{user_country}&appid={api_key1}")
    location_lon = location_data.json()['lon']
    return location_lon
def getWeather_data(location_lat,location_lon):
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={location_lat}&lon={location_lon}&units=imperial&appid={api_key1}")
    return weather_data.json()
def getWeather(location_lat,location_lon):
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={location_lat}&lon={location_lon}&units=imperial&appid={api_key1}")
    weather = weather_data.json()['weather'][0]['main'] 
    return weather
def getTemp(location_lat,location_lon):
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={location_lat}&lon={location_lon}&units=imperial&appid={api_key1}")
    temp = weather_data.json()['main']['temp']
    return temp
def getHumidity(location_lat,location_lon):
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={location_lat}&lon={location_lon}&units=imperial&appid={api_key1}")
    humidity = weather_data.json()['main']['humidity']
    return humidity
def getWind_spd(location_lat,location_lon):
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={location_lat}&lon={location_lon}&units=imperial&appid={api_key1}")
    wind_spd = weather_data.json()['wind']['speed']
    return wind_spd
def getWind_dir(location_lat,location_lon):
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={location_lat}&lon={location_lon}&units=imperial&appid={api_key1}")
    wind_dir = weather_data.json()['wind']['deg']
    return wind_dir
def getSunrise(location_lat,location_lon):
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={location_lat}&lon={location_lon}&units=imperial&appid={api_key1}")
    sunrise = weather_data.json()['sys']['sunrise']
    return sunrise
def getSunset(location_lat,location_lon):
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={location_lat}&lon={location_lon}&units=imperial&appid={api_key1}")
    sunset = weather_data.json()['sys']['sunset']
    return sunset
def getIcon(location_lat,location_lon):
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={location_lat}&lon={location_lon}&units=imperial&appid={api_key1}")
    icon = weather_data.json()['weather'][0]['icon']
    return icon
#test cases

