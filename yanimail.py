import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
import string
import random
import time
def convertTuple(tup):
        # initialize an empty string
    strc = ''
    c=len(tup)
    
    for item in range(5):
        strc=strc+strc.join(tup[item])
        
    return strc
letters = string.ascii_lowercase
#usernameStr = 'poppyharlow78978'
usernameStr = 'hggmn56yt'
Str = ''
options = uc.ChromeOptions()

#options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')
options.add_argument('--load-extension=D:\\autologinbot-master\\UltraSur')

#options.add_argument('--load-extension=D:\\autologinbot-master\\LOBBY\\Nope')
mobile_emulation = {"deviceName": "iPhone SE"}
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
#options.add_experimental_option("mobileEmulation", mobile_emulation)
count=0
recount=0
#time.sleep(1000)
while(1):
 while(1):  
  numb="0123456789"
 
  url='https://www.yaanimail.com/register'

  fnumbers = ["3368603207", "3368987986", "3369471349", "3370334378", "3370698250", "3324975741", "3304689699",
              "3367909642", "3368602263", "3368987985", "3369470168", "3370334374", "3370698249", "3324975766",
              "3304766571", "3367909509", "3368601702", "3368987976", "3369465875", "3370334369", "3370698244",
              "3324975860", "3304915933", "3367909485", "3368575532", "3368987974", "3369464742", "3370334328",
              "3370696523", "3324974299", "3310156215", "3368060237", "3368670587", "3368988458", "3369574568",
              "3370338067", "3370771209", "3324974310", "3314385265", "3368059750", "3368670488", "3368988454",
              "3369572855", "3370338065","3302589975","3367920812","3368604797","3368988029","3369479011","3370334508","3370711570","3324975516","3303453117","3367916878","3368604796","3368988016","3369476427","3370334398","3370711506","3324975583","3303482890","3367915870","3368604794","3368988014","3369471875","3370334386","3370711233","3324975650","3303877823","3367914558","3368604271","3368987996","3369471802","3370334381","3370710554","3324975731","3304020302","3367914495","3368603797","3368987989","3369471614","3370334379","3370698768","3324975738","3304020320","3367911259","3368603207","3370334532", "3370720213", "3324975299", "3366738467", "3367922041", "3368608093", "3368988097",
              "3369491255", "3370334528", "3370719802", "3324975317", "3302362973", "3367922039", "3368608074",
              "3368988096", "3369487962", "3370334527", "3370717740", "3324975335", "3302367094", "3367922035",
              "3368607540", "3368988093", "3369487784", "3370334526", "3370714751", "3324975428", "3302387664",
              "3367921546", "3368606598", "3368988058", "3369487210", "3370334516", "3370711734", "3324975429",
              "3302388127", "3367920816", "3368604798", "3368988031", "3369483443", "3370334513", "3370711672",
              "3324975469"]

  numbers=[]
 
  while(1):
    options = uc.ChromeOptions()

      # options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')
    options.add_argument("--disable-renderer-backgrounding")
    options.add_argument("--disable-backgrounding-occluded-windows")
    options.add_argument('--load-extension=D:\\autologinbot-master\\UltraSur')
    browser = uc.Chrome(options=options,use_subprocess=True,version_main=105)
    num='0123456789'







    while(1):







     try:

        while(1):
         browser.get(url)
         phonee = WebDriverWait(browser, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                'body > app-root > app-register > div > div > div > app-general-step > form > div.modal-static-body > div:nth-child(1) > input')))
         phonee.send_keys(random.choices(string.ascii_lowercase, k=9))
         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             'body > app-root > app-register > div > div > div > app-general-step > form > div.modal-static-body > div:nth-child(2) > div.input-group.mb-1 > input')))
         phonee.send_keys(random.choices(string.ascii_lowercase, k=9),random.choices(num,k=3))
         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             'body > app-root > app-register > div > div > div > app-general-step > form > div.modal-static-body > div:nth-child(3) > div.input-group > input')))
         phonee.send_keys('A@hmed12')
         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             'body > app-root > app-register > div > div > div > app-general-step > form > div.modal-static-body > div:nth-child(4) > div > input')))
         phonee.send_keys('A@hmed12')
         time.sleep(5)
         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             'body > app-root > app-register > div > div > div > app-general-step > form > div.modal-static-footer > div.form-group > button')))
         phonee.click()



         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             'body > app-root > app-register > div > div > div > app-detailed-step > form > div.modal-static-body > div:nth-child(2) > div > div.col-4.pr-3 > select')))
         phonee.click()

         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             'body > app-root > app-register > div > div > div > app-detailed-step > form > div.modal-static-body > div:nth-child(2) > div > div.col-4.pr-3 > select > option:nth-child(43)')))
         phonee.click()
         time.sleep(3)

         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             'body > app-root > app-register > div > div > div > app-detailed-step > form > div.modal-static-body > div:nth-child(2) > div > div.col-8.pl-0 > input')))

         phonee.send_keys(Keys.CONTROL,'a')
         phonee.send_keys(fnumbers[recount])
         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             '#agreement-link')))

         phonee.click()
         time.sleep(2)

         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             '#accept-button')))

         phonee.click()
         time.sleep(1)
         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             'body > app-root > app-register > div > div > div > app-detailed-step > form > div.modal-static-footer > button')))

         phonee.click()
         time.sleep(1)
         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             'body > app-root > app-register > div > div > div > app-msisdn-verification > form > div.modal-static-footer > div:nth-child(2) > button')))

         phonee.click()
         time.sleep(2)
         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             'body > app-root > app-register > div > div > div > app-msisdn-verification > div > div > a > i')))

         phonee.click()
         time.sleep(1)
         while (1):

             phonee = WebDriverWait(browser, 120).until(
                 EC.presence_of_element_located((By.CSS_SELECTOR,
                                                 'body > app-root > app-register > div > div > div > app-detailed-step > form > div.modal-static-body > div:nth-child(2) > div > div.col-8.pl-0 > input')))

             phonee.send_keys(Keys.CONTROL, 'a')
             phonee.send_keys(fnumbers[recount])
             time.sleep(1)
             phonee = WebDriverWait(browser, 120).until(
                 EC.presence_of_element_located((By.CSS_SELECTOR,
                                                 'body > app-root > app-register > div > div > div > app-detailed-step > form > div.modal-static-footer > button')))

             phonee.click()
             time.sleep(1)
             try:
              phonee = WebDriverWait(browser, 20).until(
                 EC.presence_of_element_located((By.CSS_SELECTOR,
                                                 'body > app-root > app-register > div > div > div > app-msisdn-verification > form > div.modal-static-footer > div:nth-child(2) > button')))

              phonee.click()
              time.sleep(2)
              phonee = WebDriverWait(browser, 120).until(
                 EC.presence_of_element_located((By.CSS_SELECTOR,
                                                 'body > app-root > app-register > div > div > div > app-msisdn-verification > div > div > a > i')))

              phonee.click()
              time.sleep(1)

              count = count + 1
              print(count)
              x = (len(fnumbers)) - 1
              if (recount < (x)):
                 recount = recount + 1
              else:
                 browser.get('chrome-extension://jnckhdjpjmofalipcflghpnmihgnnhee/control.html')
                 phonee = WebDriverWait(browser, 20).until(
                     EC.presence_of_element_located((By.CSS_SELECTOR,
                                                     "body > div > div > div > div > div > div.col-xs-4 > enable-switch > div > form > div")))
                 phonee.click()

                 time.sleep(2)
                 phonee = WebDriverWait(browser, 20).until(
                     EC.presence_of_element_located((By.CSS_SELECTOR,
                                                     "body > div > div > div > div > div > div.col-xs-4 > enable-switch > div > form > div")))
                 phonee.click()
                 recount = 0


             except Exception as  e:

                 browser.delete_all_cookies()
                 browser.get('chrome-extension://jnckhdjpjmofalipcflghpnmihgnnhee/control.html')
                 phonee = WebDriverWait(browser, 20).until(
                     EC.presence_of_element_located((By.CSS_SELECTOR,
                                                     "body > div > div > div > div > div > div.col-xs-4 > enable-switch > div > form > div")))
                 phonee.click()

                 time.sleep(2)
                 phonee = WebDriverWait(browser, 20).until(
                     EC.presence_of_element_located((By.CSS_SELECTOR,
                                                     "body > div > div > div > div > div > div.col-xs-4 > enable-switch > div > form > div")))
                 phonee.click()
                 break




















  

      

      
      

     except Exception  as e:
       browser.delete_all_cookies()
       browser.get('chrome-extension://jnckhdjpjmofalipcflghpnmihgnnhee/control.html')
       phonee = WebDriverWait(browser, 20).until(
           EC.presence_of_element_located((By.CSS_SELECTOR,
                                           "body > div > div > div > div > div > div.col-xs-4 > enable-switch > div > form > div")))
       phonee.click()

       time.sleep(2)
       phonee = WebDriverWait(browser, 20).until(
           EC.presence_of_element_located((By.CSS_SELECTOR,
                                           "body > div > div > div > div > div > div.col-xs-4 > enable-switch > div > form > div")))
       phonee.click()

       pass
    



     

    
     
     
  
