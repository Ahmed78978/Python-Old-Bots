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
#soptions.add_extension('extension_1_6_6_0.crx')
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
 
  url='https://www.roblox.com/my/account#!/infos'
  strr=["099"],random.choices(numb,k=1),["-4"],random.choices(numb,k=1),random.choices(numb,k=1),random.choices(numb,k=1)
  
  yo=convertTuple(strr)
  
  
  rt=url.replace("0995-4521",yo)
  
  

  
    
    
  
  

  fnumbers=["3324974299","3310156215","3368060237","3368670587","3368988458","3369574568","3370338067","3370771209","3324974310","3314385265","3368059750","3368670488","3368988454","3369572855","3370338065","3370771132","3324974328","3314418195","3368059184","3368669489","3368988439","3369571599","3370337850","3370770693","3359115878","3359115083","3359114637","3359114395","3359114352","3359114307","3359112784","3359105219","3359105217","3359104168","3359104135","3324974902","3358079281","3367956840","3368634399","3368988235","3369522534","3370335881","3370745103","3324974923","3358366138","3367947513","3368634390","3368988202","3369521468","3370335878","3370743891","3324974951","3358718461","3367936495","3368628137","3368988201","3369515080","3370335872","3370741263","3324975036","3359085530","3367935506","3368621483","3368988185","3369512768","3370335870","3370738516","3324975069","3362044735","3367934492","3368619838","3368988168","3369508629","3370335864","3370736987","3324975071","3362504974","3367931638","3368616682","3368988148","3369507859","3370335855","3370733949","3324975199","3362533626","3367927215","3368616068","3368988139","3369504035","3370335854","3370728513","3324975255","3363614860","3367922773","3368614772","3368988134","3369504027","3370335847","3370727554","3324975273","3363615334","3367922701","3368609900","3368988132","3369503623","3370335841","3370726763","3324975285","3363615973","3367922694","3368609643","3368988122","3369498225","3370335840","3370724014","3324975292","3364971453","3367922046","3368608099","3368988104","3369493155","3370334532","3370720213","3324975299","3366738467","3367922041","3368608093","3368988097","3369491255","3370334528","3370719802","3324975317","3302362973","3367922039","3368608074","3368988096","3369487962","3370334527","3370717740","3324975335","3302367094","3367922035","3368607540","3368988093","3369487784","3370334526","3370714751","3324975428","3302387664","3367921546","3368606598","3368988058","3369487210","3370334516","3370711734","3324975429","3302388127","3367920816","3368604798","3368988031","3369483443","3370334513","3370711672","3324975469","3302589975","3367920812","3368604797","3368988029","3369479011","3370334508","3370711570","3324975516","3303453117","3367916878","3368604796","3368988016","3369476427","3370334398","3370711506","3324975583","3303482890","3367915870","3368604794","3368988014","3369471875","3370334386","3370711233","3324975650","3303877823","3367914558","3368604271","3368987996","3369471802","3370334381","3370710554","3324975731","3304020302","3367914495","3368603797","3368987989","3369471614","3370334379","3370698768","3324975738","3304020320","3367911259","3368603207","3368987986","3369471349","3370334378","3370698250","3324975741","3304689699","3367909642","3368602263","3368987985","3369470168","3370334374","3370698249","3324975766","3304766571","3367909509","3368601702","3368987976","3369465875","3370334369","3370698244","3324975860","3304915933","3367909485","3368575532","3368987974","3369464742","3370334328","3370696523"]
  numbers=[]
  #for x  in range(len(fnumbers)):
  # c=fnumbers[x]
   
  # rwithout=c.replace("+880","")
 #  numbers.append(rwithout)
  #time.sleep(8)
  
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
    #usernasp =browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div/div[6]/section/div/div/div/div/div[3]/a')
    #usernasp.click()
   
  #  print("signin clciked")
  #  time.sleep(20)
   # phone = browser.find_element_by_xpath('//*[@id="answerForm"]/div[1]/div/div[1]/div/div[1]/div/div/select')
#ph one = browser.find_element_by_class_name('hwid-input hwid-input-pwd')
    #phone.click() 
  #except NoSuchElementException:
  #   browser.close()
  #   break
  usrmn=["drellay","drniris","wysotig","oseom","ghamoasr","eeddie","etsbusr","etcirhear","ocrrsiehchc","opesosm","paedefeun","lsomrp","stien","abubrtawdlia","bhneadendroryn","alceme","lkytuans","ratieer","tianzordib","akkaeclfjopcma","bobbaalthh","emaaohl","alicnoat","yotretw","unegtidar","urleti","kviacndiaa","lagoearn","gaeeta","inunlaisoyl","arctopi","ornaoms","rnyaepe","kahsatfcysrih","ictcaob","dortnoar","leimih","alleerti","kceceih","htgrto","ampcsikall","enttiabir","aatsblufn","imanige","armiet","gerycylo","ndnoula","roars","lascuno","aaegulol","usrasnigexis","rierouf","ogohroruonciny","mastkaes","tonodoidhgaluh","nilcasleloy","nsahluf","alling","rpseraagp","rsaiuemlmu","exntieapshr","nrweerdyab","atidironew","opethhatiyn","uhrkas","annhgsual","atckrwo","isahinompa","ublagviel","ofyedn","husrainot","alteele","apulkol","wrnaliml","moslra","sondisirou","loihzerawln","roobtih","tocsiketss","pmehalgnit","zoossu","trasmbur","catuagnts","espbfuf","rneidoeus","ebhaoc","nanhbpulm","ipntaats","easrettat","yffiach","obsfaemou","eganeeeo","eflaahb","ahjenpl","fnonnea","nefrila","ncreetshcept","edgemn","nocaltandu","aotovcnlaa","lleogkirr","allias","refunkig","yrogcraj","ziavju","reatikn","eirtsndyni","horasdlar","chiaraps","ocidarr","eaanjsa","hramhu","oayrhlke","siteaita","nliaod","retelemr","nchrcru","trhsiohi","uciakro","angmomnda","lalloc","oelesubqu","rleoot","mapsoui","hcibbti","ntgialis","gmrsolrnani","nrigafr","gnftihut","ewlreaeriur","uprdui","hditiapn","anmzit","ryryrwn","slclbuo","lhclacrapseirm","miauiav","vosghu","welrlnai","werli","aroiemaw","ivbkars","hrpriyiimtb","rchautb","ttryeognsroe","gulodfadl","hdcchioser","nnfocinbmua","yczeigsntlio","nmehopbuars","ronrlma","lkeuscawn","reeodo","ngirol","dturgoegc","dielute","roontsu","aslomosa","rcecethr","daotee","useaig","denlefu","lliatse","ctuairb","etrrlada","aatbirly","rltyfba","ctbagaa","anicnens","igsnev","ydtsen","babohm","ppabeiaclg","syhgec","lfleufligeer","otuvo","lbonilig","tlealskgnlia","emvhrntapoulfll","ilkdeso","eerngi","pprometp","agimsu","lcohgs","awnyozrt","murisctei","resieal","mcrhituectiatdc","meeyre","jodregl","nkigicn","tllsansay","rpuoekm","eardurmal","uhttet","siling","okldeyn","rmetman","itrkikect","ahoenaz"]
  while(1):
   
   #userna = WebDriverWait(browser, 30).until(
    #  EC.presence_of_element_located((By.XPATH, '//*[@id="answerForm"]/div[1]/div/div[1]/div/div[1]/div/div/select/option[198]')))
  # userna.click()
    #phone = WebDriverWait(browser, 120).until(
     # EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button')))
   #phone = browser.find_element_by_class_name('hwid-input hwid-input-pwd')
    #phone.click()
    browser = webdriver.Chrome(options=options, desired_capabilities=capa)
    browser.get((url))
    p = browser.current_window_handle

#get first child window
    time.sleep(5) 
    chwd = browser.window_handles
  
    if (len(chwd)>=2):

     browser.switch_to.window(chwd[1])
 
     browser.close()
     browser.switch_to.window(chwd[0])
    time.sleep(5) 
    try:
     phonee = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="sign-up-button"]')))
     phonee.click()
     time.sleep(2)
     phonee = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="MonthDropdown"]')))
     phonee.click()
     time.sleep(1)
     usernap = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="MonthDropdown"]/option[3]')))

     usernap.click()
     time.sleep(1)

     usernap = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="DayDropdown"]')))
     usernap.click()
     time.sleep(1)
     usernap = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="DayDropdown"]/option[4]')))
     usernap.click()
     time.sleep(1)
     usernap = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="YearDropdown"]')))
     usernap.click()
     time.sleep(1)
     usernap = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="YearDropdown"]/option[24]')))
     usernap.click()
     time.sleep(1)
     nammm=random.choices(string.ascii_lowercase , k=15)

     usernap = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="signup-username"]')))
     usernap.send_keys(nammm)
     time.sleep(1)
     passs=random.choices(string.ascii_lowercase , k=10)
     usernap = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="signup-"]'))).send_keys(passs)
    
     time.sleep(1)
     usernap = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="MaleButton"]')))
     usernap.click()
     time.sleep(4)

     usernap = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="signup-button"]')))
     usernap.click()
   

     while (1):
      time.sleep(10)
      phone = WebDriverWait(browser, 120).until(
       EC.presence_of_element_located((By.XPATH, '//button[@ng-click="addPhone()"]'))).click()

      time.sleep(1)
      phonesp = WebDriverWait(browser, 120).until(
       EC.presence_of_element_located((By.XPATH, '//select[@ng-model="phoneInfo.phonePrefix"]'))).click()

      time.sleep(1)
      phones = WebDriverWait(browser, 120).until(
       EC.presence_of_element_located((By.XPATH, '//option[@label="Pakistan (+92)"]'))).click()

      time.sleep(1)
      phonesp = WebDriverWait(browser, 120).until(
       EC.presence_of_element_located((By.XPATH, '//*[@id="phone-text-box"]'))).send_keys(fnumbers[recount])

      time.sleep(1)
      try:
       usernasp = browser.find_element(By.CSS_SELECTOR,
                                       '#rbx-body > div.modal.ng-scope.ng-isolate-scope.in > div > div > div > div:nth-child(1) > div > div.modal-footer > div.update-button-container > button').click()

       time.sleep(1)

      except (NoSuchElementException, TimeoutException):
       print("exception ayatha")
       browser.close()
       break
      time.sleep(1)
      count = count + 1
      x = (len(fnumbers))-1
      if (recount < (x)):
       recount = recount + 1
      else:
       recount = 0
      print(count)
      time.sleep(5)
      if(count%5==0):
        browser.close()
        break
      else:  
        browser.refresh() 
    except Exception  as e:
     browser.close()
    
     
     break
    



     

    
     
     
  
