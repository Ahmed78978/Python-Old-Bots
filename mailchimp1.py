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
options = webdriver.ChromeOptions()
#bboptions.add_argument('--load-extension=D:\\autologinbot-master\\UltraSur')
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
 
  url='https://us8.admin.mailchimp.com/account/security/'
  strr=["099"],random.choices(numb,k=1),["-4"],random.choices(numb,k=1),random.choices(numb,k=1),random.choices(numb,k=1)
  
  yo=convertTuple(strr)
  
  
  rt=url.replace("0995-4521",yo)
  
  

  
    
    
  
  

  fnumbers=["3368616682","3368988148","3369507859","3370335855","3370733949","3324975199","3362533626","3367927215","3368616068","3368988139","3369504035","3370335854","3370728513","3324975255","3363614860","3367922773","3368614772","3368988134","3369504027","3370335847","3370727554","3324975273","3363615334","3367922701","3368609900","3368988132","3369503623","3370335841","3370726763","3324975285","3363615973","3367922694","3368609643","3368988122","3369498225","3370335840","3370724014","3324975292","3364971453","3367922046","3368608099","3368988104","3369493155"]


  numbers=[]
 
  usrmn=["drellay","drniris","wysotig","oseom","ghamoasr","eeddie","etsbusr","etcirhear","ocrrsiehchc","opesosm","paedefeun","lsomrp","stien","abubrtawdlia","bhneadendroryn","alceme","lkytuans","ratieer","tianzordib","akkaeclfjopcma","bobbaalthh","emaaohl","alicnoat","yotretw","unegtidar","urleti","kviacndiaa","lagoearn","gaeeta","inunlaisoyl","arctopi","ornaoms","rnyaepe","kahsatfcysrih","ictcaob","dortnoar","leimih","alleerti","kceceih","htgrto","ampcsikall","enttiabir","aatsblufn","imanige","armiet","gerycylo","ndnoula","roars","lascuno","aaegulol","usrasnigexis","rierouf","ogohroruonciny","mastkaes","tonodoidhgaluh","nilcasleloy","nsahluf","alling","rpseraagp","rsaiuemlmu","exntieapshr","nrweerdyab","atidironew","opethhatiyn","uhrkas","annhgsual","atckrwo","isahinompa","ublagviel","ofyedn","husrainot","alteele","apulkol","wrnaliml","moslra","sondisirou","loihzerawln","roobtih","tocsiketss","pmehalgnit","zoossu","trasmbur","catuagnts","espbfuf","rneidoeus","ebhaoc","nanhbpulm","ipntaats","easrettat","yffiach","obsfaemou","eganeeeo","eflaahb","ahjenpl","fnonnea","nefrila","ncreetshcept","edgemn","nocaltandu","aotovcnlaa","lleogkirr","allias","refunkig","yrogcraj","ziavju","reatikn","eirtsndyni","horasdlar","chiaraps","ocidarr","eaanjsa","hramhu","oayrhlke","siteaita","nliaod","retelemr","nchrcru","trhsiohi","uciakro","angmomnda","lalloc","oelesubqu","rleoot","mapsoui","hcibbti","ntgialis","gmrsolrnani","nrigafr","gnftihut","ewlreaeriur","uprdui","hditiapn","anmzit","ryryrwn","slclbuo","lhclacrapseirm","miauiav","vosghu","welrlnai","werli","aroiemaw","ivbkars","hrpriyiimtb","rchautb","ttryeognsroe","gulodfadl","hdcchioser","nnfocinbmua","yczeigsntlio","nmehopbuars","ronrlma","lkeuscawn","reeodo","ngirol","dturgoegc","dielute","roontsu","aslomosa","rcecethr","daotee","useaig","denlefu","lliatse","ctuairb","etrrlada","aatbirly","rltyfba","ctbagaa","anicnens","igsnev","ydtsen","babohm","ppabeiaclg","syhgec","lfleufligeer","otuvo","lbonilig","tlealskgnlia","emvhrntapoulfll","ilkdeso","eerngi","pprometp","agimsu","lcohgs","awnyozrt","murisctei","resieal","mcrhituectiatdc","meeyre","jodregl","nkigicn","tllsansay","rpuoekm","eardurmal","uhttet","siling","okldeyn","rmetman","itrkikect","ahoenaz"]
  while(1):
   
 
    browser = webdriver.Chrome(options=options, desired_capabilities=capa)
    browser.get((url))
    
    try:
     phonee = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, '#username')))
     phonee.send_keys("jamalimtiaz545@gmail.com")

   
     phonee = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, '#')))
     phonee.send_keys("")

     usernap = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, '#submit-btn')))

     usernap.click()
     time.sleep(10)
     usernap = WebDriverWait(browser, 120).until(
         EC.presence_of_element_located((By.CSS_SELECTOR, '#onetrust-close-btn-container > button')))

     usernap.click()



     while(1):
       while(1):
           try:
             usernap = WebDriverWait(browser, 120).until(
               EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src='/i/account/security/'")))
             break
           except:
               print("element")
               pass
       usernap = WebDriverWait(browser, 240).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#edit-phone-number")))

       browser.execute_script("arguments[0].click();", usernap)
       while(1):
        try:
         usernap = WebDriverWait(browser, 120).until(
           EC.presence_of_element_located((By.CSS_SELECTOR, '#sms-phone-cc')))
         usernap.click()
         break
        except:
            print("trying")
            usernap = WebDriverWait(browser, 60).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#edit-phone-number")))

            browser.execute_script("arguments[0].click();", usernap)
            pass

       usernap = WebDriverWait(browser, 125).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#dijit_MenuItem_134_text')))
       usernap.click()
       time.sleep(0.5)
       usernap = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#sms-phone-number')))
       usernap.send_keys(Keys.CONTROL, "a")
       usernap.send_keys(fnumbers[recount])

       usernap = WebDriverWait(browser, 120).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#verify-phone')))
       usernap.click()
       time.sleep(5)
       browser.switch_to.default_content()

       count = count + 1
       x = (len(fnumbers)) - 1
       if (recount < (x)):
         recount = recount + 1
       else:
        recount = 0
       print(count)

       browser.refresh()
    except Exception as e:
      print(a)

      browser.quit()

      break


    



     

    
     
     
  
