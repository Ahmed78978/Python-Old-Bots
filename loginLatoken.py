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
usernameStr=['zahidkamal78978@gmail.com','zahid60@gmail.com','78978@gmail.com']

Str = ''



mobile_emulation = {"deviceName": "iPhone SE"}
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
#options.add_experimental_option("mobileEmulation", mobile_emulation)
count=0
recount=0
while(1):
 while(1):  
  numb="0123456789"
  
  url='https://latoken.com/exchange/USDT?do=login'


  

  
    
    
  
  

  fnumbers=["3324974902","3358079281","3367956840","3368634399","3368988235","3369522534","3370335881","3370745103","3324974923","3358366138","3367947513","3368634390","3368988202","3369521468","3370335878","3370743891","3324974951","3358718461","3367936495","3368628137","3368988201","3369515080","3370335872","3370741263","3324975036","3359085530","3367935506","3368621483","3368988185","3369512768","3370335870","3370738516","3324975069","3362044735","3367934492","3368619838","3368988168","3369508629","3370335864","3370736987","3324975071","3362504974","3367931638","3368616682","3368988148","3369507859","3370335855","3370733949","3324975199","3362533626","3367927215","3368616068","3368988139","3369504035","3370335854","3370728513","3324975255","3363614860","3367922773","3368614772","3368988134","3369504027","3370335847","3370727554","3324975273","3363615334","3367922701","3368609900","3368988132","3369503623","3370335841","3370726763","3324975285","3363615973","3367922694","3368609643","3368988122","3369498225","3370335840","3370724014","3324975292","3364971453","3367922046","3368608099","3368988104","3369493155","3370334532","3370720213","3324975299","3366738467","3367922041","3368608093","3368988097","3369491255","3370334528","3370719802","3324975317","3302362973","3367922039","3368608074","3368988096","3369487962","3370334527","3370717740","3324975335","3302367094","3367922035","3368607540","3368988093","3369487784","3370334526","3370714751","3324975428","3302387664","3367921546","3368606598","3368988058","3369487210","3370334516","3370711734","3324975429","3302388127","3367920816","3368604798","3368988031","3369483443","3370334513","3370711672","3324975469","3302589975","3367920812","3368604797","3368988029","3369479011","3370334508","3370711570","3324975516","3303453117","3367916878","3368604796","3368988016","3369476427","3370334398","3370711506","3324975583","3303482890","3367915870","3368604794","3368988014","3369471875","3370334386","3370711233","3324975650","3303877823","3367914558","3368604271","3368987996","3369471802","3370334381","3370710554","3324975731","3304020302","3367914495","3368603797","3368987989","3369471614","3370334379","3370698768","3324975738","3304020320","3367911259","3368603207","3368987986","3369471349","3370334378","3370698250","3324975741","3304689699","3367909642","3368602263","3368987985","3369470168","3370334374","3370698249","3324975766","3304766571","3367909509","3368601702","3368987976","3369465875","3370334369","3370698244","3324975860","3304915933","3367909485","3368575532","3368987974","3369464742","3370334328","3370696523","3324974299","3310156215","3368060237","3368670587","3368988458","3369574568","3370338067","3370771209","3324974310","3314385265","3368059750","3368670488","3368988454","3369572855","3370338065","3370771132","3324974328","3314418195","3368059184","3368669489","3368988439","3369571599","3370337850","3370770693","3359115878","3359115083","3359114637","3359114395","3359114352","3359114307","3359112784","3359105219","3359105217","3359104168","3359104135","3324976235","3367904397","3368528280","3368987929","3369428197","3369981951","3370661498","3378069513","3324976265","3367904052","3368526438","3368987928","3369426592","3369973584","3370660930","3378069514","3324976299","3367903741","3368526429","3368987923","3369425344","3369972753","3370660537","3378069515"]
                                                                                                                                                                                                                                                                                                                
  mailcount=0

  numbers=[]
  while(1):
   
  
    browser = uc.Chrome(use_subprocess=True)
 



    browser.get((url))
    while(1):
        try:
            time.sleep(5)
            usernap = WebDriverWait(browser, 120).until(
                EC.presence_of_element_located((By.XPATH, '//button[@data-tid="head__btn__login"]')))
            usernap.click()
        except Exception as e:
            print(".")
        try:
            
            phonee = WebDriverWait(browser, 120).until(
                EC.presence_of_element_located((By.XPATH, '//button[@tabindex="-1"]')))

            phonee.click()
            time.sleep(1)
            phonee = browser.find_element(By.XPATH,'//input[@aria-invalid="false"][@autocomplete="off"]')
            phonee.send_keys(Keys.CONTROL + 'a')
          


            phonee.send_keys("+92")

            phonee.send_keys(Keys.RETURN)


            usernap = WebDriverWait(browser, 120).until(
                EC.presence_of_element_located((By.XPATH, '//input[@name="mobileNumber"]')))

            usernap.send_keys(fnumbers[recount])
            
            usernap = WebDriverWait(browser, 120).until(
                EC.presence_of_element_located((By.XPATH, '//button[@data-tid="button__signup"]')))
            usernap.click()
            time.sleep(2)
            usernap = WebDriverWait(browser, 120).until(
                EC.presence_of_element_located((By.XPATH, '//input[@name=""]')))
            usernap.send_keys("")
            
            usernap = WebDriverWait(browser, 120).until(
                EC.presence_of_element_located((By.XPATH, '//input[@name="Confirmation"]')))
            usernap.send_keys("")
            time.sleep(2)
            usernap = WebDriverWait(browser, 120).until(
                EC.presence_of_element_located((By.XPATH, '//button[@data-tid="button__continue"]')))
            usernap.click()
            time.sleep(10)

            browser.delete_all_cookies()
            browser.refresh()
            browser.delete_all_cookies()




        except  Exception as e:
            
            print("exception ayatha")
      
            browser.close()
            break

        count = count + 1
        if (recount < (len(fnumbers) - 1)):
            recount = recount + 1
        else:
            recount = 0
        print(count)
        time.sleep(5)

     
     
     
     
  