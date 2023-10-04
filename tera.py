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
from selenium.webdriver.common.action_chains import ActionChains
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
options.add_argument('--load-extension=D:\\autologinbot-master\\LOBBY\\Nope,,D:\\autologinbot-master\\Urbanvpn')

#options.add_argument('--load-extension=D:\\autologinbot-master\\LOBBY\\Nope')
mobile_emulation = {"deviceName": "iPhone SE"}
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
#options.add_experimental_option("mobileEmulation", mobile_emulation)
count=1
recount=0
#time.sleep(1000)
while(1):
 while(1):  
  numb="0123456789"
 
  url='https://www.terabox.com'

  

  
    
    
  
  

  fnumbers=["1994856942","1999561479","1999597042","1958544372","1958544676","1958544753","1958544835","1958544912","1958544988","1958545064","1958545140","1958545216","1958545292","1958545368","1958545444","1958545520","1958545597","1958545673","1958545749","1958545825","1958545902","1958545978","1958546054","1958546130","1958546206","1958546282","1958546358","1958546434","1958546510","1958546589","1958652066","1958652146","1958652231","1958652308","1958652384","1958652460","1958652537","1958652615","1958652691","1958652767","1958652844","1958652920","1958652996","1958653072","1958653148","1958540082","1958540173","1958540262","1958540345","1958540439","1958540527","1958540616"]

  numbers=[]

  while (1):
    try:
      options = uc.ChromeOptions()

      # options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')
      options.add_argument("--disable-renderer-backgrounding")

      options.add_argument("--disable-backgrounding-occluded-windows")
      options.add_argument('--load-extension=D:\\autologinbot-master\\LOBBY\\Nope,D:\\autologinbot-master\\Urbanvpn')
      browser = uc.Chrome(options=options, use_subprocess=True, version_main=107,desired_capabilities=capa)
      while (1):
          try:
              browser.get('chrome-extension://dlnlfkobboboecjlnfnaabpfoegcgnkn/popup.html')
              time.sleep(3)
              phonee = WebDriverWait(browser, 120).until(
                  EC.presence_of_element_located((By.CSS_SELECTOR,
                                                  '#edit_key')))
              phonee.click()
              phonee = WebDriverWait(browser, 120).until(
                  EC.presence_of_element_located((By.CSS_SELECTOR,
                                                  '#app_frame > div:nth-child(5) > div.plan_info_container > input')))

              phonee.send_keys(Keys.CONTROL, 'a')

              phonee.send_keys('sub_1M0ulICRwBwvt6ptsU5sJPCD')

              time.sleep(2)
              break
          except:
              pass

      i = random.randint(2, 57)
      browser.get("chrome-extension://ecokmenakcanpnkbgifdiacoapdmhdjf/popup/index.html#/welcome-consent")
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

          browser.get(url)



          try:

              while (1):

                  time.sleep(1)
                  phonee = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      'body > div.login-home-center > div > div.bg > div.login-login-index > div > div.login-card-box > div > div.login-register-list > div > div:nth-child(2)')))
                  action = ActionChains(browser)
                  action.move_to_element(phonee)
                  action.click()
                  action.perform()
                  time.sleep(1)


                  phonee = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#vs1__combobox > div.vs__selected-options > input')))
                  phonee.send_keys('+880')
                  time.sleep(0.5)
                  phonee = WebDriverWait(browser, 30).until(
                      EC.presence_of_element_located((By.XPATH,
                                                      (
                                                          "//*[contains(text(), 'BD +880')]"))))
                  phonee.click()

                  phonee = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      'body > div.login-home-center > div > div.bg > div.login-login-index > div > div.login-card-box > div > div:nth-child(2) > div:nth-child(3) > div > div > div.components-login-center-input-phone > div > div.input-contain > input')))

                  phonee.send_keys(fnumbers[recount])
                  time.sleep(0.5)
                  c=0
                  while(1):
                   try:

                       phonee = WebDriverWait(browser, 5).until(
                           EC.presence_of_element_located((By.XPATH,
                                                           (
                                                               "//*[contains(text(), ' Send code ')]")))).click()
                       time.sleep(10)




                   except:
                       break






                  browser.delete_all_cookies()
                  browser.get(url)
                  if(count%10==0):
                      count+=1
                      print(a)



                  count = count + 1
                  x = (len(fnumbers)) - 1
                  if (recount < (x)):
                      recount = recount + 1
                  else:
                      recount = 0
                  print(count)
          except:
              print(a)
              i = random.randint(2, 57)
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
              browser.get(url)
























    except:
        print(a)

        i = random.randint(2, 57)
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











    



     

    
     
     
  
