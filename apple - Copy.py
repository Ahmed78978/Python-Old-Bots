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


options = webdriver.ChromeOptions()
#options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')
options.add_argument("--disable-renderer-backgrounding")
options.add_argument("--disable-backgrounding-occluded-windows")
#options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')
options.add_argument('--load-extension=D:\\autologinbot-master\\Urbanvpn')



mobile_emulation = {"deviceName": "iPhone SE"}
#options.add_experimental_option("mobileEmulation", mobile_emulation)
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
#options.add_experimental_option("mobileEmulation", mobile_emulation)
count=0
recount=100
total=0
if __name__ == "__main__":
 while(1):
  if (total >= 10):

         break
  numb="0123456789"
  
  url='https://appleid.apple.com/account'
  fnumbers=["1958806497","1958807917","1958809852","1958816136","1958823809","1958825517","1958828057","1958829550","1958829581","1958830711","1958831428","1958834170","1958836407","1958838414","1958839066","1958843199","1958843922","1958844648","1958845751","1958851494","1958853319","1958854514","1958854538","1958857237","1958860233","1958865724","1958866934","1958867877","1958869710","1958871080","1958873876","1958877042","1958880709","1958881081","1958881404","1958892405","1958893040","1958893781","1958894384","1958895607","1958896625","1958896961","1958899698","1958899851","1958900011","1958900915","1958901143","1958901750","1958901912","1958902099","1958904489","1958906557","1958908850","1958909176","1958909662","1958909938","1958910608","1958910648","1958911232","1958911282","1958914709","1958915102","1958916518","1958918630","1958920650","1958920970","1958921166","1958922191","1958923129","1958924616","1958924766","1958926952","1958927655","1958929655","1958930849","1958932938","1958933932","1958937145","1958939748","1958940271","1958941666","1958942038","1958943563","1958944015","1958944949","1958945217","1958946671","1958949449","1958952582","1958953923","1958957551","1958958235","1958960296","1958963426","1958965918","1958969753","1958971046","1958971943","1958972589","1958974602","1958975947","1958976314","1958977521","1958980434","1958980684","1958981122","1958981417","1958981723","1958982874","1958983453","1958985116","1958986423","1958989828","1958994478","1958995798","1958998670","1962760288","1963115350","1969372813","1972348099","1974685329","1982763305","1984696322","1985254690","1990530942","1990626133","1958785142","1958812502","1958854733","1958858153","1958881410","1958902065","1958933571","1958934021","1958954142","1958968480","1958970426","1958977169","1958983912","1958990655","1958997398","1959004141","1959010884","1958916483","1958923226","1958929969","1958936712","1958943455","1958950198","1958956941","1958963683","1958745735","1958762701","1958885312","1958952093","1958856128","1958965805","1958816978","1958918955","1958801408","1958915531","1958800415","1958824518","1958924096","1958771679","1958793417","1424153345","1424156235","1424160177","1424162360","1424164229","1424168547","1424191681","1424192409","1424198507","1424200711","1424201282","1424202398","1424206218","1424217161","1424217587","1424219958","1424223253","1424224756","1424224889","1424229152","1424231706","1424238266","1424238646","1424238858","1424244685","1424248805","1424249308","1424252951","1424253620","1424258653","1424259969","1424263630","1424266014","1424268788","1424269771","1424276034","1424277152","1424278973","1424280130","1424282751","1424287913","1424288151","1424310845","1424312997","1424314475","1424317837","1424320583","1424322184","1424322725","1424323499"]

  mailcount=0

  numbers=[]




  while(1):
      try:
          if (total >= 10):

              break
          options = webdriver.ChromeOptions()
          # options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')
          options.add_argument("--disable-renderer-backgrounding")
          options.add_argument("--disable-backgrounding-occluded-windows")
          # options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')
          options.add_argument('--load-extension=D:\\autologinbot-master\\Urbanvpn')
          browser = webdriver.Chrome(options=options, desired_capabilities=capa,version_main=107)
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

          while (1):
              if (total >= 10):

                  break

              try:

                  browser.get(url)
                  #ft.generateMail()
                  #email = ft.getEmail()
                  inbox = TempMail.generateInbox()
                  print("Email Address: " + inbox.address)  # View output below

                  time.sleep(2)
                  import requests, time

                  key = 'sub_1M0ulICRwBwvt6ptsU5sJPCD'
                  phonee = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.XPATH, '//img[@alt="Image challenge"]')))
                  phonee = phonee.get_attribute('src')
                  myStr = str(phonee)
                  substring = "data:image/jpeg;base64,"
                  output_string = ""
                  str_list = myStr.split(substring)
                  for element in str_list:
                      output_string += element

                  print(output_string)

                  image_urls = [
                      output_string,
                  ]

                  data = {
                      'type': 'textcaptcha',
                      'image_data': image_urls,
                      'key': key,
                  }

                  job_id = requests.post('https://api.nopecha.com/', json=data).json()['data']
                  print('job_id', job_id)
                  d = 0

                  while True:
                      d += 1
                      time.sleep(1)
                      response = requests.get(f"https://api.nopecha.com/?id={job_id}&key={key}").json()
                      print(response)
                      if (d >= 5):
                          break
                      if 'data' in response:
                          break

                  phonee = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located(
                          (By.CSS_SELECTOR,
                           '#firstNameInput > div > idms-textbox > idms-error-wrapper > div > div > input')))

                  phonee.send_keys('')

                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.XPATH,
                                                      '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/full-name/div[2]/div/div/last-name-input/div/idms-textbox/idms-error-wrapper/div/div/input')))

                  usernap.send_keys('zahid')
                  time.sleep(2)
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.XPATH,
                                                      '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[2]/div/div/div[2]/div/div[3]/div/wc-birthday/div/div/div/div/masked-date/div/idms-error-wrapper/div/div/input')))
                  usernap.send_keys('22/08/1999')
                  time.sleep(2)
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.XPATH,
                                                      '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[2]/div/div/div[3]/div/div[1]/div/account-name/div/div/email-input/div/idms-textbox/idms-error-wrapper/div/div/input')))
                  usernap.send_keys(inbox.address)
                  time.sleep(2)

                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.XPATH,
                                                      '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[2]/div/div/div[3]/div/div[2]/div/new-/div/div/-input/div/input')))
                  usernap.send_keys("")
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.XPATH,
                                                      '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[2]/div/div/div[3]/div/div[2]/div/confirm-/div/div/confirm--input/div/idms-textbox/idms-error-wrapper/div/div/input')))
                  usernap.send_keys("")
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.XPATH,
                                                      '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[2]/div/div/div[4]/div/div/div/div/phone-number/div/div/div[1]/div/phone-input/div/idms-dropdown/div/idms-error-wrapper/div/div/select')))
                  usernap.click()
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.XPATH,
                                                      '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[2]/div/div/div[4]/div/div/div/div/phone-number/div/div/div[1]/div/phone-input/div/idms-dropdown/div/idms-error-wrapper/div/div/select/option[19]')))
                  usernap.click()
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.XPATH,
                                                      '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[2]/div/div/div[4]/div/div/div/div/phone-number/div/div/div[1]/div/phone-input/div/idms-textbox/idms-error-wrapper/div/div/input')))
                  usernap.send_keys(fnumbers[recount])
                  time.sleep(2)
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.XPATH,
                                                      '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[2]/div/div/div[6]/div/create-captcha/div/div/div/div/div[2]/div/div[1]/captcha-input/div/idms-textbox/idms-error-wrapper/div/div/input')))
                  usernap.send_keys(response['data'])
                  time.sleep(2)

                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.XPATH,
                                                      '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[3]/idms-toolbar/div/div/div/button')))
                  actions = ActionChains(browser)
                  actions.move_to_element(usernap)
                  actions.click()
                  actions.perform()
                  time.sleep(1)
                  while (1):

                      try:
                          usernap = WebDriverWait(browser, 10).until(
                              EC.presence_of_element_located((By.XPATH,
                                                              '/html/body/div[8]/div/div/div[1]/step-verify-code/idms-step/div/div/div/div[2]/div/div/div[2]/security-code/div/idms-error-wrapper/div/div/div/div[1]/input')))
                          break
                      except:
                          inbox = TempMail.generateInbox()
                          print("Email Address: " + inbox.address)  # View output below
                          usernap = WebDriverWait(browser, 120).until(
                              EC.presence_of_element_located((By.XPATH,
                                                              '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[2]/div/div/div[3]/div/div[1]/div/account-name/div/div/email-input/div/idms-textbox/idms-error-wrapper/div/div/input')))
                          usernap.send_keys(Keys.CONTROL,'a')
                          usernap.send_keys(inbox.address)
                          if (recount < (len(fnumbers) - 1)):
                              recount = recount + 1
                          else:
                              recount = 0
                          usernap = WebDriverWait(browser, 120).until(
                              EC.presence_of_element_located((By.XPATH,
                                                              '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[2]/div/div/div[4]/div/div/div/div/phone-number/div/div/div[1]/div/phone-input/div/idms-textbox/idms-error-wrapper/div/div/input')))
                          usernap.send_keys(Keys.CONTROL, 'a')
                          usernap.send_keys(fnumbers[recount])


                          phonee = WebDriverWait(browser, 120).until(
                              EC.presence_of_element_located((By.XPATH, '//img[@alt="Image challenge"]')))
                          phonee = phonee.get_attribute('src')
                          myStr = str(phonee)
                          substring = "data:image/jpeg;base64,"
                          output_string = ""
                          str_list = myStr.split(substring)
                          for element in str_list:
                              output_string += element

                          print(output_string)

                          image_urls = [
                              output_string,
                          ]

                          data = {
                              'type': 'textcaptcha',
                              'image_data': image_urls,
                              'key': key,
                          }

                          job_id = requests.post('https://api.nopecha.com/', json=data).json()['data']
                          print('job_id', job_id)
                          d = 0

                          while True:
                              d += 1
                              time.sleep(1)
                              response = requests.get(f"https://api.nopecha.com/?id={job_id}&key={key}").json()
                              print(response)
                              if (d >= 5):
                                  break
                              if 'data' in response:
                                  break
                          usernap = WebDriverWait(browser, 120).until(
                              EC.presence_of_element_located((By.XPATH,
                                                              '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[2]/div/div/div[6]/div/create-captcha/div/div/div/div/div[2]/div/div[1]/captcha-input/div/idms-textbox/idms-error-wrapper/div/div/input')))
                          usernap.send_keys(response['data'])
                          usernap = WebDriverWait(browser, 120).until(
                              EC.presence_of_element_located((By.XPATH,
                                                              '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[3]/idms-toolbar/div/div/div/button')))
                          actions = ActionChains(browser)
                          actions.move_to_element(usernap)
                          actions.click()
                          actions.perform()

                  emails = TempMail.getEmails(inbox)  # Returns list of Email objects





                  otp1 = re.findall("\d\d\d\d\d\d", str(emails))
                  print(otp1)

                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.XPATH,
                                                      '/html/body/div[8]/div/div/div[1]/step-verify-code/idms-step/div/div/div/div[2]/div/div/div[2]/security-code/div/idms-error-wrapper/div/div/div/div[1]/input')))
                  usernap.send_keys(otp1[1])

                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.XPATH,
                                                      '/html/body/div[8]/div/div/div[1]/step-verify-code/idms-step/div/div/div/div[3]/idms-toolbar/div/div[1]/div/button[1]')))
                  usernap.click()
                  c = 0
                  while (1):

                      usernap = WebDriverWait(browser, 50).until(
                          EC.presence_of_element_located((By.XPATH,
                                                          '/html/body/div[8]/div/div/step-verify-code/idms-step/div/div/div/div[2]/div/div/div[3]/button')))
                      usernap.click()
                      time.sleep(1)
                      usernap = WebDriverWait(browser, 120).until(
                          EC.presence_of_element_located((By.XPATH,
                                                          '/html/body/div[8]/div/div/step-verify-code/idms-step/div/div/div/div[2]/div/div/div[3]/options-popover/div/idms-popover/div/div/div/div/div/div[1]/div/button')))
                      usernap.click()
                      c += 1
                      if (c >= 10):
                          break
                      count = count + 1
                      if (recount < (len(fnumbers) - 1)):
                          recount = recount + 1
                      else:
                          recount = 0

                      print(count)

                      browser.delete_all_cookies()
                      if (count % 18 == 0):
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
                          inbox = TempMail.generateInbox()
                          break






              except  Exception as e:


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
                  inbox = TempMail.generateInbox()

                  if (recount < (len(fnumbers) - 1)):
                      recount = recount + 1
                  else:
                      recount = 0
                      total+=1
                      print(total)
                      if (total >= 10):
                          browser.quit()
                          break
      except:

          browser.quit()
          print('biggest exception')



   


     
      


     
     
     
     
  
