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
#usernameStr = 'poppyharlow78978'
usernameStr = 'hggmn56yt'
Str = ''
options = uc.ChromeOptions()

#options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')
options.add_argument('--load-extension=D:\\autologinbot-master\\UltraSur,D:\\autologinbot-master\\LOBBY\\Nope')

#options.add_argument('--load-extension=D:\\autologinbot-master\\LOBBY\\Nope')
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
 
  url='https://signup.ebay.com/pa/crte?ru=https%3A%2F%2Fwww.ebay.com%2F'

  

  
    
    
  
  

  fnumbers=["3007982112","3007982112","3317263972","3305094490","3305710811","3305712567","3305747159","3305750758","3305918309","3306032726","3306105908","3306185154","3306198931","3306231734","3306399061","3306794291","3306937418","3307269262","3308075538","3308494814","3308677432","3308697145","3308697262","3308697388","3308697689","3309518247","3310178071","3310456022","3311215119","3311216453","3311219635","3312251433","3312535405","3312656805","3312894453","3313125455","3313272862","3313596147","3313884135","3314214392","3314385331","3314418840","3314418861","3314738520","3314914162","3315303240","3315833942","3316093485","3316360924","3316845361","3317763174","3317994263","3318241357","3318806750","3319876087","3320916204","3322425623","3323811905","3324810852","3325997385","3326194901","3326440420","3326809904","3326890749","3327404972","3327918460","3328928216","3329421373","3330374841","3330916254","3331695866","3334188614","3334753396","3335789123","3336472055","3336799140","3338382201","3339563320","3340273323","3340778394","3340970279","3340970316","3341279054","3341597587","3341597787","3341597987","3341598187","3341598387","3341598587","3341598787","3341598987","3341599187","3341599387","3341599587","3341599787","3341599987","3341912659","3343270612","3343592088","3343957239","3344650452","3345740187","3345740387","3345740587","3345740787","3345740987","3345741187","3345741387","3345741587","3345741787","3345741987","3345742187","3345742387","3345742587","3345742787","3345742987","3345743187","3345743387","3345743587","3345743787","3345743987","3345744187","3345744387","3345744587","3345744787","3345744987","3345745187","3345745387","3345745587","3345745787","3345745987","3345746187","3345746387","3345746587","3345746787","3345746987","3345747187","3345747387","3345747587","3345747787","3345747987","3345748187","3345748387","3345748587","3345748787","3345748987","3345749187","3345749387","3345749587","3345749787","3345749987","3345880849","3346529408","3346904714","3347751836","3348308428","3348435979","3349371221","3350038135","3350382670","3350849504","3351253956","3351489244","3351908608","3352393090","3352896420","3353096059","3353591632","3358365853","3359328231","3359558764","3359833140","3360310128","3366570689","3366870323","3367044574","3367259974","3367424520","3367643736","3371662169","3374671066","3374943697","3376049068","3376250872","3376335169","3377244386","3377460492","3377460955","3377626642","3378069497","3378077683","3379237409","3317286156","3317286188","3317286193","3317286194","3317286201","3317286209","3317286247","3317286258","3317286271","3317286282","3317286332","3317286348","3317286412","3317286443","3317286457","3317286461","3317286476","3317286490","3317286506","3317286548"]

  numbers=[]
 
  while(1):
    options = uc.ChromeOptions()
    options.add_argument("--disable-renderer-backgrounding")
    options.add_argument("--disable-backgrounding-occluded-windows")

      # options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')
    options.add_argument('--load-extension=D:\\autologinbot-master\\Urbanvpn,D:\\autologinbot-master\\LOBBY\\Nope')
    browser = uc.Chrome(options=options,use_subprocess=True)
    i = random.randint(2, 57)
    inb = 'infotelcotestahymed@gmail.com'
    browser.get(
        "chrome-extension://ecokmenakcanpnkbgifdiacoapdmhdjf/popup/index.html#/welcome-consent")
    try:

        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,
                 "body > div > div > div.simple_layout__body > div > div > div > button.button_pink.agreement_agree"))).click()
    except:
        pass
    try:

        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,
                 "body > div > div > div.simple_layout__header > div"))).click()
    except:
        pass
    time.sleep(2)

    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        "body > div > div > div.main_layout__body > div.location-box > div > div:nth-child(1) > input"))).click()
    time.sleep(2)
    ph = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div/div[3]/div[2]/div/div[2]/div/ul/li[" + str(i) + "]")))
    browser.execute_script("arguments[0].scrollIntoView(true);", ph);
    ph.click()
    print('country is: ' + str(i))





    while(1):





     browser.get(url)

     try:
         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             '#firstname')))
         phonee.send_keys('')

         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             '#lastname')))
         phonee.send_keys('zahid')
         emaill=random.choices(string.ascii_lowercase, k=9)
         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             '#Email')))

         phonee.send_keys(emaill,'@gmail.com')
         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             '#')))
         phonee.send_keys('')
         time.sleep(3)
         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             '#EMAIL_REG_FORM_SUBMIT')))
         phonee.click()
         time.sleep(8)

         browser.get('https://reg.ebay.com/reg/Upgrade?ru=https%3A%2F%2Faccountsettings.ebay.com%2Fuas')
         time.sleep(1)
         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             '#countryId')))
         phonee.click()

         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             '#countryId > option:nth-child(151)')))
         phonee.click()
         time.sleep(1)

         #phonee.send_keys(random.choices(string.ascii_lowercase, k=9))
         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             '#address1'))).send_keys(random.choices(string.ascii_lowercase, k=9))


         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             '#city')))
         phonee.send_keys(random.choices(string.ascii_lowercase, k=5))
         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             '#state')))
         phonee.send_keys(random.choices(string.ascii_lowercase, k=5))
         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             '#zip')))
         phonee.send_keys(random.choices(numb, k=5))
         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             '#phoneFlagComp1')))
         phonee.send_keys(fnumbers[recount])
         time.sleep(2)
         phonee = WebDriverWait(browser, 120).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             '#sbtBtn')))
         phonee.click()
         time.sleep(2)







         browser.get('https://accounts.ebay.com/acctsec/security-center')


         try:
             phonee = WebDriverWait(browser, 10).until(
                 EC.presence_of_element_located((By.CSS_SELECTOR,
                                                 '#pass')))
             phonee.send_keys('')
             phonee = WebDriverWait(browser, 120).until(
                 EC.presence_of_element_located((By.CSS_SELECTOR,
                                                 '#sgnBt')))
             phonee.click()

             browser.get('https://accountsettings.ebay.com/profile')

         except:
             pass
         cm=0

         while(1):


          try:




           phonee = WebDriverWait(browser, 50).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             '#mfa-link')))
           phonee.click()
           phonee = WebDriverWait(browser, 50).until(
               EC.presence_of_element_located((By.CSS_SELECTOR,
                                               '#text-btn')))
           phonee.click()
           phonee = WebDriverWait(browser, 50).until(
               EC.presence_of_element_located((By.CSS_SELECTOR,
                                               '#mobile-verify-init')))
           phonee.click()


           time.sleep(3)
           browser.execute_script("window.history.go(-1)")
          except:

             break
          cm+=1
          count = count + 1
          x = (len(fnumbers)) - 1
          if (recount < (x)):
              recount = recount + 1
          else:
              recount = 0
          print(count)
          if(cm>9):
              break

         time.sleep(2)
         browser.delete_all_cookies()
         i = random.randint(2, 57)
         inb = 'infotelcotestahymed@gmail.com'
         browser.get(
             "chrome-extension://ecokmenakcanpnkbgifdiacoapdmhdjf/popup/index.html#/welcome-consent")
         try:

             WebDriverWait(browser, 10).until(
                 EC.presence_of_element_located(
                     (By.CSS_SELECTOR,
                      "body > div > div > div.simple_layout__body > div > div > div > button.button_pink.agreement_agree"))).click()
         except:
             pass
         try:

             WebDriverWait(browser, 10).until(
                 EC.presence_of_element_located(
                     (By.CSS_SELECTOR,
                      "body > div > div > div.simple_layout__header > div"))).click()
         except:
             pass
         time.sleep(2)

         WebDriverWait(browser, 20).until(
             EC.presence_of_element_located((By.CSS_SELECTOR,
                                             "body > div > div > div.main_layout__body > div.location-box > div > div:nth-child(1) > input"))).click()
         time.sleep(2)
         ph = WebDriverWait(browser, 20).until(
             EC.presence_of_element_located(
                 (By.XPATH, "/html/body/div/div/div[3]/div[2]/div/div[2]/div/ul/li[" + str(i) + "]")))
         browser.execute_script("arguments[0].scrollIntoView(true);", ph);
         ph.click()
         print('country is: ' + str(i))







  

      

      
      

     except Exception  as e:



       browser.close()
     
       break
    



     

    
     
     
  
