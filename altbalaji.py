import undetected_chromedriver.v2 as  webdriver

import base64
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






mobile_emulation = {"deviceName": "iPhone SE"}
#options.add_experimental_option("mobileEmulation", mobile_emulation)
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
#options.add_experimental_option("mobileEmulation", mobile_emulation)
count=0
recount=0
key = 'sub_1M0ulICRwBwvt6ptsU5sJPCD'
total=0
if __name__ == "__main__":
 while(1):


  numb="0123456789"
  if (total >= 20):

      break
  
  url='https://www.altbalaji.com/user-detail'
  fnumbers=["1400076041","1400115397","1400195961","1400218732","1400245578","1400508294","1400586088","1400819993","1400855140","1400963166","1401137604","1401184255","1401363730","1401642326","1401651255","1401862030","1401923450","1401985313","1401990512","1402043218","1402049023","1402053263","1402089532","1402119176","1402141316","1402258859","1402273508","1402300837","1402450915","1402475530","1402482894","1402636067","1402668106","1402888920","1403018836","1403030431","1403091358","1403268454","1403313025","1403591286","1403595044","1403601418","1403618559","1403667681","1403695813","1403808632","1403844562","1403850864","1403875161","1403885038","1404013375","1404034108","1404122087","1404139190","1404175706","1404328428","1404370076","1404375718","1404521333","1404532705","1404533836","1404550286","1404554080","1404585528","1404646037","1404649769","1404684942","1404764084","1404818534","1404838767","1404981301","1405027256","1405200973","1405469727","1405471023","1405560389","1405600566","1405642711","1406149866","1406826229","1406936049","1407550347","1407552079","1407605688","1408223736","1408633624","1408895034","1408928410","1408937795","1409006595","1409243826","1409293440","1902080533","1902119261","1902148339","1902220138","1902270816","1902414744","1902764829","1902960846","1903371004","1904332391","1905096514","1905399145","1906105790","1906156857","1906697959","1907159131","1908019563","1908542890","1908582416","1908781534","1909234982","1910307027","1910987350","1911074379","1911202689","1911212491","1911400666","1911531929","1911566720","1911660047","1911854496","1911972227","1912075034","1912121866","1912301345","1912311381","1912471433","1912679336","1912726046","1913120442","1913149942","1913637494","1913961553","1914173595","1914486180","1914731449","1914790274","1915034241","1915197140","1915375681","1915765148","1915827006","1916195229","1916465595","1916486312","1916574785","1916767909","1916906489","1917181793","1917256953","1917619893","1918170318","1918317501","1918385768","1918426924","1918499954","1918512644","1918714055","1918731635"]
  mailcount=0

  numbers=[]




  while(1):

      try:
          options = webdriver.ChromeOptions()
          # options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')
          #options.add_argument('--headless')
          options.add_argument("--disable-renderer-backgrounding")
          options.add_argument("--disable-backgrounding-occluded-windows")
          # options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')
          options.add_argument('--load-extension=D:\\autologinbot-master\\Urbanvpn')
          browser = webdriver.Chrome(options=options, desired_capabilities=capa,version_main=109)
          i = random.randint(2, 57)
          inb = 'infotelcotestahymed@gmail.com'
          browser.get(
              "chrome-extension://ecokmenakcanpnkbgifdiacoapdmhdjf/popup/index.html#/welcome-consent")
          try:

              WebDriverWait(browser, 10).until(
                  EC.presence_of_element_located(
                      (By.CSS_SELECTOR,
                       "body > div > div > div.simple_layout__body > div > div > div > button.button_pink.agreement_agree"))).click()
          except:
              pass
          try:

              WebDriverWait(browser, 10).until(
                  EC.presence_of_element_located(
                      (By.CSS_SELECTOR,
                       "body > div > div > div.simple_layout__header > div"))).click()
          except:
              pass
          time.sleep(2)

          WebDriverWait(browser, 20).until(
              EC.presence_of_element_located((By.CSS_SELECTOR,
                                              "body > div > div > div.main_layout__body > div.location-box > div > div:nth-child(1) > input"))).click()
          time.sleep(2)
          ph = WebDriverWait(browser, 20).until(
              EC.presence_of_element_located(
                  (By.XPATH, "/html/body/div/div/div[3]/div[2]/div/div[2]/div/ul/li[" + str(i) + "]")))
          browser.execute_script("arguments[0].scrollIntoView(true);", ph);
          ph.click()
          print('country is: ' + str(i))


          while (1):

              try:
                  total = 0



                  browser.get(url)


                  time.sleep(2)


                  phonee = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located(
                          (By.CSS_SELECTOR,
                           'body > app-root > main > app-user-detail > div > div.row.pt-3 > div > app-login > div > div > section > div > form > div.form-group.country-form-group > input')))

                  phonee.send_keys(fnumbers[recount])
                  phonee = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located(
                          (By.CSS_SELECTOR,
                           '#dropdownMenuButton')))

                  phonee.click()
                  phonee = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located(
                          (By.CSS_SELECTOR,
                           '#search-country')))

                  phonee.send_keys("bangladesh")
                  phonee = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located(
                          (By.CSS_SELECTOR,
                           '#dropdownMenuButton > ul > li.country-list > ul > li')))

                  phonee.click()
                  time.sleep(1)


                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      'body > app-root > main > app-user-detail > div > div.row.pt-3 > div > app-login > div > div > section > div > form > div.form-group.ng-star-inserted > button')))

                  usernap.click()
                  try:
                      usernap = WebDriverWait(browser, 5).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          '#latpickrDatePicker')))
                      usernap.click()
                  except:
                      usernap = WebDriverWait(browser, 5).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          'body > app-root > main > app-user-detail > div > div.row.pt-3 > div > app-login > div > div > section > div > form > div.form-group.ng-star-inserted > button')))

                      usernap.click()
                      usernap = WebDriverWait(browser, 120).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          '#latpickrDatePicker')))
                      usernap.click()




                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      'body > div.flatpickr-calendar.animate.arrowTop.arrowLeft.open > div.flatpickr-innerContainer > div > div.flatpickr-days > div > span:nth-child(12)')))
                  usernap.click()
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#signupSubmitProcessMobile')))
                  usernap.click()
                  usernap = WebDriverWait(browser, 10).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      'body > app-root > main > app-user-detail > div > div.row.pt-3 > div > app-login > div > div > section > div > form > div.form-group.otp-container > div:nth-child(1) > div > input')))

                  time.sleep(3)



                  browser.delete_all_cookies()
                  if (recount < (len(fnumbers) - 1)):
                      recount = recount + 1
                  else:
                      recount = 0
                      total+=1
                      print(total)


                  count+=1
                  if(count%250==0):
                      i = random.randint(2, 57)
                      inb = 'infotelcotestahymed@gmail.com'
                      browser.get(
                          "chrome-extension://ecokmenakcanpnkbgifdiacoapdmhdjf/popup/index.html#/welcome-consent")
                      try:

                          WebDriverWait(browser, 10).until(
                              EC.presence_of_element_located(
                                  (By.CSS_SELECTOR,
                                   "body > div > div > div.simple_layout__body > div > div > div > button.button_pink.agreement_agree"))).click()
                      except:
                          pass
                      try:

                          WebDriverWait(browser, 10).until(
                              EC.presence_of_element_located(
                                  (By.CSS_SELECTOR,
                                   "body > div > div > div.simple_layout__header > div"))).click()
                      except:
                          pass
                      time.sleep(2)

                      WebDriverWait(browser, 20).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          "body > div > div > div.main_layout__body > div.location-box > div > div:nth-child(1) > input"))).click()
                      time.sleep(2)
                      ph = WebDriverWait(browser, 20).until(
                          EC.presence_of_element_located(
                              (By.XPATH, "/html/body/div/div/div[3]/div[2]/div/div[2]/div/ul/li[" + str(i) + "]")))
                      browser.execute_script("arguments[0].scrollIntoView(true);", ph);
                      ph.click()
                      print('country is: ' + str(i))
                  print(count)
                  browser.refresh()






              except  Exception as e:
                  delete_cache(browser)







      except:



          browser.quit()
          print('biggest exception')




   


     
      


     
     
     
     
  
