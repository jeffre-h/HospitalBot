#web scraping practice
import time
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import csv


Hospitals = ['BC Children\'s Hospital',
'Vancouver General Hospital',
'St. Paul\'s Hospital',
'Mount Saint Joseph Hospital',
'UBC Hospital (UBCH)',
'City Centre Urgent & Primary Care Centre',
'REACH Urgent and Primary Care Centre',
'Northeast Urgent and Primary Care Centre',
'Southeast Urgent and Primary Care Centre',
'Richmond Hospital',
'Richmond Urgent and Primary Care Centre',
'Lions Gate Hospital',
'North Van Urgent & Primary Care Centre',
'Squamish General Hospital',
'Whistler Health Care Centre',
'Pemberton Health Centre',
'Sechelt Hospital',]

wait = []
status = []

def open_site(): #not actually currently used
    ChromeDriverManager(log_level=0)  
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://www.edwaittimes.ca/WaitTimes.aspx')
    time.sleep(2)



def print_hospitals_name(): #prints the name of all hospitals
    ChromeDriverManager(log_level=0)  
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://www.edwaittimes.ca/WaitTimes.aspx')
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source,'lxml')
    hospital_table = soup.find_all('div',class_="Row")
    for hospital in hospital_table:
        if hospital.a is not None:
            print("\'" + hospital.a.text + "\',")



def print_hospitals_time():#prints the wait time of all the hospitals
    ChromeDriverManager(log_level=0)    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://www.edwaittimes.ca/WaitTimes.aspx') 
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source,'lxml')
    hospital_table = soup.find_all('div',class_="Row")#finds all div tags with class ="Row"

    for hospital in hospital_table: #loops through hospitals
        if hospital.a is not None: #if a hospital exsits (need this because there are empty blocks of text on website)
            if(hospital.find('div',class_="Cell")): #if hospital div tag and class="Cell" exists
                hos_time = hospital.find('div',class_="Cell") #gets the tiem
                wait_time = hos_time.p.text 
                print(wait_time) #prints wait time to list
            else: #if hospital requires calling to find time or it is closed
                hos_time = hospital.find('div',class_="CellcW")#gets the message
                wait_time = hos_time.p.text
                print(wait_time)#prints message to list


    
def print_hospital_time(name): #prints the specific wait time given the name of the hospital
    ChromeDriverManager(log_level=0)  #gets rid of annoying console message
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #installing driver
    driver.get('http://www.edwaittimes.ca/WaitTimes.aspx') #gets website
    time.sleep(2) #lets website load for 2 seconds
    soup = BeautifulSoup(driver.page_source, 'lxml')#using beautiful soup and lxml to parse through html code
    hospital_table = soup.find_all('div',class_="Row")#finds all div tags with class ="Row"

    for hospital in hospital_table: #loops through hospitals
        if hospital.a is not None: #if a hospital exsits (need this because there are empty blocks of text on website)
            if hospital.a.text == name: # checks if given name is equal to the hospital name we are looking for
                hospital_time = hospital.find('div',class_="Cell") 
                print(hospital_time.p.text)


def append_wait(): #appends all the wait times to wait[]
    ChromeDriverManager(log_level=0)  #gets rid of annoying console message
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #installing driver
    driver.get('http://www.edwaittimes.ca/WaitTimes.aspx') #gets website
    time.sleep(2) #lets website load for 2 seconds
    soup = BeautifulSoup(driver.page_source, 'lxml') #using beautiful soup and lxml to parse through html code
    hospital_table = soup.find_all('div',class_="Row") #finds all div tags with class ="Row"

    for hospital in hospital_table: #loops through hospitals
        if hospital.a is not None: #if a hospital exsits (need this because there are empty blocks of text on website)
            if(hospital.find('div',class_="Cell")): #if hospital div tag and class="Cell" exists
                hos_time = hospital.find('div',class_="Cell") #gets the tiem
                wait_time = hos_time.p.text 
                wait.append(wait_time) #adds wait time to list
            else: #if hospital requires calling to find time or it is closed
                hos_time = hospital.find('div',class_="CellcW")#gets the message
                wait_time = hos_time.p.text
                wait.append(wait_time)#adds message to list
                

def print_status(name): #prints the status given the name of hospital
    ChromeDriverManager(log_level=0)  #gets rid of annoying console message
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #installing driver
    driver.get('http://www.edwaittimes.ca/WaitTimes.aspx') #gets website
    time.sleep(2) #lets website load for 2 seconds
    soup = BeautifulSoup(driver.page_source, 'lxml') #using beautiful soup and lxml to parse through html code
    hospital_table = soup.find_all('div',class_="Row") #finds all div tags with class ="Row"

    for hospital in hospital_table:
        if hospital.a is not None:
            if hospital.a.text ==name:
                hospital_status = hospital.find('div',class_="CellS")

                if hospital_status.find("img",src="Shared/Images/check.png"):
                    status = 1
    
    if status ==1:
        print("Hospital open")
    else:
        print("Hospital not in service")


def append_status(): #appends the status of all the hospitals onto the status[]
    ChromeDriverManager(log_level=0)  #gets rid of annoying console message
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #installing driver
    driver.get('http://www.edwaittimes.ca/WaitTimes.aspx') #gets website
    time.sleep(2) #lets website load for 2 seconds
    soup = BeautifulSoup(driver.page_source, 'lxml')#using beautiful soup and lxml to parse through html code
    hospital_table = soup.find_all('div',class_="Row")#finds all div tags with class ="Row"
    
    
    

    for hospital in hospital_table: #for each hospital on the hospital website
        stat = 0
        if hospital.a is not None: #if a hospital exists there (need this because there are empty blocks of text on website)
                if (hospital.find('div',class_="CellS")): #finds all hospitals with div tag with class="CellS"
                    if (hospital.find("img",src="Shared/Images/check.png")): #find img tag srs equal to checkmark image (meaning it is open)
                        stat = 1
                    
                    else:
                        stat = 0
    
        if stat == 1: #if it is true then add open to list
            status.append("Open")
        else: #if it is false then add closed to list
            status.append("Busy")
        
    status.pop() #gets rid of last element

    
    return status
    

append_status()
append_wait()

def total_wait():
    file=open("hospital_data.csv")
    header=file.readline()
    total = []
    user_origin = input("Please enter your address specifically\n").strip()
    for line in file:
        data=line.strip().split(",")
        timedata = data[1].split(':')
        if (timedata[0] == '\"Currently open'):
            time = 0
        else:
            time = int(timedata[0])*60 + int(timedata[1])
            
        if (timedata[0] == "Pemberton Health Centre"): 
            total.append(time + get_traveltime(user_origin,"pembertonhealthcentre")) 
        else:
            total.append(time + get_traveltime(user_origin,timedata[0]))
    print(total)
    return total


df = pd.DataFrame({'Hospitals': Hospitals, 'Wait Time':wait, 'Status': status})
df.to_csv('hospital_data.csv' , index=False) #extra index=False parameter if want to remove numbers before name



