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
options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')
#options.add_argument('--load-extension=D:\\autologinbot-master\\UltraSur')
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
 
  url='https://m.bolt.eu/Login'
  strr=["099"],random.choices(numb,k=1),["-4"],random.choices(numb,k=1),random.choices(numb,k=1),random.choices(numb,k=1)
  
  yo=convertTuple(strr)
  
  
  rt=url.replace("0995-4521",yo)
  
  

  
    
    
  
  

  fnumbers=["1958664041","1958540802","1958662581","1958665196","1958650573","1958663900","1958540961","1958663378","1941090409","1958651901","1958663758","1958540545","1958661453","1958664191","1958666470","1958662639","1958665153","1958542078","1958547248","1958546224","1958661648","1958664386","1958668127","1958663032","1973586754","1958651907","1958663764","1958652405","1958661703","1958664437","1958543001","1958663485","1925384071","1958661970","1958664583","1958670426","1958662988","1949373297","1958651759","1958663673","1958652257","1958662651","1938449825","1958541986","1958546852","1953229858","1958661425","1958664163","1958666362","1958663350","1953877811","1958661337","1958664121","1958662817","1945946734","1958547646","1958663646","1958541000","1958663012","1963930545","1915819219","1958663650","1958652830","1958661896","1958664563","1958540502","1958662624","1958665189","1958542053","1958663701","1958652293","1958650551","1958661942","1958662762","1958663363","1958663581","1958664109","1958664589","1958544654","1958546136","1958653077","1958540605","1958657635","1958661276","1958664089","1958540958","1958662632","1958665270","1958543297","1958663948","1958541426","1958663426","1941345642","1958651595","1958663806","1958540719","1958661501","1958664239","1958666778","1958662689","1958665208","1958651955","1958663521","1958652164","1958661697","1958664434","1958669499","1958663081","1963929059","1958651805","1958663812","1958652636","1958661817","1958664485","1958541675","1958546642","1931488114","1958662027","1958664833","1958549143","1958663037","1971810682","1958651708","1958663721","1958540026","1958662699","1952571201","1958541833","1958546919","1948178411","1958661473","1958664211","1958667408","1958663401","1937216913","1958661431","1958664169","1958662870","1932579589","1958542862","1958663694","1958541388","1958663061","1919750576","1976987089","1958663698","1958652906","1958661948","1958664612","1958540504","1958662677","1958665254","1958541798","1958663749","1958652369","1958650550","1958661976","1958662766","1958663394","1958663595","1958664117","1958664599","1958544681","1958546184","1958653078","1958540606","1958658025","1958661391","1958664137","1958541271","1958662684","1958665370","1958543246","1958663996","1958666604","1958663476","1929863663","1958650014","1958663854","1958540807","1958661549","1958664287","1958667073","1958662737","1958665287","1958651751","1958663569","1958652249","1958661810","1958664482","1958550229","1958663132","1955790038","1958651703","1958663860","1958652941","1958661917","1958664533","1946368958","1958546704","1948504594","1958662090","1958664882","1958542034","1958663086","1947849630","1958651402","1958663769","1958540116","1958662747","1951457173","1958665325","1958546971","1958544782","1958661521","1958664259","1958669121","1958663450","1948557309","1958661479","1958664217","1958662930","1962570313","1958651158","1958663742","1958541464","1958663109","1960795811","1958651772","1958663746","1958652977","1958662000","1958664813","1958540596","1958662725","1958665357","1958541747","1958663797","1958652522","1958650335","1958661992","1958662769","1958663402","1958663597","1958664118","1958664603","1958544682","1958546211","1958653126","1958540621","1958666010","1958661447","1958664185","1958541499","1958662732","1959456633","1958665870","1958664044","1958668256","1958546631","1952525534","1958543503","1958663902","1958541040","1958661597","1958664335","1958667522","1958662788","1958665375","1958650833","1958663617","1958652402","1958661914","1958664530","1958551395","1958663182","1963928987","1958651652","1958663908","1958653017","1958661968","1958664581","1945089278","1958546769","1966469578","1958662258","1958664930","1958541779","1958663138","1963928610","1958651096","1958663817","1958540468","1958662799","1935262691","1958660011","1958547023","1958544864","1958661569","1958664307","1958670034","1958663499","1973693553","1958661527","1958664265","1958663009","1945088976","1958650903","1958663790","1958657349","1958663162","1960817032","1958650497","1958663794","1958540246","1958662064","1958664862","1958540678","1958662776","1954575270","1958651216","1958663845","1958652600","1958650091","1958661994","1958662802","1958663403","1958663600","1958664119","1958664606","1958544731","1958546212","1958653153","1958540622","1958666011"]

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
  browser = webdriver.Chrome(options=options, desired_capabilities=capa)
  while(1):
   


    browser.get((url))

    try:
     try:
      phonee = WebDriverWait(browser, 10).until(
       EC.presence_of_element_located((By.CSS_SELECTOR, '#cookiebanner-top > div > div > div > div > button.cb-bolt-btn-action.cb-bolt-btn-accept')))
      phonee.click()
     except:
       pass


     time.sleep(1)
     phonee = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > div > div.Body > div.PhoneInputs > div > input:nth-child(2)')))
     phonee.click()
     phonee = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located(
       (By.CSS_SELECTOR, '#root > div > div > div.Body > form > div > div > input:nth-child(2)')))

     phonee.send_keys(Keys.CONTROL,'a')
     phonee.send_keys(fnumbers[recount])
     time.sleep(1)
     usernap = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > div > div.Body > form > div > div > input.underlined.flag-icon.flag-icon-pk')))
     usernap.send_keys(Keys.CONTROL,'a')
     usernap.send_keys("+880")
     time.sleep(1)

     usernap = WebDriverWait(browser, 120).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > div > div.Body > form > button')))
     usernap.click()
     time.sleep(8)
     browser.delete_all_cookies()
     browser.refresh()

     
   

           
     count = count + 1
     x = (len(fnumbers))-1
     if (recount < (x)):
       recount = recount + 1
     else:
       recount = 0
     print(count)
     time.sleep(5)
     browser.refresh()
    except Exception  as e:

     browser.close()
    
     
     break
    



     

    
     
     
  
