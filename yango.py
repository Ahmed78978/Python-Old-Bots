import undetected_chromedriver.v2 as  webdriver
from TempMail import TempMail #imports everything from TempMail library

import  re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import string
import random
import time
import requests
from apiclient import discovery
from apiclient import errors
from httplib2 import Http
from oauth2client import file, client, tools
import base64
from bs4 import BeautifulSoup
import re
import time
import dateutil.parser as parser
from datetime import datetime
import datetime
import csv
import email
import imaplib
def read_emails_from_file(file_path):
    emails = []
    with open(file_path, 'r') as f:
        for line in f:
            email = line.strip()
            emails.append(email)
    return emails
inb=read_emails_from_file("infokamalhmed.txt")
user = "infokamalhmed@gmail.com"
gmail_pass = "exbbdrfxhdedqngi"
host = "imap.gmail.com"
# Creating a storage.JSON file with authentication details
def read_email_from_gmail(count=3, contain_body=True):

    # Create server and login
    mail = imaplib.IMAP4_SSL(host)
    mail.login(user, gmail_pass)

    # Using SELECT to chose the e-mails.
    res, messages = mail.select('INBOX')

    # Caluclating the total number of sent Emails
    messages = int(messages[0])

    # Iterating over the sent emails
    for i in range(messages, messages - count, -1):
        # RFC822 protocol
        res, msg = mail.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])

                # Store the senders email
                sender = msg["From"]

                # Store subject of the email
                subject = msg["Subject"]

                # Store Body
                body = ""
                temp = msg
                if temp.is_multipart():
                    for part in temp.walk():
                        ctype = part.get_content_type()
                        cdispo = str(part.get('Content-Disposition'))

                        # skip text/plain type
                        if ctype == 'text/plain' and 'attachment' not in cdispo:
                            body = part.get_payload(decode=True)  # decode
                            break
                else:
                    body = temp.get_payload(decode=True)


                return subject


def delete_cache(driver):

    driver.switch_to.window(driver.window_handles[-1])  # Switch window to the second tab
    driver.get('chrome://settings/clearBrowserData')  # Open your chrome settings.
    perform_actions(driver, Keys.TAB * 2 + Keys.DOWN * 4 + Keys.TAB * 7 + Keys.ENTER)  # Tab to the time select and key down to say "All Time" then go to the Confirm button and press Enter


def perform_actions(driver, keys):
    actions = ActionChains(driver)
    actions.send_keys(keys)
    time.sleep(5)
    print('Performing Actions!')
    actions.perform()

def convertTuple(tup):
        # initialize an empty string
    strc = ''
    c=len(tup)
    
    for item in range(5):
        strc=strc+strc.join(tup[item])
        
    return strc
letters = string.ascii_lowercase
usernameStr=['zahidkamal78978@gmail.com','zahid60@gmail.com','78978@gmail.com']

Str = ''






mobile_emulation = {"deviceName": "iPhone SE"}
#options.add_experimental_option("mobileEmulation", mobile_emulation)
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
#options.add_experimental_option("mobileEmulation", mobile_emulation)
count=0
recount=0
total=0
mai=1500
if __name__ == "__main__":
 while(1):

  numb="0123456789"
  if (total >= 10):

      break
  
  url='https://passport.yandex.com/auth?retpath=https%3A%2F%2Fyandex.com%2F&msid=1687942405778832-7038542009592573738-balancer-l7leveler-kubr-yp-sas-21-BAL-1098&origin=home_yaru_touch_new'
  fnumbers = ["+923312829602","+923312825594","+923374380481","+923301372798","+923360376502","+923378410611","+923312186787","+923378346043","+923322581722","+923323456525","+923352274392","+923358217624","+923303844236","+923323614156","+923378070865","+923303153279","+923322645523","+923343242539","+923323859117","+923361240317","+923492861791","+923378346005","+923378092531","+923370370677","+923352893161","+923323574077","+923378241001","+923302495351","+923341021994","+923313246102","+923317516229","+923358186701","+923362289245","+923321501307","+923313789804","+923315176878","+923378073729","+923343410478","+923378212278","+923340032047","+923318354355","+923322527520","+923352786871","+923326917712","+923241287046","+923241286842","+923353130551","+923303622501","+923303278433","+923312238766","+923316058689","+923302065466","+923374371375","+923301475996","+923343919714","+923343324853","+923327357422","+923362076470","+923302065506","+923323842954","+923367190834","+923089501298","+923378098704","+923303413225","+923326918035","+923312262853","+923343653220","+923323408016","+923358217440","+923352367610","+923323849574","+923327357933","+923323243921","+923316842272","+923322604247","+923312263961","+923304341688","+923353064076","+923302512471","+923378342933","+923342646941","+923327228061","+923343393625","+923343323628","+923322528905","+923322548775","+923303525508","+923488764497","+923322891918","+923306488138","+923364691151","+923349525386","+923315625049","+923314907972","+923321322377","+923302065586","+923360392740","+923378243509","+923323425944","+923322604201","+923350323058","+923378346048","+923323793876","+923342743806","+923312307910","+923318179978","+923351339357","+923318930920","+923370436463","+923369402119","+923363682108","+923216894798","+923308697289","+923313974782","+923368988176","+923312836553","+923302513076","+923378092588","+923351250594","+923350322463","+923318830932","+923378346032","+923360472998","+923365041570","+923350321523","+923307025341","+923306513438","+923352042974","+923378096278","+923353117091","+923352876158","+923302539692","+923378342910","+923361368950","+923327810430","+923306490115","+923307175686","+923378096290","+923315624609","+923342532205","+923323849921","+923323845079","+923303276168","+923378241022","+923322621317","+923302489627","+923318377045","+923322450393","+923301480836","+923343253967","+923318849886","+923313975278","+923352139382","+923301293473","+923312559321","+923361292243","+923317071436","+923343211592","+923351249850","+923365040317","+923323456221","+923378094178","+923303278544","+923378212364","+923352335879","+923348597224","+923378241984","+923302545068","+923320482481","+923315301607","+923307026890","+923342361453","+923323486967","+923378241092","+923378418229","+923351130531","+923191738645","+923342881347","+923315194390","+923353750095","+923363705291","+923350230281","+923322659398","+923322527418","+923366135794","+923323587086","+923303276139","+923342657078","+923358188450","+923363286886","+923312251432","+923313974969","+923308768228","+923342744375","+923378342950","+923363926508","+923362001571","+923378343822","+923322473099"]

  mailcount=0

  numbers=[]

  while (1):
      if (total >= 10):
          break
      try:




          while (1):


              try:










                  while (1):
                      options = webdriver.ChromeOptions()
                      # options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')
                      options.add_argument("--disable-renderer-backgrounding")
                      options.add_argument("--disable-backgrounding-occluded-windows")
                      # disable images
                      # options.add_argument('--blink-settings=imagesEnabled=false')

                      # disable animations
                      options.add_argument('--disable-gpu')
                      # options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2\\')
                      # options.add_argument("user-data-dir=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2\\")
                      options.add_argument(
                          '--load-extension=D:\\autologinbot-master\\chromium_automation')
                      browser = webdriver.Chrome(options=options, version_main=114, desired_capabilities=capa)

                      browser.get(url)

                      usernap = WebDriverWait(browser, 50).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          '#root > div > div.passp-page > div.passp-flex-wrapper > div > div > div.passp-auth-content > div:nth-child(3) > div > div > div > div > form > div > div.layout_content > div.AuthLoginInputToggle-wrapper.AuthLoginInputToggle-wrapper_theme_default > div:nth-child(2) > button')))
                      usernap.click()
                      time.sleep(2)
                      while (1):
                         try:
                          usernap = WebDriverWait(browser, 2).until(
                              EC.presence_of_element_located((By.CSS_SELECTOR,
                                                              '#passp-field-phone')))
                          usernap.send_keys(fnumbers[recount])
                          break
                         except:
                             usernap = WebDriverWait(browser, 50).until(
                                 EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                 '#root > div > div.passp-page > div.passp-flex-wrapper > div > div > div.passp-auth-content > div:nth-child(3) > div > div > div > div > form > div > div.layout_content > div.AuthLoginInputToggle-wrapper.AuthLoginInputToggle-wrapper_theme_default > div:nth-child(2) > button')))
                             usernap.click()

                      usernap = WebDriverWait(browser, 50).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          '#passp\:sign-in')))
                      usernap.click()
                      time.sleep(1)
                      c=0
                      d=0
                      while(1):
                          try:

                              usernap = WebDriverWait(browser, 1).until(
                                  EC.presence_of_element_located((By.XPATH,
                                                                  "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/form/div/div[3]/button[2]/span/span[2]")))

                          except:
                              d+=1
                              if(d>200):
                                  break
                              time.sleep(1)

                              usernap = WebDriverWait(browser, 50).until(
                                  EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                  '#UserEntryFlow > form > div > div.PhoneConfirmationCode-controls.layout_controls > button.Button2.Button2_size_l.Button2_view_default.Button2_width_max')))
                              usernap.click()
                              c+=1
                              if(c%6==0):
                                  break

                      count = count + 1
                      if (recount < (len(fnumbers) - 1)):
                          recount = recount + 1
                      else:
                          recount = 0

                      print(count)
                      browser.quit()

















              except  Exception as e:

                  browser.quit()



      except:


          browser.quit()
          print('biggest exception')



   


     
      


     
     
     
     
  
