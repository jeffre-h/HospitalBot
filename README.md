# HospitalBot

## Inspiration 
This project was created to combat the emergency healthcare crisis currently happening in Vancouver, B.C. Ever since the 2021 Covid-19 pandemic, there has been an emergency staff shortage affecting the Lower Mainland. In addition, the rise of the record-breaking heatwave in the summer of 2021 left thousands of patients with acute symptoms with no ambulance or emergency service to turn to. This amassed more than 600 deaths, which is a dangerous amount for a well developed country like Canada. Therefore, this healthcare project was created, not only to help patients reach emergency services faster, but also to relieve the stress for all emergency staff.

## Description
*** This project is no longer live as the Twilio API requires a monthly subscription ***

Hospital Bot is a texting chat bot that provides the latest wait times and directions to the nearest hospitals. All hospital data is scraped from: http://www.edwaittimes.ca/WaitTimes.aspx. The value of this chatbot is that it runs fully on SMS via cellular connection, no internet/data connection is necessary for the user. There is also no download required, only a text message is required to get started.

Key Technologies:
- Webscraping & Data Processing: Python, Beautifulsoup, Selenium, Pandas, Lxml, GoogleMaps API 
- Deployment: Twilio, Heroku, Gunicorn, Flask
  
## How to use Hospital Bot
1. Deploy Heroku to run Hospital Bot
2. Text the address of your current location to 255-800-4128 and the HospitalBot will return the 3 closest hospitals with respect to distance and wait time.

![image](https://user-images.githubusercontent.com/90656973/209623520-8858898e-34b8-424f-8481-0bb8b4828e31.png)



## Contributors
- Ronney Lok
- Jeffrey Wong
- Kevin Hau
- Derek Huang

