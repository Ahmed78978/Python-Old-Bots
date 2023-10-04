from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import string
import random
import time
import os
letters = string.ascii_lowercase

options = webdriver.ChromeOptions()
options.add_argument('--load-extension=D:\\autologinbot-master\\UltraSur')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--log-level=3')
while(1):
  try:
   browser = webdriver.Chrome(options=options)
   break
  except Exception  as e:
    pass
number='+8801401791995'
urll='https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&prevRID=XH5TGFNQ8J0EK09Y9PGJ&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0'
count = 0
file_name = os.path.basename(os.path.abspath(__file__))
filee=(os.path.splitext(file_name)[0]+".txt")
try:
    f = open(filee , 'w+')
except Exception as  a :
 print("file not found")
for line in f:
    if  number+"|" in line: 
        url=line 
        url = url.split("|")
        if(url[1]  is None):
         print("Link not  found")
        else:
         urll=url[1]

time.sleep(30)
while(1):
  try:
      browser.get(urll)
      break
  except:
     pass
# fill in username and hit the next button


#get first child window







try:
    username =WebDriverWait(browser, 20).until(
      EC.presence_of_element_located((By.ID, 'ap_customer_name')))
    username.send_keys(random.choices(string.ascii_lowercase, k=10))

    phone = browser.find_element(By.ID, 'ap_email')
    phone.send_keys(number)
    
    
       
        

    passs = random.choices(string.ascii_lowercase, k=10)

    passwo = browser.find_element(By.ID, 'ap_')
    passwo.send_keys(passs)

    passwo = browser.find_element(By.NAME, 'Check')
    passwo.send_keys(passs)

    nextButton = browser.find_element(By.ID, 'continue')
    nextButton.click()
    resend = WebDriverWait(browser, 580).until(
        EC.presence_of_element_located((By.ID, "auth-resend-code-link")))
    # resend =browser.find_element(By.ID,'auth-resend-form')
    urll=browser.current_url
    strr = number+"|" + browser.current_url
    f.write('\n')
    f.write(strr)
    f.close()

except Exception  as  e:
    print("link existed")
    f.close()
    print("yo")
    
    
       
        
while(1):
 time.sleep(65)
 try:

 
# wait for transition then continue to fill items
  resend = WebDriverWait(browser, 120).until(
    EC.presence_of_element_located((By.ID, "auth-resend-code-link")))

 
  resend.click()
  count=count+1
  print(count)
 except Exception as e:
    browser.get(urll)
 if count>=35:
   browser.quit()
   break
 
