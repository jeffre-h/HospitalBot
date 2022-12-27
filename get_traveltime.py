from time import time_ns
import requests


def get_traveltime(user_origin, destination):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+user_origin+"&destinations="+destination+"&units=imperial&key=AIzaSyBuTicylmUtgzgzzxuTpKow3ClCKWIBXLA"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)


    time = response.json()["rows"][0]["elements"][0]["duration"]["text"]       
    seconds = response.json()["rows"][0]["elements"][0]["duration"]["value"]


    #print(time)
    # print(time.count("hour"))

    i = 0
    i2 = 0
    index = 0
    str_min = ''
    str_hr = ''

    if (time.count("hour") == 0):
        while i == 0:
            if (ord(time[index]) > 57 or ord(time[index]) < 48):
                i += 1

            str_min = str_min + time[index]
            index +=1


    if (time.count("hour") != 0):
        while i == 0:
            if(ord(time[index]) > 57 or ord(time[index]) < 48):
                i += 1
            
            str_hr = str_hr + time[index]
            index +=1


        while i2 == 0:
            if (time.count("hours")):
                if(ord(time[index+6]) > 57 or ord(time[index+6]) < 48):
                    i2 += 1
                
                str_min = str_min + time[index+5]
                index +=1   
            else:
                if(ord(time[index+5]) > 57 or ord(time[index+5]) < 48):
                    i2 += 1
                
                str_min = str_min + time[index+5]
                index +=1
    

    if (time.count("hour") == 0):
        total_min = int(str_min)
    if (time.count("hour") != 0):
        total_min = int(str_hr) * 60 +  int(str_min)
    
    return total_min
  

#running the function. Eventually, the function call would have to take 2 parameters. Origin and Destination.
user_origin = input("Please enter your address specifically\n").strip()
destination = input("Please enter you destination\n").strip()
print(get_traveltime(user_origin,destination))
