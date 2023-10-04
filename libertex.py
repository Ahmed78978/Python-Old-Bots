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
#usernameStr = 'poppyharlow78978'
usernameStr = 'hggmn56yt'
Str = ''
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
#time.sleep(1000)
while(1):
 while(1):  
  numb="0123456789"
 
  url='https://libertex.org'
  strr=["099"],random.choices(numb,k=1),["-4"],random.choices(numb,k=1),random.choices(numb,k=1),random.choices(numb,k=1)
  
  yo=convertTuple(strr)
  
  
  rt=url.replace("0995-4521",yo)
  
  

  
    
    
  
  

  fnumbers=["3007982112","3324974902","3358079281","3367956840","3368634399","3368988235","3369522534","3370335881","3370745103","3324974923","3358366138","3367947513","3368634390","3368988202","3369521468","3370335878","3370743891","3324974951","3358718461","3367936495","3368628137","3368988201","3369515080","3370335872","3370741263","3324975036","3359085530","3367935506","3368621483","3368988185","3369512768","3370335870","3370738516","3324975069","3362044735","3367934492","3368619838","3368988168","3369508629","3370335864","3370736987","3324975071","3362504974","3367931638"]


  numbers=[]
 
  usrmn=["drellay","drniris","wysotig","oseom","ghamoasr","eeddie","etsbusr","etcirhear","ocrrsiehchc","opesosm","paedefeun","lsomrp","stien","abubrtawdlia","bhneadendroryn","alceme","lkytuans","ratieer","tianzordib","akkaeclfjopcma","bobbaalthh","emaaohl","alicnoat","yotretw","unegtidar","urleti","kviacndiaa","lagoearn","gaeeta","inunlaisoyl","arctopi","ornaoms","rnyaepe","kahsatfcysrih","ictcaob","dortnoar","leimih","alleerti","kceceih","htgrto","ampcsikall","enttiabir","aatsblufn","imanige","armiet","gerycylo","ndnoula","roars","lascuno","aaegulol","usrasnigexis","rierouf","ogohroruonciny","mastkaes","tonodoidhgaluh","nilcasleloy","nsahluf","alling","rpseraagp","rsaiuemlmu","exntieapshr","nrweerdyab","atidironew","opethhatiyn","uhrkas","annhgsual","atckrwo","isahinompa","ublagviel","ofyedn","husrainot","alteele","apulkol","wrnaliml","moslra","sondisirou","loihzerawln","roobtih","tocsiketss","pmehalgnit","zoossu","trasmbur","catuagnts","espbfuf","rneidoeus","ebhaoc","nanhbpulm","ipntaats","easrettat","yffiach","obsfaemou","eganeeeo","eflaahb","ahjenpl","fnonnea","nefrila","ncreetshcept","edgemn","nocaltandu","aotovcnlaa","lleogkirr","allias","refunkig","yrogcraj","ziavju","reatikn","eirtsndyni","horasdlar","chiaraps","ocidarr","eaanjsa","hramhu","oayrhlke","siteaita","nliaod","retelemr","nchrcru","trhsiohi","uciakro","angmomnda","lalloc","oelesubqu","rleoot","mapsoui","hcibbti","ntgialis","gmrsolrnani","nrigafr","gnftihut","ewlreaeriur","uprdui","hditiapn","anmzit","ryryrwn","slclbuo","lhclacrapseirm","miauiav","vosghu","welrlnai","werli","aroiemaw","ivbkars","hrpriyiimtb","rchautb","ttryeognsroe","gulodfadl","hdcchioser","nnfocinbmua","yczeigsntlio","nmehopbuars","ronrlma","lkeuscawn","reeodo","ngirol","dturgoegc","dielute","roontsu","aslomosa","rcecethr","daotee","useaig","denlefu","lliatse","ctuairb","etrrlada","aatbirly","rltyfba","ctbagaa","anicnens","igsnev","ydtsen","babohm","ppabeiaclg","syhgec","lfleufligeer","otuvo","lbonilig","tlealskgnlia","emvhrntapoulfll","ilkdeso","eerngi","pprometp","agimsu","lcohgs","awnyozrt","murisctei","resieal","mcrhituectiatdc","meeyre","jodregl","nkigicn","tllsansay","rpuoekm","eardurmal","uhttet","siling","okldeyn","rmetman","itrkikect","ahoenaz"]
  while(1):
   
 
    browser = webdriver.Chrome(options=options)
    browser.get((url))
    p = browser.current_window_handle

#get first child window
     
    chwd = browser.window_handles
  
    if (len(chwd)>=2):

     browser.switch_to.window(chwd[1])
 
     browser.close()
     browser.switch_to.window(chwd[0])
  
    try:
     phonee = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, '#block-mainnavigation > ul > li:nth-child(2) > a')))
     phonee.click()

   
     phonee = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Your email"]')))
     phonee.send_keys(random.choices(string.ascii_lowercase , k=6),"@gmail.com")

     usernap = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Come up with "]')))

     usernap.send_keys("")
     time.sleep(3)


     usernap = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, '#modal-real > div > div:nth-child(5) > input[type=tel]')))
     #usernap.send_keys(Keys.CONTROL, "a")
     time.sleep(0.5)
     #usernap.send_keys("+92")
     #time.sleep(0.5)
     usernap.send_keys(fnumbers[recount])
     time.sleep(0.3)

     usernap = WebDriverWait(browser, 120).until(
       EC.presence_of_element_located((By.CSS_SELECTOR, '#modal-real > div > div.form-row.form-row--last > input')))
     usernap.click()
     time.sleep(120)
     while(1):
        try:


            browser.get('https://app.libertex.org/profile-management')
            break

        except:
            pass     
    

     curl=browser.current_url
     if(curl!='https://app.libertex.org/profile-management'):
        browser.get('https://app.libertex.org/profile-management')

     while (1):

      time.sleep(0.8)
      usernap = WebDriverWait(browser, 5).until(
       EC.presence_of_element_located((By.CSS_SELECTOR, '#region-phone > div > div.set-state-wrapper > span.a-in-text.set-state')))
      usernap.click()
      time.sleep(0.5)
      usernap = WebDriverWait(browser, 10).until(
       EC.presence_of_element_located((By.CSS_SELECTOR, '#phone')))
      usernap.send_keys(Keys.CONTROL,"a")
      time.sleep(0.5)
      usernap.send_keys("92")
      usernap.send_keys(fnumbers[recount])
     
      nammm=random.choices(string.ascii_lowercase , k=15)

      usernap = WebDriverWait(browser, 120).until(
       EC.presence_of_element_located((By.CSS_SELECTOR, '#region-phone > div > form > input')))
      usernap.click()      
   


      count = count + 1
      x = (len(fnumbers))-1
      if (recount < (x)):
       recount = recount + 1
      else:
       recount = 0
      print(count)
      time.sleep(2)
      if(count%3==0):
         browser.close()
         break  
    except Exception  as e:

     browser.close()
    
     
     break
    



     

    
     
     
  
