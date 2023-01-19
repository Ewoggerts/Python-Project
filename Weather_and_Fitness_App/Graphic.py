from distutils.command.build_scripts import first_line_re
from modulefinder import packagePathMap
from tkinter import *
from time import strftime
import data
import functions
from configparser import ConfigParser

app = Tk()
app.title("Weather app")
app.geometry('900x750')

def complexWeather(user_zip,user_country):
    WindDirection="Wind Direction: "+str(data.getWind_dir(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country)))
    Sunrise="Sunrise Time: "+str(functions.UnixConverter(data.getSunrise(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country))))
    Sunset="Sunset Time: "+str(functions.UnixConverter(data.getSunset(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country))))
    HeatIdx=functions.tempSafety(functions.calcHeatIndex(data.getTemp(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country)),data.getHumidity(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country))))
    WindEff=functions.windEffect(data.getWind_spd(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country)))
    WindDir=functions.compass(data.getWind_dir(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country)))
    Pace=functions.paceChangeHeat(functions.dewpoint(data.getTemp(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country)),data.getHumidity(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country))))
    PaceC=functions.paceChangeCold(data.getTemp(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country)))
    final=(WindDirection,Sunrise,Sunset,HeatIdx,WindEff,WindDir,Pace,PaceC)
    return final
def weatherEZ(user_zip,user_country):
    weather="Weather: "+data.getWeather(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country))
    Temp="Temp: "+str(data.getTemp(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country)))
    Humidity="Humidity: "+str(data.getHumidity(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country)))
    hIdx="Heat Index: "+str(functions.calcHeatIndex(data.getTemp(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country)),data.getHumidity(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country))))
    WindSpeed="Wind Speed: "+str(data.getWind_spd(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country)))
    final=(weather,Temp,Humidity,hIdx,WindSpeed)
    return final

def searchWeather():
    user_city=city_text.get()
    user_state=state_text.get()
    user_zip=zip_num.get()
    user_country=country_text.get()
    first=weatherEZ(user_zip,user_country)
    second=complexWeather(user_zip,user_country)
    location['text']=user_city
    weather['text']=first[0]
    Temp['text']=first[1]
    Humidity['text']=first[2]
    hIdx['text']=first[3]
    WindSpeed['text']=first[4]
    WindDirection['text']=second[0]
    Sunrise['text']=second[1]
    Sunset['text']=second[2]
    heatIdx_lbl['text']=second[3]
    windEff_lbl['text']=second[4]
    windDir_lbl['text']=second[5]
    pace_lbl['text']=second[6]
    paceC_lbl['text']=second[7]

def resetSearch():
    location.config(text=" ")
    weather.config(text=" ")
    Temp.config(text=" ")
    Humidity.config(text=" ")
    hIdx.config(text=" ")
    WindSpeed.config(text=" ")
    WindDirection.config(text=" ")
    Sunrise.config(text=" ")
    Sunset.config(text=" ")
    heatIdx_lbl.config(text=" ")
    windEff_lbl.config(text=" ")
    windDir_lbl.config(text=" ")
    pace_lbl.config(text=" ")
    paceC_lbl.config(text=" ")

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

lbl = Label(app, font = ('calibri', 18, 'bold'),background = 'purple',foreground = 'white') 
lbl.pack(side=BOTTOM)
time()

city_label = Label(app, text = "Enter City :")
city_label.pack()
city_text = StringVar()
city_entry= Entry(app, textvariable=city_text)
city_entry.pack()

state_label = Label(app, text = "Enter State :")
state_label.pack()
state_text = StringVar()
state_entry= Entry(app, textvariable=state_text)
state_entry.pack()

zip_label = Label(app, text = "Enter Zip :")
zip_label.pack()
zip_num = IntVar()
zip_num = Entry(app, textvariable=zip_num)
zip_num.pack()

country_label = Label(app, text = "Enter Country :")
country_label.pack()
country_text = StringVar()
country_entry= Entry(app, textvariable=country_text)
country_entry.pack()

search_btn = Button(app, text='Search Weather', width=16, command=searchWeather)
search_btn.pack()

reset_btn= Button(app, text='Reset Search',width=16,command=resetSearch)
reset_btn.pack()

location=Label(app,text='')
location.pack()
weather=Label(app, text='')
weather.pack()
Temp=Label(app, text='')
Temp.pack()
Humidity=Label(app, text='')
Humidity.pack()
hIdx=Label(app, text='')
hIdx.pack()
WindSpeed=Label(app, text='')
WindSpeed.pack()
WindDirection=Label(app, text='')
WindDirection.pack()
Sunrise=Label(app, text='')
Sunrise.pack()
Sunset=Label(app, text='')
Sunset.pack()
heatIdx_lbl=Label(app, text='')
heatIdx_lbl.pack()
windEff_lbl=Label(app, text='')
windEff_lbl.pack()
windDir_lbl=Label(app, text='')
windDir_lbl.pack()
pace_lbl=Label(app, text='')
pace_lbl.pack()
paceC_lbl=Label(app, text='')
paceC_lbl.pack()

print(weatherEZ(11209,'us'))
app.mainloop()