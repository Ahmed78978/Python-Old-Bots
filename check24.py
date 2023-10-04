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
options.add_argument('--load-extension=D:\\autologinbot-master\\UltraSur')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
mobile_emulation = {"deviceName": "iPhone SE"}
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
#options.add_experimental_option("mobileEmulation", mobile_emulation)
count=1
recount=0
#time.sleep(1000)
while(1):
 while(1):  
  numb="0123456789"
 
  url='https://kundenbereich.check24.de/user/login.html?uli_mode=register&email=&phone='
  strr=["099"],random.choices(numb,k=1),["-4"],random.choices(numb,k=1),random.choices(numb,k=1),random.choices(numb,k=1)
  
  yo=convertTuple(strr)
  
  
  rt=url.replace("0995-4521",yo)
  
  

  
    

  
  

  #fnumbers=["+923324974902","+923358079281","+923367956840","+923368634399","+923368988235","+923369522534","+923370335881","+923370745103","+923324974923","+923358366138","+923367947513","+923368634390","+923368988202","+923369521468","+923370335878","+923370743891","+923324974951","+923358718461","+923367936495","+923368628137","+923368988201","+923369515080","+923370335872","+923370741263","+923324975036","+923359085530","+923367935506","+923368621483","+923368988185","+923369512768","+923370335870","+923370738516","+923324975069","+923362044735","+923367934492","+923368619838","+923368988168","+923369508629","+923370335864","+923370736987","+923324975071","+923362504974","+923367931638"]

  fnumbers=["+923007982112","+923374997844"]
  numbers=[]
 
  usrmn=["drellay","drniris","wysotig","oseom","ghamoasr","eeddie","etsbusr","etcirhear","ocrrsiehchc","opesosm","paedefeun","lsomrp","stien","abubrtawdlia","bhneadendroryn","alceme","lkytuans","ratieer","tianzordib","akkaeclfjopcma","bobbaalthh","emaaohl","alicnoat","yotretw","unegtidar","urleti","kviacndiaa","lagoearn","gaeeta","inunlaisoyl","arctopi","ornaoms","rnyaepe","kahsatfcysrih","ictcaob","dortnoar","leimih","alleerti","kceceih","htgrto","ampcsikall","enttiabir","aatsblufn","imanige","armiet","gerycylo","ndnoula","roars","lascuno","aaegulol","usrasnigexis","rierouf","ogohroruonciny","mastkaes","tonodoidhgaluh","nilcasleloy","nsahluf","alling","rpseraagp","rsaiuemlmu","exntieapshr","nrweerdyab","atidironew","opethhatiyn","uhrkas","annhgsual","atckrwo","isahinompa","ublagviel","ofyedn","husrainot","alteele","apulkol","wrnaliml","moslra","sondisirou","loihzerawln","roobtih","tocsiketss","pmehalgnit","zoossu","trasmbur","catuagnts","espbfuf","rneidoeus","ebhaoc","nanhbpulm","ipntaats","easrettat","yffiach","obsfaemou","eganeeeo","eflaahb","ahjenpl","fnonnea","nefrila","ncreetshcept","edgemn","nocaltandu","aotovcnlaa","lleogkirr","allias","refunkig","yrogcraj","ziavju","reatikn","eirtsndyni","horasdlar","chiaraps","ocidarr","eaanjsa","hramhu","oayrhlke","siteaita","nliaod","retelemr","nchrcru","trhsiohi","uciakro","angmomnda","lalloc","oelesubqu","rleoot","mapsoui","hcibbti","ntgialis","gmrsolrnani","nrigafr","gnftihut","ewlreaeriur","uprdui","hditiapn","anmzit","ryryrwn","slclbuo","lhclacrapseirm","miauiav","vosghu","welrlnai","werli","aroiemaw","ivbkars","hrpriyiimtb","rchautb","ttryeognsroe","gulodfadl","hdcchioser","nnfocinbmua","yczeigsntlio","nmehopbuars","ronrlma","lkeuscawn","reeodo","ngirol","dturgoegc","dielute","roontsu","aslomosa","rcecethr","daotee","useaig","denlefu","lliatse","ctuairb","etrrlada","aatbirly","rltyfba","ctbagaa","anicnens","igsnev","ydtsen","babohm","ppabeiaclg","syhgec","lfleufligeer","otuvo","lbonilig","tlealskgnlia","emvhrntapoulfll","ilkdeso","eerngi","pprometp","agimsu","lcohgs","awnyozrt","murisctei","resieal","mcrhituectiatdc","meeyre","jodregl","nkigicn","tllsansay","rpuoekm","eardurmal","uhttet","siling","okldeyn","rmetman","itrkikect","ahoenaz"]
  while(1):
      while (1):

          browser = webdriver.Chrome(options=options, desired_capabilities=capa)

          browser.get((url))


          try:
              time.sleep(8)
              while (1):
                  try:
                      phonee = WebDriverWait(browser, 120).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          'body > div.c24-cookie-consent-wrapper > div.c24-cookie-consent-notice > div.c24-cookie-consent-notice-buttons.clearfix > a:nth-child(2)')))
                      phonee.click()
                      break
                  except:
                      pass

              while(1):
                  time.sleep(2)
                  while (1):
                      try:
                          usernap = WebDriverWait(browser, 120).until(
                              EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '#c24-uli-iframe')))
                          break
                      except:

                          pass
                  while (1):
                      try:
                          usernap = WebDriverWait(browser, 5).until(
                              EC.presence_of_element_located((By.CSS_SELECTOR, '#cl_login')))
                          actions = ActionChains(browser)
                          actions.move_to_element(usernap)
                          actions.click()
                          actions.send_keys(fnumbers[recount])
                          actions.perform()
                          break
                      except:

                          pass

                  time.sleep(1)
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR, '#c24-uli-login-btn')))
                  browser.execute_script("arguments[0].click();", usernap)
                  time.sleep(2)
                  while (1):
                      try:
                          usernap = WebDriverWait(browser, 5).until(
                              EC.presence_of_element_located((By.CSS_SELECTOR, '#cl_email_registercheck')))
                          actions = ActionChains(browser)
                          actions.move_to_element(usernap)
                          actions.click()
                          actions.send_keys(random.choices(string.ascii_lowercase, k=10), "@gmail.com")
                          actions.perform()
                          break
                      except:

                          pass

                  time.sleep(0.5)
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR, '#c24-uli-registercheck-btn')))
                  browser.execute_script("arguments[0].click();", usernap)
                  while (1):
                      try:
                          usernap = WebDriverWait(browser, 5).until(
                              EC.presence_of_element_located((By.CSS_SELECTOR, '#cl_ul_firstname')))
                          actions = ActionChains(browser)
                          actions.move_to_element(usernap)
                          actions.click()
                          actions.send_keys(random.choices(string.ascii_lowercase, k=10))
                          actions.perform()
                          break
                      except:
                          pass

                  usernap = WebDriverWait(browser, 5).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR, '#cl_ul_lastname')))
                  actions = ActionChains(browser)
                  actions.move_to_element(usernap)
                  actions.click()
                  actions.send_keys(random.choices(string.ascii_lowercase, k=10))
                  actions.perform()

                  usernap = WebDriverWait(browser, 5).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR, '#cl_pw_register')))
                  actions = ActionChains(browser)
                  actions.move_to_element(usernap)
                  actions.click()
                  actions.send_keys('')
                  actions.perform()

                  usernap = WebDriverWait(browser, 5).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR, '#cl_ul_pw_register_repeat')))
                  actions = ActionChains(browser)
                  actions.move_to_element(usernap)
                  actions.click()
                  actions.send_keys('')
                  actions.perform()

                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR, '#c24-uli-register-btn')))
                  browser.execute_script("arguments[0].click();", usernap)
                  time.sleep(3)
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      'body > div > div > div.c24-uli > div.c24-uli-ele.c24-uli-tan.clearfix > form > div.c24-uli-form-ele.clearfix > a')))
                  browser.execute_script("arguments[0].click();", usernap)
                  time.sleep(10)
                  browser.get((url))

                  browser.switch_to.default_content()

                  count = count + 1
                  x = (len(fnumbers)) - 1
                  if (recount < (x)):
                      recount = recount + 1
                  else:
                      recount = 0
                  print(count)

                  if (count % 10 == 0):
                      browser.close()
                      break


          except Exception as e:


           browser.close()





   


     

    
     
     
  
