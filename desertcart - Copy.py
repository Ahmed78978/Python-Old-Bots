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
options.add_argument('--load-extension=D:\\autologinbot-master\\LOBBY\\Nope,,D:\\autologinbot-master\\Urbanvpn')

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
 
  url='https://pakistan.desertcart.com/account/personal-information'

  

  
    
    
  
  

  fnumbers=["+8801958661276","+8801958664089","+8801958540958","+8801958662632","+8801958665270","+8801958543297","+8801958663948","+8801958541426","+8801958663426","+8801941345642","+8801958651595","+8801958663806","+8801958540719","+8801958661501","+8801958664239","+8801958666778","+8801958662689","+8801958665208","+8801958651955","+8801958663521","+8801958652164","+8801958661697","+8801958664434","+8801958669499","+8801958663081","+8801963929059","+8801958651805","+8801958663812","+8801958652636","+8801958661817","+8801958664485","+8801958541675","+8801958546642","+8801931488114","+8801958662027","+8801958664833","+8801958549143","+8801958663037","+8801971810682","+8801958651708","+8801958663721","+8801958540026","+8801958662699","+8801952571201","+8801958541833","+8801958546919","+8801948178411","+8801958661473","+8801958664211","+8801958667408","+8801958663401","+8801937216913","+8801958661431","+8801958664169","+8801958662870","+8801932579589","+8801958542862","+8801958663694","+8801958541388","+8801958663061","+8801919750576","+8801976987089","+8801958663698","+8801958652906","+8801958661948","+8801958664612","+8801958540504","+8801958662677","+8801958665254","+8801958541798","+8801958663749","+8801958652369","+8801958650550","+8801958661976","+8801958662766","+8801958663394","+8801958663595","+8801958664117","+8801958664599","+8801958544681","+8801958546184","+8801958653078","+8801958540606","+8801958658025","+8801958661391","+8801958664137","+8801958541271","+8801958662684","+8801958665370","+8801958543246","+8801958663996","+8801958666604","+8801958663476","+8801929863663","+8801958650014","+8801958663854","+8801958540807","+8801958661549","+8801958664287","+8801958667073","+8801958662737","+8801958665287","+8801958651751","+8801958663569","+8801958652249","+8801958661810","+8801958664482","+8801958550229","+8801958663132","+8801955790038","+8801958651703","+8801958663860","+8801958652941","+8801958661917","+8801958664533","+8801946368958","+8801958546704","+8801948504594","+8801958662090","+8801958664882","+8801958542034","+8801958663086","+8801947849630","+8801958651402","+8801958663769","+8801958540116","+8801958662747","+8801951457173","+8801958665325","+8801958546971","+8801958544782","+8801958661521","+8801958664259","+8801958669121","+8801958663450","+8801948557309","+8801958661479","+8801958664217","+8801958662930","+8801962570313","+8801958651158","+8801958663742","+8801958541464","+8801958663109","+8801960795811","+8801958651772","+8801958663746","+8801958652977","+8801958662000","+8801958664813","+8801958540596","+8801958662725","+8801958665357","+8801958541747","+8801958663797","+8801958652522","+8801958650335","+8801958661992","+8801958662769","+8801958663402","+8801958663597","+8801958664118","+8801958664603","+8801958544682","+8801958546211","+8801958653126","+8801958540621","+8801958666010","+8801958661447","+8801958664185","+8801958541499","+8801958662732","+8801959456633","+8801958665870","+8801958664044","+8801958668256","+8801958546631","+8801952525534","+8801958543503","+8801958663902","+8801958541040","+8801958661597","+8801958664335","+8801958667522","+8801958662788","+8801958665375","+8801958650833","+8801958663617","+8801958652402","+8801958661914","+8801958664530","+8801958551395","+8801958663182","+8801963928987","+8801958651652","+8801958663908","+8801958653017","+8801958661968","+8801958664581","+8801945089278","+8801958546769","+8801966469578","+8801958662258","+8801958664930","+8801958541779","+8801958663138","+8801963928610","+8801958651096","+8801958663817","+8801958540468","+8801958662799","+8801935262691","+8801958660011","+8801958547023","+8801958544864","+8801958661569","+8801958664307","+8801958670034","+8801958663499","+8801973693553","+8801958661527","+8801958664265","+8801958663009","+8801945088976","+8801958650903","+8801958663790","+8801958657349","+8801958663162","+8801960817032","+8801958650497","+8801958663794","+8801958540246","+8801958662064","+8801958664862","+8801958540678","+8801958662776","+8801954575270","+8801958651216","+8801958663845","+8801958652600","+8801958650091","+8801958661994","+8801958662802","+8801958663403","+8801958663600","+8801958664119","+8801958664606","+8801958544731","+8801958546212","+8801958653153","+8801958540622","+8801958666011"]

  numbers=[]

  while (1):
      options = uc.ChromeOptions()

      # options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')
      options.add_argument("--disable-renderer-backgrounding")
      options.add_argument('--ignore-ssl-errors=yes')
      options.add_argument('--ignore-certificate-errors')
      options.add_argument("--disable-backgrounding-occluded-windows")
      options.add_argument('--load-extension=D:\\autologinbot-master\\LOBBY\\Nope,D:\\autologinbot-master\\Urbanvpn')
      browser = uc.Chrome(options=options, use_subprocess=True, version_main=107)
      while (1):
          try:
              browser.get('chrome-extension://dlnlfkobboboecjlnfnaabpfoegcgnkn/popup.html')
              time.sleep(3)
              phonee = WebDriverWait(browser, 120).until(
                  EC.presence_of_element_located((By.CSS_SELECTOR,
                                                  '#edit_key')))
              phonee.click()
              phonee = WebDriverWait(browser, 120).until(
                  EC.presence_of_element_located((By.CSS_SELECTOR,
                                                  '#app_frame > div:nth-child(5) > div.plan_info_container > input')))

              phonee.send_keys(Keys.CONTROL, 'a')

              phonee.send_keys('sub_1M0ulICRwBwvt6ptsU5sJPCD')

              time.sleep(2)
              break
          except:
              pass

      i = random.randint(2, 57)
      browser.get("chrome-extension://ecokmenakcanpnkbgifdiacoapdmhdjf/popup/index.html#/welcome-consent")
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

      while (1):

          browser.get(url)


          try:
              time.sleep(60)
              while (1):
                  try:
                      phonee = WebDriverWait(browser, 10).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          'body > div.MuiDialog-root.RedirectModal__modal > div.MuiDialog-container.MuiDialog-scrollPaper > div > div.MuiDialogActions-root.RedirectModal__modalActions.MuiDialogActions-spacing > button.MuiButtonBase-root.MuiButton-root.MuiButton-outlined.RedirectModal-button.MuiButton-outlinedPrimary')))

                      phonee.click()
                  except:
                      pass
                  phonee = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#root > div > div.global__container-inner > div > div > div.AccountPage__tab-content > div.PersonalInformation > div:nth-child(2) > div:nth-child(2) > div.MuiFormControl-root.MuiTextField-root.MuiFormControl-fullWidth > div > input')))
                  phonee.send_keys(Keys.CONTROL, 'a')

                  phonee.send_keys(fnumbers[recount])

                  phonee = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#root > div > div.global__container-inner > div > div > div.AccountPage__tab-content > div.PersonalInformation > div.PersonalInformation--button-container > button:nth-child(1)')))
                  phonee.click()
                  time.sleep(3)

                  phonee = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#root > div > div.global__container-inner > div > div > div.AccountPage__tab-content > div.PersonalInformation > div.PersonalInformation--button-container > button:nth-child(2)')))

                  phonee.click()
                  time.sleep(5)

                  try:
                      phonee = WebDriverWait(browser, 120).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          'body > div.MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper > div > div > div.Auth__form > div > form > div.MuiDialogActions-root.Auth__actions-vertical.MuiDialogActions-spacing > button')))
                      count = count + 1
                      x = (len(fnumbers)) - 1
                      if (recount < (x)):
                          recount = recount + 1
                      else:
                          recount = 0
                      print(count)
                  except:
                      i = random.randint(2, 57)
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
                      browser.get(url)
                      try:
                          WebDriverWait(browser, 10).until(EC.alert_is_present(),
                                                           'Timed out waiting for PA creation ' +
                                                           'confirmation popup to appear.')
                          alert = browser.switch_to.alert
                          alert.close()
                      except:
                          pass
                      try:
                          phonee = WebDriverWait(browser, 50).until(
                              EC.presence_of_element_located((By.CSS_SELECTOR,
                                                              'body > div.MuiDialog-root.RedirectModal__modal > div.MuiDialog-container.MuiDialog-scrollPaper > div > div.MuiDialogActions-root.RedirectModal__modalActions.MuiDialogActions-spacing > button.MuiButtonBase-root.MuiButton-root.MuiButton-outlined.RedirectModal-button.MuiButton-outlinedPrimary')))

                          phonee.click()
                      except:
                          pass

                      pass
                  time.sleep(1)
                  browser.refresh()




















          except Exception as e:

              pass
    



     

    
     
     
  
