from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

names = []
wait_times = []
status = []

# names
def extract_names():
    #ChromeDriverManager(log_level=0)  
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://www.edwaittimes.ca/WaitTimes.aspx')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    soup = BeautifulSoup(driver.page_source,'lxml')
    rows = soup.find_all('div', class_='Row')
    for r in rows:
        if (r.a is not None):
            h = r.find('div', class_='CellfcW2')
            c = r.find('div', class_='CellcW')
            if (h.a is not None):
                if (r.find('div',class_='Cell')):
                    names.append(h.a.text+" - British Columbia")
                else:
                    if (c is not None):
                        if (c.p.text != "Currently closed"):
                            names.append(h.a.text+" - British Columbia")
    driver.close()
    return names


# wait times
def extract_wait_times():
    #ChromeDriverManager(log_level=0)  
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://www.edwaittimes.ca/WaitTimes.aspx')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    soup = BeautifulSoup(driver.page_source, 'lxml')
    rows = soup.find_all('div', class_='Row')
    
    for r in rows:
        if (r.a is not None):
            if (r.find('div',class_='Cell')):
                t = r.find('div',class_='Cell')
                wait_times.append(t.p.text)
            else:
                t = r.find('div',class_='CellcW')
                if (t.p.text != "Currently closed"):
                    txt = t.p.text.replace(',','.')
                    wait_times.append(txt)
    
    driver.close()
    return wait_times


# status 
# can either be "Open" or "Abnormally Busy" or "Call"
def extract_status():
    #ChromeDriverManager(log_level=0)  
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://www.edwaittimes.ca/WaitTimes.aspx')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    soup = BeautifulSoup(driver.page_source,'lxml')
    rows = soup.find_all('div', class_='Row')
    for r in rows:
        if (r.a is not None):
            if (r.find('div', class_='CellS')):
                if (r.find("img",src="Shared/Images/check.png")):
                    status.append("Open")
                else:
                    status.append("Abnormally Busy")
            if (r.find('div', class_='CellcW')):
                s = r.find('div', class_='CellcW')
                if (s.p.text != "Currently closed"):
                    status.append('Call')
    
    driver.close()
    return status
    

def csv():
    names = extract_names()
    times = extract_wait_times()
    status = extract_status()
    frame = pd.DataFrame({'Hospital Name': names,'Wait Time': times,'Status': status})
    frame.to_csv('hospital_data.csv', index=False)
