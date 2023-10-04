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


user = "inforipha@gmail.com"
gmail_pass = "hbyswscrqygdwnoc"
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

                # Print Sender, Subject, Body
                print("-"*50)  # To divide the messages
                print("From    : ", sender)
                print("Subject : ", subject)
                if(contain_body):
                    print("Body    : ", body.decode())
                    return body.decode()







mobile_emulation = {"deviceName": "iPhone SE"}
#options.add_experimental_option("mobileEmulation", mobile_emulation)
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
#options.add_experimental_option("mobileEmulation", mobile_emulation)
count=0
recount=0
total=0
mno=0
if __name__ == "__main__":
 while(1):

  numb="0123456789"
  if (total >= 10):

      break
  
  url='https://www.twilio.com/try-twilio'
  fnumbers=["1311511534","1311511535","1311511536","1311511537","1311511538","1311511539","1311511540","1311511541","1311511542","1311511543","1311511544","1311511545","1311511546","1311511547","1311511548","1311511549","1311511550","1311511551","1311511552","1311511553","1311511554","1311511555","1311511556","1311511557","1311511558","1311511559","1311511560","1311511561","1311511562","1311511563","1311511564","1311511565","1311511566","1311511568","1311511569","1311511570","1311511571","1311511572","1311511573","1311511574","1311511575","1311511576","1311511578","1311511581","1311511582","1311511583","1311511584","1311511585","1311511586","1311511587","1311511588","1311511589","1311511590","1311511591","1311511592","1311511593","1311511594","1311511595","1311511596","1311511597","1311511598","1311511599","1311511600","1311511601","1311511604","1311511605","1311511606","1311511607","1311511608","1311511609","1311511610","1311511611","1311511612","1311511613","1311511614","1311511616","1311511617","1311511618","1311511619","1311511620","1311511621","1311511622","1311511639","1311511646","1311511659","1311511670","1311511706","1311511710","1311511761","1311511778","1311511809","1311511810","1311511811","1311511812","1311511813","1311511814","1311511815","1311511816","1311511817","1311511818","1311511819","1311511820","1311511821","1311511822","1311511823","1311511824","1311511825","1311511826","1311511827","1311511828","1311511829","1311511830","1311511831","1311511833","1311511834","1311511835","1311511836","1311511837","1311511838","1311511840","1311511841","1311511842","1311511843","1311511844","1311511845","1311511846","1311511847","1311511848","1311511849","1311511850","1311511851","1311511852","1311511853","1311511854","1311511855","1311511856","1311511857","1311511858","1311511859","1311511860","1311511861","1311511862","1311511863","1311511864","1311511866","1311511867","1311511868","1311511869","1311511870","1311511871","1311511872","1311511873","1311511874","1311511875","1311511877","1311511878","1311511879","1311511880","1311511881","1311511882","1311511883","1311511884","1311511885","1311511886","1311511888","1311511889","1311511890","1311511891","1311511892","1311511893","1311511894","1311511902","1311511938","1311511944","1311511957","1311511982","1311511983","1311511985","1311511987","1311512003","1311512007","1311512013","1311512017","1311512019","1311512020","1311512021","1311512022","1311512023","1311512024","1311512026","1311512027","1311512028","1311512029","1311512030","1311512031","1311512032","1311512033","1311512034","1311512035","1311512036","1311512037","1311512038","1311512039","1311512041","1311512042","1311512043","1311512044","1311512045","1311512047","1311512048","1311512049","1311512050","1311512051","1311512052","1311512053","1311512054","1311512056","1311512057","1311512058","1311512059","1311512060","1311512061","1311512062","1311512063","1311512064","1311512065","1311512066","1311512067","1311512069","1311512070","1311512071","1311512072","1311512073","1311512074","1311512075","1311512076","1311512077","1311512078","1311512079","1311512080","1311512081","1311512082","1311512083","1311512084","1311512085","1311512086","1311512087","1311512088","1311512089","1311512090","1311512091","1311512092","1311512093","1311512094","1311512095","1311512096","1311512097","1311512098","1311512099","1311512100","1311512101","1311512103","1311512104","1311512105","1311512106","1311512107","1311512108","1311512110","1311512111","1311512112","1311512113","1311512114","1311512115","1311512116","1311512118","1311512120","1311512121","1311512123","1311512124","1311512125","1311512126","1311512127","1311512129","1311512130","1311512132","1311512133","1311512134","1311512135","1311512136","1311512137","1311512138","1311512139","1311512140","1311512141","1311512142","1311512143","1311512144","1311512145","1311512146","1311512147","1311512148","1311512149","1311512150","1311512151","1311512152","1311512153","1311512154","1311512155","1311512157","1311512158","1311512159","1311512160","1311512161","1311512162","1311512163","1311512164","1311512165","1311512166","1311512167","1311512168","1311512169","1311512170","1311512171","1311512172","1311512173","1311512174","1311512175","1311512176","1311512177","1311512178","1311512179","1311512180","1311512182","1311512183","1311512184","1311512185","1311512186","1311512187","1311512188","1311512189","1311512190","1311512191","1311512192","1311512194","1311512195","1311512196","1311512197","1311512198","1311512199","1311512200","1311512201","1311512202","1311512203","1311512204","1311512205","1311512206","1311512207","1311512208","1311512209","1311512210","1311512211","1311512212","1311512213","1311512214","1311512215","1311512216","1311512217","1311512218","1311512219","1311512220","1311512221","1311512222","1311512223","1311512224","1311512225","1311512226","1311512227","1311512229","1311512230","1311512231","1311512232","1311512233","1311512234","1311512235","1311512236","1311512237","1311512239","1311512240","1311512241","1311512247","1311512276","1311512306","1311512324","1311512328","1311512366","1311512367","1311512368","1311512369","1311512370","1311512371"]
  mailcount=0

  numbers=[]




  while(1):
      if (total >= 10):

          break
      try:
          options = webdriver.ChromeOptions()
          # options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')
          options.add_argument("--disable-renderer-backgrounding")
          options.add_argument("--disable-backgrounding-occluded-windows")
          # options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')
          options.add_argument('--load-extension=D:\\autologinbot-master\\Urbanvpn')
          browser = webdriver.Chrome(options=options, desired_capabilities=capa,version_main=111)
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

              try:

                  browser.get(url)


                  time.sleep(2)
                  import requests, time

                  key = 'sub_1MtbdYCRwBwvt6ptgYCIwY4U'

                  d = 0



                  phonee = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located(
                          (By.CSS_SELECTOR,
                           '#FirstName')))

                  phonee.send_keys('')

                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#LastName')))

                  usernap.send_keys('zahid')
                  time.sleep(2)
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#EmailAddr')))
                  usernap.send_keys(inb[mno])
                  time.sleep(2)
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#Passwd')))
                  usernap.send_keys('jamal@123J655737978978')
                  time.sleep(2)

                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#Tos')))
                  usernap.click()
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#signup-button')))
                  usernap.click()
                  time.sleep(10)
                  emails = read_email_from_gmail(1, True)
                  print(emails)

                  otp1 = re.findall("\d\d\d\d\d\d", str(emails))
                  print('otp: ')
                  print(otp1)

                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[2]/div/div/div[4]/div/div/div/div/phone-number/div/div/div[1]/div/phone-input/div/idms-dropdown/div/idms-error-wrapper/div/div/select')))
                  usernap.click()
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[2]/div/div/div[4]/div/div/div/div/phone-number/div/div/div[1]/div/phone-input/div/idms-dropdown/div/idms-error-wrapper/div/div/select/option[19]')))
                  usernap.click()
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[2]/div/div/div[4]/div/div/div/div/phone-number/div/div/div[1]/div/phone-input/div/idms-textbox/idms-error-wrapper/div/div/input')))
                  usernap.send_keys(fnumbers[recount])
                  time.sleep(2)
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[2]/div/div/div[6]/div/create-captcha/div/div/div/div/div[2]/div/div[1]/captcha-input/div/idms-textbox/idms-error-wrapper/div/div/input')))
                  usernap.send_keys(response['data'])
                  time.sleep(2)

                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[3]/idms-toolbar/div/div/div/button')))
                  actions = ActionChains(browser)
                  actions.move_to_element(usernap)
                  actions.click()
                  actions.perform()
                  time.sleep(1)
                  while (1):
                      if (total >= 10):

                          break

                      try:
                          usernap = WebDriverWait(browser, 20).until(
                              EC.presence_of_element_located((By.CSS_SELECTOR,
                                                              '/html/body/div[8]/div/div/div[1]/step-verify-code/idms-step/div/div/div/div[2]/div/div/div[2]/security-code/div/idms-error-wrapper/div/div/div/div[1]/input')))

                          break
                      except:

                          usernap = WebDriverWait(browser, 120).until(
                              EC.presence_of_element_located((By.CSS_SELECTOR,
                                                              '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[2]/div/div/div[3]/div/div[1]/div/account-name/div/div/email-input/div/idms-textbox/idms-error-wrapper/div/div/input')))
                          usernap.send_keys(Keys.CONTROL, 'a')
                          usernap.send_keys(inb)
                          if (recount < (len(fnumbers) - 1)):
                              recount = recount + 1
                          else:
                              recount = 0

                          usernap = WebDriverWait(browser, 120).until(
                              EC.presence_of_element_located((By.CSS_SELECTOR,
                                                              '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[2]/div/div/div[4]/div/div/div/div/phone-number/div/div/div[1]/div/phone-input/div/idms-textbox/idms-error-wrapper/div/div/input')))
                          usernap.send_keys(Keys.CONTROL, 'a')
                          usernap.send_keys(fnumbers[recount])

                          phonee = WebDriverWait(browser, 120).until(
                              EC.presence_of_element_located((By.CSS_SELECTOR, '//img[@alt="Image challenge"]')))
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
                              EC.presence_of_element_located((By.CSS_SELECTOR,
                                                              '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[2]/div/div/div[6]/div/create-captcha/div/div/div/div/div[2]/div/div[1]/captcha-input/div/idms-textbox/idms-error-wrapper/div/div/input')))
                          usernap.send_keys(Keys.CONTROL,'a')
                          usernap.send_keys(response['data'])
                          usernap = WebDriverWait(browser, 120).until(
                              EC.presence_of_element_located((By.CSS_SELECTOR,
                                                              '/html/body/div[2]/aid-web/div[2]/div/div/create-app/aid-create/idms-flow/div/div/div/idms-step/div/div/div/div[3]/idms-toolbar/div/div/div/button')))
                          actions = ActionChains(browser)
                          actions.move_to_element(usernap)
                          actions.click()
                          actions.perform()

                  time.sleep(10)
                  emails=read_email_from_gmail(1, True)





                  otp1 = re.findall("\d\d\d\d\d\d", str(emails))
                  print('otp: ')
                  print(otp1)

                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '/html/body/div[8]/div/div/div[1]/step-verify-code/idms-step/div/div/div/div[2]/div/div/div[2]/security-code/div/idms-error-wrapper/div/div/div/div[1]/input')))
                  usernap.send_keys(otp1[0])

                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '/html/body/div[8]/div/div/div[1]/step-verify-code/idms-step/div/div/div/div[3]/idms-toolbar/div/div[1]/div/button[1]')))
                  usernap.click()
                  try:
                      usernap = WebDriverWait(browser, 50).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          '/html/body/div[8]/div/div/step-verify-code/idms-step/div/div/div/div[2]/div/div/div[3]/button')))

                  except:
                      time.sleep(10)
                      emails = read_email_from_gmail(1, True)

                      otp1 = re.findall("\d\d\d\d\d\d", str(emails))
                      print('otp: ')
                      print(otp1)

                      usernap = WebDriverWait(browser, 120).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          '/html/body/div[8]/div/div/div[1]/step-verify-code/idms-step/div/div/div/div[2]/div/div/div[2]/security-code/div/idms-error-wrapper/div/div/div/div[1]/input')))
                      usernap.send_keys(otp1[0])

                      usernap = WebDriverWait(browser, 120).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          '/html/body/div[8]/div/div/div[1]/step-verify-code/idms-step/div/div/div/div[3]/idms-toolbar/div/div[1]/div/button[1]')))
                      usernap.click()



                  c = 0
                  while (1):
                      if (total >= 10):

                          break

                      usernap = WebDriverWait(browser, 50).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          '/html/body/div[8]/div/div/step-verify-code/idms-step/div/div/div/div[2]/div/div/div[3]/button')))
                      usernap.click()
                      time.sleep(1)
                      usernap = WebDriverWait(browser, 120).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          '/html/body/div[8]/div/div/step-verify-code/idms-step/div/div/div/div[2]/div/div/div[3]/options-popover/div/idms-popover/div/div/div/div/div/div[1]/div/button')))
                      usernap.click()
                      c += 1
                      #if (c >= 10):
                       #   break
                      count = count + 1


                      print(count)
                      print('NUmber: ',fnumbers[recount])


                      if (count % 11 == 0):
                          browser.delete_all_cookies()
                          if (recount < (len(fnumbers) - 1)):
                              recount = recount + 1
                          else:
                              recount = 0
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
                                  (By.CSS_SELECTOR, "/html/body/div/div/div[3]/div[2]/div/div[2]/div/ul/li[" + str(i) + "]")))
                          browser.execute_script("arguments[0].scrollIntoView(true);", ph);
                          ph.click()
                          print('country is: ' + str(i))

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
                          (By.CSS_SELECTOR, "/html/body/div/div/div[3]/div[2]/div/div[2]/div/ul/li[" + str(i) + "]")))
                  browser.execute_script("arguments[0].scrollIntoView(true);", ph);
                  ph.click()
                  print('country is: ' + str(i))


                  if (recount < (len(fnumbers) - 1)):
                      recount = recount + 1
                  else:
                      recount = 0

                      print(total)
                      if (total >= 10):
                          browser.quit()
                          break
      except:


          browser.quit()
          print(a)
          print('biggest exception')



   


     
      


     
     
     
     
  
