import undetected_chromedriver.v2 as webdriver
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





options = webdriver.ChromeOptions()
#options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')
options.add_argument("--disable-renderer-backgrounding")
options.add_argument("--disable-backgrounding-occluded-windows")
#options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')
options.add_argument('--load-extension=D:\\autologinbot-master\\LOBBY\\Nope,D:\\autologinbot-master\\Urbanvpn')


mobile_emulation = {"deviceName": "iPhone SE"}
#options.add_experimental_option("mobileEmulation", mobile_emulation)
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
#options.add_experimental_option("mobileEmulation", mobile_emulation)
count=0
recount=0
while(1):
 while(1):  
  numb="0123456789"
  
  url='https://www.twitch.tv'
  fnumbers=["1916889755","1920413837","1921345577","1923334295","1924289356","1924307128","1927157292","1927598291","1928192905","1928194437","1928658268","1930929385","1931959044","1932791385","1933056671","1933618314","1933622795","1933859005","1934971022","1935143103","1935723616","1937358241","1937518530","1938726556","1938730391","1939776273","1940546179","1942796257","1943217727","1944021501","1944085137","1944967363","1945089107","1946188839","1947331765","1948387863","1948412781","1948642997","1948766384","1948949081","1952856047","1954571900","1957535524","1960453409","1970652359","1975698537","1975846294","1976038630","1976460618","1977508523","1984931727","1994856942","1999561479","1999597042","1958544372","1958544676","1958544753","1958544835","1958544912","1958544988","1958545064","1958545140","1958545216","1958545292","1958545368","1958545444","1958545520","1958545597","1958545673","1958545749","1958545825","1958545902","1958545978","1958546054","1958546130","1958546206","1958546282","1958546358","1958546434","1958546510","1958546589","1958652066","1958652146","1958652231","1958652308","1958652384","1958652460","1958652537","1958652615","1958652691","1958652767","1958652844","1958652920","1958652996","1958653072","1958653148","1958540082","1958540173","1958540262","1958540345","1958540439","1958540527","1958540616","1958540700","1958540788","1958540871","1958540948","1958541025","1958541106","1958541184","1958541261","1958541337","1958541413","1958541489","1958541566","1958654301","1958656123","1958657565","1958666001","1958666141","1958666282","1958666437","1958666574","1958666742","1958666894","1958667048","1958667186","1958667348","1958667490","1958667633","1958667789","1958667935","1958668074","1958668228","1958668387","1958668525","1958668692","1958668832","1958668981","1958669244","1958669454","1958669659","1958669880","1958670152","1958670361","1958670553","1958670792","1958549824","1958549952","1958550074","1958550202","1958550333","1958550453","1958550581","1958550705","1958550829","1958550946","1958551077","1958551203","1958551353","1958551499","1958551626","1958551764","1401791964","1400413201","1911893759","1921369924","1922092761","1924288808","1928658033","1929846579","1931553847","1931601763","1932134329","1934640280","1934829638","1935072003","1935228810","1935723896","1936323002","1937022329","1938051115","1939097694","1940093476","1940617243","1942796251","1946579443","1947154271","1947968749","1948558500","1948694928","1949090783","1951010586","1951014990","1951312764","1952298282","1952579833","1953019055","1954210596","1967964738","1970890567","1973016171","1973581246","1973985543","1974805641","1978941276","1987410134","1990908508","1958544647","1958544724","1958544801","1958544883","1958544959","1958545035","1958545111","1958545187","1958545263","1958545339","1958545415","1958545491","1958545568","1958545644","1958545720","1958545796","1958545873","1958545949","1958546025","1958546101","1958546177","1958546253","1958546329","1958546405","1958546481","1958546559","1958652037","1958652116","1958652196","1958652279","1958652355","1958652431","1958652508","1958652586","1958652662","1958652738","1958652815","1958652891","1958652967","1958653043","1958653119","1958653195","1958540052","1958540140","1958540229","1958540315","1958540404","1958540493","1958540585","1958540669","1958540757","1958540842","1958540919","1958540996","1958541075","1958541154","1958541232","1958541308","1958541384","1958541460","1958541536","1958653558","1958655366","1958657289","1958657959","1958666089","1958666231","1958666380","1958666526","1958666666","1958666846","1958667007","1958667142","1958667288","1958667427","1958667583","1958667726","1958667878","1958668030","1958668176","1958668334","1958668472","1958668613","1958668773","1958668927","1958669160","1958669378","1958669571","1958669801","1958670073","1958670285","1958670481","1958670708","1958670930","1958549911","1958550024","1958550155","1958550281","1958550412","1958550533","1958550651","1958550778","1958550903","1958551024","1958551157","1958551290","1958551453"]
  mailcount=0

  numbers=[]
  browser = webdriver.Chrome(options=options, desired_capabilities=capa,use_subprocess=True)
  browser.get('chrome-extension://dlnlfkobboboecjlnfnaabpfoegcgnkn/popup.html')

  time.sleep(3)
  phonee = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located((By.CSS_SELECTOR,
                                      '#key')))
  phonee.send_keys(Keys.CONTROL, 'a')

  phonee.send_keys('sub_1LwQ8xCRwBwvt6ptFLAxJSSl')
  time.sleep(5)
  i = random.randint(2, 57)
  browser.get("chrome-extension://ecokmenakcanpnkbgifdiacoapdmhdjf/popup/index.html#/welcome-consent")

  WebDriverWait(browser, 120).until(
      EC.presence_of_element_located(
          (By.CSS_SELECTOR,
           "body > div > div > div.simple_layout__body > div > div > div > button.button_pink.agreement_agree"))).click()
  WebDriverWait(browser, 20).until(
      EC.presence_of_element_located((By.CSS_SELECTOR,
                                      "body > div > div > div.main_layout__body > div.location-box > div > div:nth-child(1) > input"))).click()
  time.sleep(2)
  ph = WebDriverWait(browser, 20).until(
      EC.presence_of_element_located(
          (By.XPATH, "/html/body/div/div/div[3]/div[2]/div/div[2]/div/ul/li[" + str(i) + "]")))
  browser.execute_script("arguments[0].scrollIntoView(true);", ph);
  ph.click()
  time.sleep(2)
  print('country is: ' + str(i))
  i = 0
 
  while(1):
   
  




    browser.get(url)


    try:  
     time.sleep(2)
     phonee = WebDriverWait(browser, 120).until(
       EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > div.Layout-sc-nxg1ff-0.bSuLAT > nav > div > div.Layout-sc-nxg1ff-0.hWJFll > div.Layout-sc-nxg1ff-0.jwASrz > div > div.Layout-sc-nxg1ff-0.iLhppl.anon-user > div:nth-child(2) > button')))
    
     phonee.click()

     usernap = WebDriverWait(browser, 120).until(
         EC.presence_of_element_located((By.CSS_SELECTOR, '#signup-username')))
   
     usernap.send_keys('fdga3r4334556',random.choices(string.ascii_lowercase, k=3))
     time.sleep(2)
     usernap = WebDriverWait(browser, 120).until(
         EC.presence_of_element_located((By.CSS_SELECTOR, '#-input')))
     usernap.send_keys("^%%&#&(&*(&*")
     time.sleep(2)
     usernap = WebDriverWait(browser, 120).until(
         EC.presence_of_element_located((By.CSS_SELECTOR, '#-input-confirmation')))
     usernap.send_keys("^%%&#&(&*(&*")
     time.sleep(2)
     usernap = WebDriverWait(browser, 120).until(
         EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.ReactModalPortal > div > div > div > div > div > div.Layout-sc-nxg1ff-0.gmqBFP > div > div > div.Layout-sc-nxg1ff-0.gZaqky > form > div > div:nth-child(3) > div > div.Layout-sc-nxg1ff-0.jREsSm > div:nth-child(1) > div > input')))
     usernap.send_keys('22')
     time.sleep(2)
     usernap = WebDriverWait(browser, 120).until(
         EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.ReactModalPortal > div > div > div > div > div > div.Layout-sc-nxg1ff-0.gmqBFP > div > div > div.Layout-sc-nxg1ff-0.gZaqky > form > div > div:nth-child(3) > div > div.Layout-sc-nxg1ff-0.jREsSm > div.Layout-sc-nxg1ff-0.fQeqDH.InjectLayout-sc-588ddc-0.bupOpr > select > option:nth-child(9)')))
     usernap.click()
     usernap = WebDriverWait(browser, 120).until(
         EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.ReactModalPortal > div > div > div > div > div > div.Layout-sc-nxg1ff-0.gmqBFP > div > div > div.Layout-sc-nxg1ff-0.gZaqky > form > div > div:nth-child(3) > div > div.Layout-sc-nxg1ff-0.jREsSm > div.Layout-sc-nxg1ff-0.InjectLayout-sc-588ddc-0.birthday-picker__input.bupOpr > div > input')))
     usernap.send_keys('1999')
     time.sleep(1)
     usernap = WebDriverWait(browser, 120).until(
         EC.presence_of_element_located((By.CSS_SELECTOR,
                                         'body > div.ReactModalPortal > div > div > div > div > div > div.Layout-sc-nxg1ff-0.gmqBFP > div > div > div.Layout-sc-nxg1ff-0.gZaqky > form > div > div:nth-child(4) > div > div:nth-child(1) > div.Layout-sc-nxg1ff-0.hiuuyA > div.Layout-sc-nxg1ff-0.phone-number-input__country-selector > select > option:nth-child(29)')))
     usernap.click()

     usernap = WebDriverWait(browser, 120).until(
         EC.presence_of_element_located((By.CSS_SELECTOR,
                                         '#phone-input')))
     usernap.send_keys(fnumbers[recount])
     usernap = WebDriverWait(browser, 120).until(
         EC.presence_of_element_located((By.CSS_SELECTOR,
                                         'body > div.ReactModalPortal > div > div > div > div > div > div.Layout-sc-nxg1ff-0.gmqBFP > div > div > div.Layout-sc-nxg1ff-0.gZaqky > form > div > div:nth-child(5) > button')))
     usernap.click()
     time.sleep(3)
     usernap = WebDriverWait(browser, 120).until(
         EC.presence_of_element_located((By.CSS_SELECTOR,
                                         'body > div.ReactModalPortal > div > div > div > div > div > div > div > div > div > div > div.Layout-sc-nxg1ff-0.doXjlI > div.Layout-sc-nxg1ff-0.guDZbQ > div:nth-child(4) > button')))
     usernap.click()

     browser.refresh()
     count = count + 1
     if (recount < (len(fnumbers) - 1)):
         recount = recount + 1
     else:
         recount = 0

     print(count)




    except  Exception  as e:
      print("exception ayatha")
      print(a)
      browser.close()
      break
   


     
      


     
     
     
     
  
