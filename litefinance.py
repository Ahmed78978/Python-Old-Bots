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
def delete_cache(driver):
    driver.execute_script("window.open('')")  # Create a separate tab than the main one
    driver.switch_to.window(driver.window_handles[-1])  # Switch window to the second tab
    driver.get('chrome://settings/clearBrowserData')  # Open your chrome settings.
    perform_actions(driver, Keys.TAB * 2 + Keys.DOWN * 4 + Keys.TAB * 5 + Keys.ENTER)  # Tab to the time select and key down to say "All Time" then go to the Confirm button and press Enter
    driver.close()  # Close that window
    driver.switch_to.window(driver.window_handles[0])  # Switch Selenium controls to the original tab to continue normal functionality.


def perform_actions(driver, keys):
    actions = ActionChains(driver)
    actions.send_keys(keys)
    time.sleep(2)
    print('Performing Actions!')
    actions.perform()

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
#options.add_experimental_option("mobileEmulation", mobile_emulation)
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
#options.add_experimental_option("mobileEmulation", mobile_emulation)
count=0
recount=156
while(1):
 try:
     while (1):
         numb = "0123456789"

         url = 'https://my.litefinance.org'
         fnumbers = ["+923317263975","+923373580147","+923373580347","+923373580547","+923373580747","+923373580947","+923305187701","+923305710842","+923305719066","+923305747813","+923305753646","+923306003553","+923306039025","+923306140191","+923306187257","+923306199039","+923306235257","+923306458746","+923306824615","+923306938922","+923307541908","+923308212579","+923308571929","+923308696762","+923308697163","+923308697295","+923308697436","+923308697765","+923309892949","+923310215769","+923310474491","+923311215736","+923311216641","+923311430621","+923312354425","+923312545976","+923312690967","+923312931562","+923313169611","+923313427284","+923313618725","+923313958955","+923314265717","+923314385452","+923314419250","+923314749776","+923314946457","+923315489378","+923315891137","+923316150048","+923316300270","+923316755972","+923317511594","+923318209216","+923318736151","+923319717326","+923320709425","+923321862734","+923323495657","+923324675188","+923325772715","+923326172803","+923326359057","+923326798845","+923327404197","+923327723168","+923328854638","+923329284867","+923329925123","+923330916031","+923331694989","+923332158195","+923333809384","+923334682377","+923335334921","+923336397408","+923336626096","+923338212024","+923339087204","+923340210090","+923340716136","+923340953812","+923340970426","+923341278534","+923341597547","+923341597747","+923341597947","+923341598147","+923341598347","+923341598547","+923341598747","+923341598947","+923341599147","+923341599347","+923341599547","+923341599747","+923341599947","+923341755147","+923343061623","+923343552972","+923343924420","+923344398036","+923345675058","+923345741147","+923345741347","+923345741547","+923345741747","+923345741947","+923345742147","+923345742347","+923345742547","+923345742747","+923345742947","+923345743147","+923345743347","+923345743547","+923345743747","+923345743947","+923345744147","+923345744347","+923345744547","+923345744747","+923345744947","+923345745147","+923345745347","+923345745547","+923345745747","+923345745947","+923345746147","+923345746347","+923345746547","+923345746747","+923345746947","+923345747147","+923345747347","+923345747547","+923345747747","+923345747947","+923345748147","+923345748347","+923345748547","+923345748747","+923345748947","+923345749147","+923345749347","+923345749547","+923345749747","+923345749947","+923346387434","+923346760893","+923347549571","+923348143904","+923348435062","+923349278847","+923349794199","+923350327234","+923350813306","+923351253519","+923351367279","+923351792128","+923352360849","+923352879466","+923353076451","+923353433615","+923354079213","+923359558102","+923359771430","+923360193706","+923360701963","+923366447202","+923366572613","+923366870895","+923367106350","+923367267215","+923367464453","+923367712504","+923368797839","+923371681510","+923374823772","+923374965075","+923376076599","+923376281712","+923377040863","+923377251389","+923377492186","+923377673140","+923378076028","+923378093183","+923378094130","+923378096443","+923379716326","+923337162787","+923337162727","+923337162718","+923337162714","+923337162700","+923337162674","+923337162667","+923337162656","+923337162610","+923337162561","+923337162506","+923337162498","+923337162937","+923337162918","+923337162908","+923337162907","+923337162899","+923337162032","+923337162031","+923337161990","+923337161965","+923337161910","+923337163788","+923337163699","+923337163509","+923337163508","+923337163466","+923337163458","+923337163454","+923337163443","+923337163436","+923337163434","+923337163416","+923337163350","+923337162490","+923337162435","+923337162402","+923337162344","+923337162336","+923337162326","+923337162298","+923337162240","+923337162202","+923337162191","+923337162188","+923337162160","+923337162083","+923337162065","+923337162052","+923337162037","+923337162944","+923337162863","+923337162855","+923337162836","+923337162806","+923337163336","+923337163304","+923337163267","+923337163187","+923337163167","+923337163012","+923337163000","+923337162962","+923337162955","+923337162953","+923337224267","+923337224258","+923337224213","+923337224192","+923337224113","+923337224019","+923337223987","+923337223794","+923337223792","+923337223729","+923337223695","+923337223671","+923337223670","+923337223652","+923337223643","+923337223373","+923337223370","+923337223315","+923337223308","+923337223139","+923337223135","+923337223098","+923337223024","+923337223011","+923337222976","+923337225629","+923337225560","+923337225439","+923337225399","+923337225235","+923337225170","+923337225122","+923337225108","+923337225016","+923337225000","+923337224946","+923337224896","+923337224888","+923337224860","+923337224801","+923337224671","+923337224664","+923337224622","+923337224615","+923337224611","+923337224577","+923337224538","+923337224425","+923337224420","+923337224304","+923310504990","+923310504950","+923310504836","+923310504835","+923310504712","+923310504679","+923310504646","+923310504619","+923310504616","+923310504615","+923310504549","+923310504532","+923310504526","+923310504303","+923361706468","+923318207986","+923315625234","+923318208135","+923323477862","+923322548607","+923354483072","+923341209533","3112204570","+923316917291","+923361706876","+923361650553","+923303733937","+923352139644","+923314357518","+923347078814","+923343574130","+923343954157","+923344197730","+923303731167","+923378241255","+923378241309","+923306468386","+923378212339","3481490762","+923361416135","+923316936792","+923378096432","+923362900321","+923358206414","+923357366427","+923303739378","+923368712326","+923317936527","+923378212319","+923318849743","+923303738795","+923376911877","+923318849844","+923317627519","+923317602953","+923348510284","+923378241423","+923301372781","+923358206518","+923319708727","+923341899865","+923323849920","+923323203983","+923367022092","+923303730602","+923305936016","+923361434559","+923318133182","+923369728154","+923322450241","+923318179757","+923315625611","+923317718366","3162846571","+923353859935","+923340957487","+923351782063","+923378212391","+923354865909","+923366924995","+923318179962","3133265831","+923361650420","+923302926475","+923320124639","+923350298478","+923368709418","+923346709859","+923303829570","+923362897031","+923302922630","+923302922549","+923328227054","+923323793896","+923346388561","+923322527193","+923306051985","+923346026039","+923306476490","+923343573163","+923369316354","+923377642557","+923326905365","+923319709925","+923340752441","+923327075097","+923366924615","+923358175778","+923322457143","+923343574805","+923361435183","3089501321","+923357903467","+923366808960","+923346898059","+923317831293","+923370371024","+923312175359","+923316937965","+923318910317","+923346003721","+923323859134","+923303829565","+923317753024","+923351588155","+923357364882","+923368708981","+923306051768","+923378212340","+923322644632","+923340031505","+923346679145","3402182190","+923362709664","+923313910428","+923346167508","+923340029569","+923369335386","+923342230602","+923347114901","3161819648","+923358154672","+923327446411","+923347416195","+923353268045","+923369709535"]

         mailcount = 0

         numbers = []
         options = webdriver.ChromeOptions()
         # options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')
         options.add_argument("--disable-renderer-backgrounding")
         options.add_argument("--disable-backgrounding-occluded-windows")
         # options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')
         options.add_argument('--load-extension=D:\\autologinbot-master\\Urbanvpn')

         browser = webdriver.Chrome(options=options, use_subprocess=True,version_main=110)


         while (1):




             browser.get(url)


             try:

                 phonee = WebDriverWait(browser, 120).until(
                     EC.presence_of_element_located((By.CSS_SELECTOR,
                                                     '#js_header_demo_registration')))

                 phonee.click()
                 time.sleep(1)
                 phonee = WebDriverWait(browser, 120).until(
                     EC.presence_of_element_located((By.CSS_SELECTOR,
                                                     '#select2-registerpopupform-country-container > span > i')))

                 phonee.click()
                 time.sleep(1)
                 usernap = WebDriverWait(browser, 2).until(
                     EC.presence_of_element_located((By.CSS_SELECTOR, 'body > span > span > span.select2-search.select2-search--dropdown > input')))
                 usernap.send_keys('Pakistan')

                 time.sleep(1)
                 usernap = WebDriverWait(browser, 60).until(
                     EC.presence_of_element_located((By.CSS_SELECTOR, '#select2-registerpopupform-country-results')))
                 usernap.click()
                 time.sleep(1)

                 usernap = WebDriverWait(browser, 60).until(
                     EC.presence_of_element_located((By.CSS_SELECTOR, '#registerpopupform-login')))
                 usernap.send_keys(fnumbers[recount])
                 time.sleep(1)


                 usernap = WebDriverWait(browser, 60).until(
                     EC.presence_of_element_located((By.CSS_SELECTOR, '#registerpopupform-')))
                 usernap.send_keys('')
                 time.sleep(1)
                 usernap = WebDriverWait(browser, 60).until(
                     EC.presence_of_element_located((By.CSS_SELECTOR, '#form_registration > div.field.field_inside_label.js_label_inside.field-registerpopupform-agreement.required.s-focus > div.field_value > div > label')))
                 usernap.click()
                 time.sleep(1)

                 usernap = WebDriverWait(browser, 60).until(
                     EC.presence_of_element_located((By.CSS_SELECTOR, '#form_registration > div.field.field_inside_label.js_label_inside.field-registerpopupform-swap_free.required.s-focus > div.field_value > div > label')))
                 usernap.click()
                 time.sleep(2)
                 usernap = WebDriverWait(browser, 60).until(
                     EC.presence_of_element_located((By.CSS_SELECTOR, '#form_registration > div.button > button')))
                 usernap.click()
                 time.sleep(8)
                 browser.get('https://my.litefinance.org/verification/index')
                 usernap = WebDriverWait(browser, 60).until(
                     EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.page > main > div > section > div > div > div > div > div:nth-child(2) > div.col-5.d-flex.justify-content-end > a')))
                 usernap.click()

                 time.sleep(1)

                 usernap = WebDriverWait(browser, 60).until(
                     EC.presence_of_element_located((By.CSS_SELECTOR, '#usereditform-phone')))
                 #usernap.send_keys(fnumbers[recount])
                 time.sleep(1)
                 usernap = WebDriverWait(browser, 60).until(
                     EC.presence_of_element_located((By.CSS_SELECTOR, '#w0 > div.button > button')))
                 usernap.click()
                 time.sleep(8)
                 browser.delete_all_cookies()
                 count = count + 1
                 if (recount < (len(fnumbers) - 1)):
                     recount = recount + 1
                 else:
                     recount = 0

                 print(count)

















             except  Exception as e:




                 browser.delete_all_cookies()
                 browser.get(url)
 except:




     browser.quit()
     print('exception')

   


     
      


     
     
     
     
  
