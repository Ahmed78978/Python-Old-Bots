from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import string
import random
import time
PROXY_STR = "151.106.17.123:1080"
select = ['3', '57', '12', '26', '49', '29', '6', '23', '34', '28', '2', '18', '41', '55', '33', '24', '19']

options = webdriver.ChromeOptions()
options.add_argument('--load-extension=D:\\autologinbot-master\\LOBBY\\Nope,D:\\autologinbot-master\\Urbanvpn')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
count = 0


while(1):

 browser = webdriver.Chrome(options=options)
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

         phonee.send_keys('sub_1LwQ8xCRwBwvt6ptFLAxJSSl')

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

 while(1):

  try:


   letters = string.ascii_lowercase
   usernameStr = ''
   Str = 'A'
   browser.get(('https://www.facebook.com/reg/'))
   while(1):
     try:
       try:
         phone = WebDriverWait(browser, 5).until(
             EC.presence_of_element_located((By.NAME, 'reg_email__')))
         break
       except:
           pass
       print('clicked')

       resen = WebDriverWait(browser, 5).until(
           EC.presence_of_element_located((By.XPATH,
                                           "/html/body/div[1]/div[2]/div[1]/div/div/div[3]/div/div[1]/label/input")))

       resen.click()




     except:
       pass

   # REGButton = browser.find_element_by_name('firstname')
   # REGButton.click()
   # fill in username and hit the next button
   names = ["Ford", "Volvo", "Liam", "Olivia", "Noah", "Emma", "Oliver", "Ava", "Elijah", "Charlotte", "William",
            "Sophia", "James", "Amelia", "Benjamin", "Isabella", "Lucas", "Mia", "Henry", "Evelyn", "Alex", "ander",
            "Harper"]
   numbers = ["+8801958540842", "+8801958540919", "+8801958540996", "+8801958541075", "+8801958541154",
              "+8801958541232", "+8801958541308", "+8801958541384", "+8801958541460", "+8801958541536",
              "+8801958653558", "+8801958655366", "+8801958657289", "+8801958657959", "+8801958666089",
              "+8801958666231", "+8801958666380", "+8801958666526", "+8801958666666", "+8801958666846",
              "+8801958667007", "+8801958667142", "+8801958667288", "+8801958667427", "+8801958667583",
              "+8801958667726", "+8801958667878", "+8801958668030", "+8801958668176", "+8801958668334",
              "+8801958668472", "+8801958668613", "+8801958668773", "+8801958668927", "+8801958669160",
              "+8801958669378", "+8801958669571", "+8801958669801", "+8801958670073", "+8801958670285",
              "+8801958670481", "+8801958670708", "+8801958670930", "+8801958549911", "+8801958550024",
              "+8801958550155", "+8801958550281", "+8801958550412", "+8801958550533", "+8801958550651",
              "+8801958550778", "+8801958550903", "+8801958551024", "+8801958551157", "+8801958551290",
              "+8801958551453"]

   username = WebDriverWait(browser, 120).until(
       EC.presence_of_element_located((By.NAME, 'firstname')))
   username.send_keys(Keys.CONTROL + 'a')
   username.send_keys(random.choices(names))

   username2 = WebDriverWait(browser, 120).until(
       EC.presence_of_element_located((By.NAME, 'lastname')))
   username2.send_keys(Keys.CONTROL + 'a')
   username2.send_keys(random.choices(names))

   num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
   pk = ['300', '301', '302', '303', '304', '305', '306', '307', '308', '309', '311', '312', '313', '314', '315', '320',
         '321', '322', '323', '324', '325', '330', '331', '332', '333', '334', '335', '336', '337', '340', '341', '342',
         '343', '344', '345', '346', '347']
   phone = WebDriverWait(browser, 120).until(
       EC.presence_of_element_located((By.NAME, 'reg_email__')))
   phone.send_keys(Keys.CONTROL + 'a')
   phone.send_keys('+92', random.choice(pk), random.choices(num, k=7))

   passs = random.choices(string.ascii_lowercase, k=10)

   passwo = WebDriverWait(browser, 120).until(
       EC.presence_of_element_located((By.NAME, 'reg_passwd__')))
   passwo.send_keys(Keys.CONTROL + 'a')
   passwo.send_keys(passs)

   bir = WebDriverWait(browser, 120).until(
       EC.presence_of_element_located((By.NAME, 'birthday_year')))
   # bir.send_keys(Keys.CONTROL + 'a')
   bir.send_keys('1999')

   bir = WebDriverWait(browser, 120).until(
       EC.presence_of_element_located((By.NAME, 'birthday_day')))
   bir.send_keys(random.randint(1, 30))

   nextButton = WebDriverWait(browser, 120).until(
       EC.presence_of_element_located((By.XPATH, "//input[@value='1']")))
   nextButton.click()
   nextButton = WebDriverWait(browser, 120).until(
       EC.presence_of_element_located((By.NAME, "websubmit")))
   nextButton.click()
   time.sleep(10)


   resend = WebDriverWait(browser, 50).until(
       EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Continue']")))

   resend.click()


   while(1):
       try:


           resen = WebDriverWait(browser, 120).until(
               EC.presence_of_element_located((By.CSS_SELECTOR,
                                               "#scrollview > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x1t2pt76.x193iq5w.xl56j7k.x78zum5.x1qjc9v5 > div > div > div.xh8yej3.x14lw9ws > div > div > div > div > div > div > div > div:nth-child(3) > div > div > div")))

           resen.click()

           bir = WebDriverWait(browser, 5).until(
               EC.presence_of_element_located((By.NAME, 'contactpoint')))

           break
       except:
           pass







   bir = WebDriverWait(browser, 120).until(
       EC.presence_of_element_located((By.NAME, 'contactpoint')))

   bir.send_keys(random.choice(numbers))

   time.sleep(1)
   biro = WebDriverWait(browser, 120).until(
       EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Send Login Code']")))
   biro.click()

   while (1):
       c = 0
       while (1):
           try:

               birp = WebDriverWait(browser, 10).until(
                   EC.presence_of_element_located((By.XPATH, "//*[text()='Resend confirmation code']")))

               birp.click()
               time.sleep(0.6)
               c += 1
               if (c >= 5):
                   break
               time.sleep(2)
           except:
               print(A)

       time.sleep(2)
       birpo = WebDriverWait(browser, 120).until(
           EC.presence_of_element_located((By.CSS_SELECTOR,
                                           "#scrollview > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x1t2pt76.x193iq5w.xl56j7k.x78zum5.x1qjc9v5 > div > div > div.xh8yej3.x14lw9ws > div > div > div > div > div > div > div > div:nth-child(4) > div > div:nth-child(1) > div.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x1ypdohk.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x87ps6o.x1lku1pv.x1a2a7pz.x9f619.x3nfvp2.xdt5ytf.xl56j7k.x1n2onr6.xh8yej3 > div")))
       birpo.click()

       bir = WebDriverWait(browser, 20).until(
           EC.presence_of_element_located((By.NAME, 'contactpoint')))

       bir.send_keys(random.choice(numbers))
       biro = WebDriverWait(browser, 120).until(
           EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Send Login Code']")))
       biro.click()

       count = count + 1
       print(count)
  except:

      browser.delete_all_cookies()
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

      pass



  # wait for transition then continue to fill items


 

