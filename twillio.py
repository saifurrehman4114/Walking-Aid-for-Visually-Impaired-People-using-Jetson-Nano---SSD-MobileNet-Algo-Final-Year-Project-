import os
from twilio.rest import Client
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
import time
import chromedriver_binary
import keyboard
import board
import digitalio
import os 

def getLocation():
    options = Options()
    options.add_argument("--use--fake-ui-for-media-stream")
    #driver = webdriver.Chrome(executable_path = './chromedriver_linux64',options=options) #Edit path of chromedriver accordingly
    driver = webdriver.Chrome(options=options) 

    timeout = 0
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    #time.sleep(0.1)

    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]') #Replace with any XPath    
    longitude = [x.text for x in longitude]    
    longitude = str(longitude[0])    
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')    
    latitude = [x.text for x in latitude]    
    latitude = str(latitude[0])    
    # driver.quit()    
    
    return (latitude,longitude)


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure

def twilio_msg_snd():
    account_sid = 'ACaa0aa6365eae80dc7df66a9f6bb477de'
    auth_token = '3f90956ebcc5310862a47a2a98b8ad77'
    client = Client(account_sid, auth_token)


    latitude,longitude = getLocation()

    message = client.messages \
                    .create(
                        
                        body=f'testing for location sender Visual Impairment System https://www.google.com/maps/search/?api=1&query={latitude},{longitude}',
                        
                        from_='+14075422226',
                        to='+923325928317'
                    )

#twilio_msg_snd()







button = digitalio.DigitalInOut(board.D4)
button.direction = digitalio.Direction.INPUT
# use an external pullup since we don't have internal PU's
button.pull = digitalio.Pull.UP

while True:
    #print(button.value) # light when button is pressed!
 if(button.value == False):
  twilio_msg_snd()

