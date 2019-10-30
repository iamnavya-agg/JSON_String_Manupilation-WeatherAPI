#a1.py
#Homework - 1 -Introduction to Progamming(CSE-101)
#Navya Aggarwal (Roll no.:2018349)
#Section - B Group - 6


# function to get weather response
def weather_response(location , API_key = '59fe78995a142fb300bccb6e0d57616a'):
    """ Returns - a JSON string that is a response to a weather query.
    A weather query returns the JSON with weather attribute like
    temperature , pressure , humidity and wind speed etc.
    Parameter location : the city name(use '+' for space between two parts of name of place)
    Precondition : city name should be correct
    Parameter API_key : a valid key of weather service
    precondition : for better use one key once in 10 minute.
    """
    website = 'http://api.openweathermap.org/data/2.5/forecast?q='+location+'&APPID='+API_key
    import urllib.request
    response = urllib.request.urlopen(website)
    data = response.read()
    data = str(data)
    return data
	


# function to check for valid response 
def has_error(location,json):
     """Returns : True if the input location and response city name
        is not matched
        Parameter json : a json string to parse
        Precondition : json is the response to a weather query
     """   
     flag = int(json.find("name")) + 7
     name = json[flag:(flag+len(location))]
     location1 = location[0].upper() + location[1:]
     if name != location1:
	       return True
    

# function to get temperature on nth day
def get_temperature (json, n=0 , t = "03:00:00"):
     """Return the temperature of the nth day from the current date.
        Parameter json : a json string to parse
        n : day from the current day , valid values are 0 to 4
        t : time valid values are 00:00 , 03:00 , 06:00 , 09:00 ,
            12:00 , 15:00 , 18:00 , 21:00
        Precondition : json is the response to a weather query
     """   
     import datetime
     time_date = datetime.datetime.now()
     time_date += datetime.timedelta(days=n)
     time_date = str(time_date)
     date = time_date[:10] + " " + t
     x = int(json.find(date))
     day_data = json[x-321:x]
     temp_flag = int(day_data.find('"temp":'))
     day_data = day_data[temp_flag:]
     x1 = int(day_data.find(':')) + 1
     comma = int(day_data.find(","))
     temp = str(day_data[x1:comma])
     temp = float(temp)
     return temp


# function to get humadity on nth day
def get_humidity (json, n=0 , t = "03:00:00"):
     """Return the humidity of the nth day from the current date.
        Parameter json : a json string to parse
        n : day from the current day , valid values are 0 to 4
        t : time valid values are 00:00 , 03:00 , 06:00 , 09:00 ,
            12:00 , 15:00 , 18:00 , 21:00
        Precondition : json is the response to a weather query
     """   
     import datetime
     time_date = datetime.datetime.now()
     time_date += datetime.timedelta(days=n)
     time_date = str(time_date)
     date = time_date[:10] + " " + t
     x = int(json.find(date))
     day_data = json[x-321:x]
     humidity_flag = int(day_data.find("humidity"))+10
     comma_data = day_data[humidity_flag:]
     comma = int(comma_data.find(","))
     humidity = day_data[humidity_flag:humidity_flag+comma]
     humidity = float(humidity)
     return humidity



# function to get pressure on nth day
def get_pressure (json, n=0 , t = "03:00:00"):
     """Return the pressure of the nth day from the current date.
        Parameter json : a json string to parse
        n : day from the current day , valid values are 0 to 4
        t : time valid values are 00:00 , 03:00 , 06:00 , 09:00 ,
            12:00 , 15:00 , 18:00 , 21:00
        Precondition : json is the response to a weather query
     """
     import datetime
     time_date = datetime.datetime.now()
     time_date += datetime.timedelta(days=n)
     time_date = str(time_date)
     date = time_date[:10] + " " + t
     x = int(json.find(date))
     day_data = json[x-321:x]
     pressure_flag = int(day_data.find("pressure"))+10
     comma_data = day_data[pressure_flag:]
     comma = int(comma_data.find(","))
     pressure = day_data[pressure_flag:pressure_flag+comma]
     pressure = float(pressure)
     return pressure


# function to get wind speed on nth day
def get_wind (json, n=0 , t = "03:00:00"):
     """Return the wind speed of the nth day from the current date.
        Parameter json : a json string to parse
        n : day from the current day , valid values are 0 to 4
        t : time valid values are 00:00 , 03:00 , 06:00 , 09:00 ,
            12:00 , 15:00 , 18:00 , 21:00
        Precondition : json is the response to a weather query
     """
     import datetime
     time_date = datetime.datetime.now()
     time_date += datetime.timedelta(days=n)
     time_date = str(time_date)
     date = time_date[:10] + " " + t
     x = int(json.find(date))
     day_data = json[x-321:x]
     wind_flag = int(day_data.find("wind"))+15
     comma_data = day_data[wind_flag:]
     comma = int(comma_data.find(","))
     wind = day_data[wind_flag:wind_flag+comma]
     wind = float(wind)
     return wind


# function to get sea level on nth day
def get_sealevel (json, n=0 , t = "03:00:00"):
     """Return the sea level of the nth day from the current date.
        Parameter json : a json string to parse
        n : day from the current day , valid values are 0 to 4
        t : time valid values are 00:00 , 03:00 , 06:00 , 09:00 ,
            12:00 , 15:00 , 18:00 , 21:00
        Precondition : json is the response to a weather query
     """
     import datetime
     time_date = datetime.datetime.now()
     time_date += datetime.timedelta(days=n)
     time_date = str(time_date)
     date = time_date[:10] + " " + t
     x = int(json.find(date))
     day_data = json[x-321:x]
     sea_flag = int(day_data.find("sea_level"))+11
     comma_data = day_data[sea_flag:]
     comma = int(comma_data.find(","))
     sea_level = day_data[sea_flag:sea_flag+comma]
     sea_level = float(sea_level)
     return sea_level
