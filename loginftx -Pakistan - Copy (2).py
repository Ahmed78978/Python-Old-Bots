from selenium import webdriver
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


options = webdriver.ChromeOptions()
#options.add_extension('extension_1_6_6_0.crx')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
mobile_emulation = {"deviceName": "iPhone SE"}
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
#options.add_experimental_option("mobileEmulation", mobile_emulation)
count=0
recount=0
while(1):
 while(1):  
  numb="0123456789"
  browser = webdriver.Chrome(options=options, desired_capabilities=capa)
  url='https://ftx.com/profile'
  strr=["099"],random.choices(numb,k=1),["-4"],random.choices(numb,k=1),random.choices(numb,k=1),random.choices(numb,k=1)
  
  yo=convertTuple(strr)
  
  
  rt=url.replace("0995-4521",yo)
  
  

  
    
    
  
  

  fnumbers=["+923324978172","+923341597500","+923341597700","+923341597900","+923341598100","+923341598300","+923341598500","+923341598700","+923341598900","+923341599100","+923341599300","+923341599500","+923341599700","+923341599900","+923345740100","+923345740300","+923345740500","+923345740700","+923345740900","+923345741100","+923345741300","+923345741500","+923345741700","+923345741900","+923345742100","+923324978190","+923341597501","+923341597701","+923341597901","+923341598101","+923341598301","+923341598501","+923341598701","+923341598901","+923341599101","+923341599301","+923341599501","+923341599701","+923341599901","+923345740101","+923345740301","+923345740501","+923345740701","+923345740901","+923345741101","+923345741301","+923345741501","+923345741701","+923345741901","+923345742101","+923324978217","+923341597502","+923341597702","+923341597902","+923341598102","+923341598302","+923341598502","+923341598702","+923341598902","+923341599102","+923341599302","+923341599502","+923341599702","+923341599902","+923345740102","+923345740302","+923345740502","+923345740702","+923345740902","+923345741102","+923345741302","+923345741502","+923345741702","+923345741902","+923345742102","+923324978225","+923341597503","+923341597703","+923341597903","+923341598103","+923341598303","+923341598503","+923341598703","+923341598903","+923341599103","+923341599303","+923341599503","+923341599703","+923341599903","+923345740103","+923345740303","+923345740503","+923345740703","+923345740903","+923345741103","+923345741303","+923345741503","+923345741703","+923345741903","+923345742103"];
                                                                                                                                                                                                                                                                                                                


  numbers=[]
  #for x  in range(len(fnumbers)):
  # c=fnumbers[x]
   
  # rwithout=c.replace("+880","")
 #  numbers.append(rwithout)
  #time.sleep(8)
  p = browser.current_window_handle

#get first child window
  chwd = browser.window_handles
  
  if (len(chwd)>=2):

   browser.switch_to.window(chwd[1])
 
   browser.close()
   browser.switch_to.window(chwd[0])
  #time.sleep(5)
 # usernas = WebDriverWait(browser, 120).until(
 #   EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Log in to rider, driver, and delivery sites"]')))
 # usernas.click()
 # time.sleep(20)
 # try:
  # usernasp = WebDriverWait(browser, 120).until(
  #   EC.presence_of_element_located((By.XPATH, '//li[@class="gu bl ij b8"]')))
   #usernasp.click()
   #usernasp = WebDriverWait(browser, 120).until(
   #  EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div/div[6]/section/div/div/div/div/div[5]/a')))
   #usernasp.click()
 
   #print("signin clciked")
 
  #except NoSuchElementException:
 #   browser.close()
 #   break
 
  #time.sleep(10)
  #usernas = WebDriverWait(browser, 120).until(
     #EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Log in to rider, driver, and delivery sites"]')))
  #browser.execute_script("window.stop();")
  
  #usernas.click()
  #time.sleep(10)
  #try:
    #usernasp =browser.find_element_By_xpath('//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div/div[6]/section/div/div/div/div/div[3]/a')
    #usernasp.click()
   
  #  print("signin clciked")
  #  time.sleep(20)
   # phone = browser.find_element_By_xpath('//*[@id="answerForm"]/div[1]/div/div[1]/div/div[1]/div/div/select')
#ph one = browser.find_element_By_class_name('hwid-input hwid-input-pwd')
    #phone.click() 
  #except NoSuchElementException:
  #   browser.close()
  #   break
  while(1):
   
   #userna = WebDriverWait(browser, 30).until(
    #  EC.presence_of_element_located((By.XPATH, '//*[@id="answerForm"]/div[1]/div/div[1]/div/div[1]/div/div/select/option[198]')))
  # userna.click()
    #phone = WebDriverWait(browser, 120).until(
     # EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button')))
   #phone = browser.find_element_By_class_name('hwid-input hwid-input-pwd')
    #phone.click()
    browser.get((url))
    time.sleep(5)
    phonee = WebDriverWait(browser, 120).until(
       EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/main/div/button')))
    
    phonee.click()
    time.sleep(3)
    usernap = WebDriverWait(browser, 120).until(
         EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
   
    usernap.send_keys(usernameStr)
    
    usernap = WebDriverWait(browser, 120).until(
         EC.presence_of_element_located((By.XPATH, '//*[@id=""]'))) 
 
  
    usernap.send_keys(Str)
    #time.sleep(5)
    #phone = WebDriverWait(browser, 120).until(
     # EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[3]/form/div/div/div[8]/button')))
    #phone.click()
    #time.sleep(3)
    #phonesp = WebDriverWait(browser, 120).until(
    #  EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div[3]/div/div[3]/button[1]')))
  #  phonesp.click()
    while(1):
     time.sleep(5)
     phones = WebDriverWait(browser, 120).until(
       EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[2]/div/main/div/div[3]/div/div[3]/div[1]')))
     phones.click()
     time.sleep(3)
     phonesp = WebDriverWait(browser, 120).until(
       EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[2]/div/main/div/div[3]/div/div[3]/div[2]/div/div/div/div[2]/div/div[3]/button')))
     phonesp.click()
     time.sleep(10)
     try:
      usernasp = browser.find_element(By.XPATH,( '/html/body/div[6]/div[3]/div/div/div[2]/div/div[3]/label/span[1]/span[1]/input'))
      usernap.click()
      time.sleep(5)
      phonespp = WebDriverWait(browser, 120).until(
        EC.presence_of_element_located((By.XPATH,'/html/body/div[6]/div[3]/div/div/div[3]/button')))
      phonespp.click()
      time.sleep(5)
      phonespp = WebDriverWait(browser, 120).until(
        EC.presence_of_element_located((By.XPATH,'/html/body/div[6]/div[3]/div/div/div/div[3]/button[2]')))
      phonespp.click()
     except NoSuchElementException:
      print("exception ayatha")


     usernap = WebDriverWait(browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '//input[@class="PhoneInputInput"]')))   
     usernap.send_keys(fnumbers[recount])
     time.sleep(3)
     phonespp = WebDriverWait(browser, 120).until(
       EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div[3]/form/div[3]/button[2]')))
     phonespp.click()
     
     time.sleep(10)
     try:
       usernasp = browser.find_element(By.XPATH,( '/html/body/div[5]/div[3]/form/div[2]/div/div/div/input'))
       #usernasp.click()
       #usernasp = WebDriverWait(browser, 120).until(
        # EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div/div[6]/section/div/div/div/div/div[5]/a')))
      # usernasp.click()
 
       
     except (NoSuchElementException,TimeoutException):
      print("wait")
      time.sleep(160)
      browser.get((url))
      
     count=count+1
     if(recount<9):
         recount=recount+1
     else:
      recount=0
     print(count)
     time.sleep(65)
     browser.get((url))
     time.sleep(10)
     
     
  
