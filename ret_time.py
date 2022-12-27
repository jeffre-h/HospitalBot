import requests

# add " - British Columbia" at the end of user input (location)

# travel time from location to a destination
def travel_time(location, destination):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+location+"&destinations="+destination+"&units=imperial&key=AIzaSyBuTicylmUtgzgzzxuTpKow3ClCKWIBXLA"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    t = response.json()["rows"][0]["elements"][0]["duration"]["text"]
    time = ""
    token = False
    nums = ['1','2','3','4','5','6','7','8','9','0']

    if ("hours" in t or "hour" in t): # < 60 mins
        for i in t:
            if (i in nums and token == False):
                time = time + i
            if (i == ' '):
                token = True
        time = time + ':'
        
        if ("hours" in t):
            st = t.partition("hours ")[2]
        else:
            st = t.partition("hour ")[2]

        for i in st:
            if (i in nums):
                time = time + i 
    else: # < 60 mins
        time = time + "0:"
        for i in t:
            if (i in nums):
                time = time + i 
    
    part = time.partition(":")
    mins = int(part[0])*60 + int(part[2])
    return mins


# wait time at given hospital
# hospital can't have status call:
def wait_time(hospital):
    file = open("hospital_data.csv")
    removeHeaders = file.readline()

    for line in file:
        dataline = line.strip().split(",")
        if (dataline[0] == hospital):
            w = dataline[1].partition(":")
            file.close()
            return int(w[0])*60 + int(w[2])


# total time = travel time + wait time 
def total_time(location,destination):
    return travel_time(location,destination) + wait_time(destination)


# helper function that sorts dictionary
def sort_dict(dictionary):
    temp = sorted(dictionary.values())
    sorted_d = {}

    for i in temp:
        for j in dictionary.keys():
            if (dictionary[j] == i):
                sorted_d[j] = dictionary[j]

    return sorted_d


#create a dict storing all the wait times in order
def travel_time_dict(location):
    file = open("hospital_data.csv")
    removeHeaders = file.readline()

    sorted_tr_time = {}
    for line in file:
        dataline = line.strip().split(",")
        sorted_tr_time[dataline[0].replace(" - British Columbia",'')] = travel_time(location,dataline[0])
        
    file.close()
    return sort_dict(sorted_tr_time)


# create a dict storing all the total times in order 
def total_time_dict(location):
    file = open("hospital_data.csv")
    removeHeaders = file.readline()

    sorted_tot_time = {}
    for line in file:
        dataline = line.strip().split(",")
        if (dataline[2] != "Call"):
            sorted_tot_time[dataline[0].replace(" - British Columbia",'')] = total_time(location,dataline[0])

    file.close()
    return sort_dict(sorted_tot_time)


# given hospital, if status is "Call" returns message with phone number to call 
def status_checker(hospital):
    file = open("hospital_data.csv")
    removeHeaders = file.readline()

    for line in file:
        dataline = line.strip().split(",")
        if (dataline[0] == hospital):
            return dataline[2]


# if hospital has status "Call" return the phone number
def call_number(hospital):
    file = open("hospital_data.csv")
    removeHeaders = file.readline()

    for line in file:
        dataline = line.strip().split(",")
        if (dataline[0] == hospital):
            return dataline[1]


# converts time from mins to "x:xx"
def time_conversion(t):
    m = t%60
    mins = str(m)
    hrs = int((t-m)/60)

    if (len(mins) == 1):
        if (mins == "0"):
            return str(hrs)+":"+mins+"0"
        else:
            return str(hrs)+":0"+mins
    else:
        return str(hrs)+":"+mins

             
# given address, output top 3 hospital choices 
# check if hospital status is not "call"
# if hospital status is "Busy" warn the user
def output(location):
    tr_d = travel_time_dict(location)

    call_hospitals = {}
    for i in range(3):
        name = list(tr_d)[i]
        if (status_checker(name + " - British Columbia") == "Call"):
            call_hospitals[i] = name
    
    tot_d = total_time_dict(location)
    
    ret = ""
    if (call_hospitals):
        count = 1
        ret += "The following hospital(s) are close to your address, but you have to call for further information:\n"
        for x,y in call_hospitals.items():
            ret += (str(count) + ". "+ y +  " is " + call_number(y + " - British Columbia").lower().replace('.',',') + ".\n")
            count += 1
        ret += "\n"
    
    ret += "Accounting for distance from hospital and wait time, your top 3 options are:\n"
    for i in range(1,4):
        t = time_conversion(list(tot_d.values())[i])
        ret += str(i)+". "+list(tot_d)[i]+", total time: " + t + "\n"
    
    return ret

