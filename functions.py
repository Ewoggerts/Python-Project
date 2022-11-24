import data
import math
import datetime
def change_location():
    user_city = input("Enter city: ")
    user_state = input("Enter state: ")
    user_zip = input("Enter zip code: ")
    user_country = input("Enter your country code: ")

def calcHeatIndex(T,RH):
    HI=HI=-42.379 + 2.04901523*T + 10.14333127*RH - .22475541*T*RH - .00683783*T*T - .05481717*RH*RH + .00122874*T*T*RH + .00085282*T*RH*RH - .00000199*T*T*RH*RH
    if T<80:
        HI = 0.5 * (T + 61.0 + ((T-68.0)*1.2) + (RH*0.094))
    elif (T>=80 and T<=112) and (RH < 13):
        HI=HI-((13-RH)/4)*(math.sqrt((17-abs(T-95.))/17))
    elif (T>=80 and T<=85) and (RH > 85):
        HI=((RH-85)/10) * ((87-T)/5)
    return int(HI)
#USE
def tempSafety(index):
    if index<80:
        return "Safe to exercise outdoors."
    elif index>=80 and index<91:
        return "According to the National Weather Service take caution in this heat."
    elif index>=91 and index<103:
        return "According to the National Weather Service take extreme caution in this heat."
    elif index>=103 and index<126:
        return "According to the National Weather Service there is danger running in this heat."
    else:
        return "There is extreme danger according to the National Weather Service. DO NOT RUN IN THIS HEAT."

def compass(degree):
    dir=["Northeast","East","Southeast","South","Southwest","West","Northwest","North"]
    const=[45,90,135,180,225,270,315,360]
    total=[]
    index=0
    for each in const:
        ret=abs(each-degree)
        total.append(ret)
    min=total[0]
    for num, each in enumerate(total):
        if each<min:
            min=each
            index=num
    return "If you run "+dir[index]+" you will deal with the wind first, and have a tailwind on the way back (vice versa). Other directions may result in crosswinds"

def UnixConverter(time):
    return datetime.datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S')

def dewpoint(T,RH):
    Td = T - ((100 - RH)/5)
    return int(Td)

def paceValue(T,DP):
    return T+DP

def paceChangeHeat(value):
    if value<=100:
        return "No change in physical performance due to the heat"
    if value>100 and value<111:
        return "There is slight not no change in physical performance due to the heat."
    if value>110 and value<121:
        return "There is a slight change in physical performance due to heat."
    if value>120 and value<131:
        return "There is a noticeable change in physical performance due to heat. Your workout will be harder."
    if value>130 and value<141:
        return "Your workout is getting noticeable harder"
    if value>140 and value<151:
        return "Your workout is definitely harder today in this heat."
    if value>150 and value<161:
        return "You will be running 25 seconds slower per mile. Significant difficulty"
    if value>160 and value<171:
        return "At this point you should stop. "
    if value>170 and value<181:
        return "You are truely insane. Brace for a difficult workout."
    else:
        return "hard exercise outdoors is not recommended"
#USE
def paceChangeCold(temp):
    if temp<10:
        return "pace will be slower if proper warmup and atire is not worn."
    else:
        return
#USE
def windEffect(wind):
    if wind>=1 and wind<=3:
        return "Running performance will not be affected in the direction of wind."
    elif wind>=4 and wind<=7:
        return "Running performance will not be affected in the direction of wind, but wind is noticeable."
    elif wind>=8 and wind<=12:
        return "Running will get slightly harder in the direction of wind."
    elif wind>=13 and wind<=18:
        return "Running will be noticeably harder in the direction of wind."
    elif wind>=19 and wind<=24:
        return "Running will be hard in the direction of wind."
    elif wind>=25 and wind<=31:
        return "Running will be much harder in the direction of wind. You may see things blowing around."
    elif wind>=32 and wind<=38:
        return "Running will be very difficult in the direction of wind. There will be lots of small objects blowing around."
    elif wind>=39 and wind<=46:
        return "Running is possible in the direction of the wind, but not at all recommended."
    elif wind>=47 and wind<=54:
        return "Running will be near impossible today. Danger do not run outside."
    else:
        return "Running will be near impossible today. Danger do not run outside."
#USE
def recommendations():
    return "If weather is very hot run in the late evenings or early morning. If the weather is too cold workout indoors or layer up. "
#def comfortLevel():
    #level=[-20,-10,0,10,20,30,40,50,60,70,80,90,100,110]



#testcases
#Set the variables with useful data
#user_city = "Brooklyn"
#user_state = "NY"
#user_zip = 11217
#user_country = "US"
#user_street_address = "636 Ovington Av."
#print("Please enter location data")
#user_city = input("Enter city: ")
#user_state = input("Enter state code aka NY, NJ, CT : ")
#user_zip = input("Enter zip code: ")
#user_country = input("Enter your country code: ").upper()
##user_comfort = input("Do you prefer running in -20,-10,0,10,20,30,40,50,60,70,80,90,100,110 degree weather?:")
#extratestcases
#print("City: "+data.getUser_city(user_city))
#print("State: "+data.getUser_state(user_state))
#print("Zip: "+str(data.getUser_zip(user_zip)))
#print("Country: "+data.getUser_country(user_country))
#print(data.getLocation_data(user_zip,user_country))
#print("Latitude: "+str(data.getLocation_lat(user_zip,user_country)))
#print("Longitude: "+str(data.getLocation_lon(user_zip,user_country)))
#print(data.getWeather_data(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country)))
#print("Weather: "+data.getWeather(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country)))
#print("Temp: "+str(data.getTemp(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country))))
#print("Humidity: "+str(data.getHumidity(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country))))
#print("Wind Speed: "+str(data.getWind_spd(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country))))
#print("Wind Direction: "+str(data.getWind_dir(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country))))
#print("Sunrise Time: "+str(data.getSunrise(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country))))
#print("Sunset Time: "+str(data.getSunset(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country))))
#print("Icon: "+str(data.getIcon(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country))))

#print("testing")
#print("City: "+data.getUser_city(user_city))
#print("State: "+data.getUser_state(user_state))
#print("Zip: "+str(data.getUser_zip(user_zip)))
#print("Country: "+data.getUser_country(user_country))
#print(calcHeatIndex(data.getTemp(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country)),data.getHumidity(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country))))
#print(tempSafety(calcHeatIndex(data.getTemp(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country)),data.getHumidity(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country)))))
#print(compass(data.getWind_dir(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country))))
#print(UnixConverter(data.getSunrise(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country))))
#print(dewpoint(data.getTemp(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country)),data.getHumidity(data.getLocation_lat(user_zip,user_country),data.getLocation_lon(user_zip,user_country))))