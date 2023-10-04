import undetected_chromedriver.v2 as webdriver
from tempmail import EMail

import re
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
from apiclient import discovery
from apiclient import errors
from httplib2 import Http
from oauth2client import file, client, tools
import base64
from bs4 import BeautifulSoup
import re
import time
import dateutil.parser as parser
from datetime import datetime
import datetime
import csv
import email
import imaplib

user = ['i.nfokamalhmed@gmail.com', 'in.fokamalhmed@gmail.com', 'inf.okamalhmed@gmail.com', 'info.kamalhmed@gmail.com',
        'infok.amalhmed@gmail.com', 'infoka.malhmed@gmail.com', 'infokam.alhmed@gmail.com', 'infokama.lhmed@gmail.com',
        'infokamal.hmed@gmail.com', 'infokamalh.med@gmail.com', 'infokamalhm.ed@gmail.com', 'infokamalhme.d@gmail.com',
        'a.hmedinfozahid@gmail.com', 'ah.medinfozahid@gmail.com', 'ahm.edinfozahid@gmail.com',
        'ahme.dinfozahid@gmail.com', '.infozahid@gmail.com', 'i.nfozahid@gmail.com',
        'in.fozahid@gmail.com', 'inf.ozahid@gmail.com', 'info.zahid@gmail.com',
        'infoz.ahid@gmail.com', 'infoza.hid@gmail.com', 'infozah.id@gmail.com',
        'infozahi.d@gmail.com', 'i.nfotelcotestahymed@gmail.com', 'in.fotelcotestahymed@gmail.com',
        'inf.otelcotestahymed@gmail.com', 'info.telcotestahymed@gmail.com', 'infot.elcotestahymed@gmail.com',
        'infote.lcotestahymed@gmail.com', 'infotel.cotestahymed@gmail.com', 'infotelc.otestahymed@gmail.com',
        'infotelco.testahymed@gmail.com', 'infotelcot.estahymed@gmail.com', 'infotelcote.stahymed@gmail.com',
        'infotelcotes.tahymed@gmail.com', 'infotelcotest.ahymed@gmail.com', 'infotelcotesta.hymed@gmail.com',
        'infotelcotestah.ymed@gmail.com', 'infotelcotestahy.med@gmail.com', 'infotelcotestahym.ed@gmail.com',
        'infotelcotestahyme.d@gmail.com', 'i.nfokaiengeering@gmail.com', 'in.fokaiengeering@gmail.com',
        'inf.okaiengeering@gmail.com', 'info.kaiengeering@gmail.com', 'infok.aiengeering@gmail.com',
        'infoka.iengeering@gmail.com', 'infokai.engeering@gmail.com', 'infokaie.ngeering@gmail.com',
        'infokaien.geering@gmail.com', 'infokaieng.eering@gmail.com', 'infokaienge.ering@gmail.com',
        'infokaiengee.ring@gmail.com', 'infokaiengeer.ing@gmail.com', 'infokaiengeeri.ng@gmail.com',
        'infokaiengeerin.g@gmail.com', 'infokaiengeering.@gmail.com', 'infokaiengeeringa.hmed@gmail.com',
        'infokaiengeeringah.med@gmail.com', 'infokaiengeeringahm.ed@gmail.com', 'infokaiengeeringahme.d@gmail.com',
        'i.nforipha@gmail.com', 'in.foripha@gmail.com', 'inf.oripha@gmail.com',
        'info.ripha@gmail.com', 'infor.ipha@gmail.com', 'infori.pha@gmail.com',
        'inforip.ha@gmail.com', 'inforiph.a@gmail.com', 'inforipha.@gmail.com',
        'inforiphaa.hmed@gmail.com', 'inforiphaah.med@gmail.com', 'inforiphaahm.ed@gmail.com',
        'inforiphaahme.d@gmail.com']
gmail_pass = ['exbbdrfxhdedqngi', 'exbbdrfxhdedqngi', 'exbbdrfxhdedqngi', 'exbbdrfxhdedqngi', 'exbbdrfxhdedqngi',
              'exbbdrfxhdedqngi', 'exbbdrfxhdedqngi', 'exbbdrfxhdedqngi', 'exbbdrfxhdedqngi', 'exbbdrfxhdedqngi',
              'exbbdrfxhdedqngi', 'exbbdrfxhdedqngi', 'txplsxbiunzycygq', 'txplsxbiunzycygq', 'txplsxbiunzycygq',
              'txplsxbiunzycygq', 'txplsxbiunzycygq', 'txplsxbiunzycygq', 'txplsxbiunzycygq', 'txplsxbiunzycygq',
              'txplsxbiunzycygq', 'txplsxbiunzycygq', 'txplsxbiunzycygq', 'txplsxbiunzycygq', 'txplsxbiunzycygq',
              'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid',
              'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid',
              'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid',
              'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx',
              'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx',
              'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx',
              'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx',
              'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'hbyswscrqygdwnoc', 'hbyswscrqygdwnoc',
              'hbyswscrqygdwnoc', 'hbyswscrqygdwnoc', 'hbyswscrqygdwnoc', 'hbyswscrqygdwnoc', 'hbyswscrqygdwnoc',
              'hbyswscrqygdwnoc', 'hbyswscrqygdwnoc', 'hbyswscrqygdwnoc', 'hbyswscrqygdwnoc', 'hbyswscrqygdwnoc',
              'hbyswscrqygdwnoc']

host = "imap.gmail.com"


# Creating a storage.JSON file with authentication details
def delete_cache(driver):
    driver.switch_to.window(driver.window_handles[-1])  # Switch window to the second tab
    driver.get('chrome://settings/clearBrowserData')  # Open your chrome settings.
    perform_actions(driver,
                    Keys.TAB * 2 + Keys.DOWN * 4 + Keys.TAB * 7 + Keys.ENTER)  # Tab to the time select and key down to say "All Time" then go to the Confirm button and press Enter


def perform_actions(driver, keys):
    actions = ActionChains(driver)
    actions.send_keys(keys)
    time.sleep(25)
    print('Performing Actions!')
    actions.perform()


def get_total_emails(mai):
    # Create server and login
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(user[mai], gmail_pass[mai])

    # Using SELECT to choose the INBOX folder
    mail.select("INBOX")

    # Get the total number of emails in the INBOX folder
    _, response = mail.search(None, "0ALL")
    return len(response[0].split())


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_verification_code(length):
    return ''.join(random.choices('0123456789', k=length))
def generate_random_email():
    username_length = random.randint(5, 10)
    domain = "@"+generate_random_string(username_length)+".com"
    username = generate_random_string(username_length)
    email = username + domain
    return email


def read_email_from_gmail(count=1, contain_body=True, mai=0):
    # Create server and login
    mail = imaplib.IMAP4_SSL(host)
    mail.login(user[mai], gmail_pass[mai])

    # Using SELECT to chose the e-mails.
    res, messages = mail.select('INBOX')

    # Caluclating the total number of sent Emails
    messages = int(messages[0])

    # Iterating over the sent emails
    for i in range(messages, messages - count, -1):
        # RFC822 protocol
        res, msg = mail.fetch(str(i), "0(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])

                # Store the senders email
                sender = msg["From"]

                # Store subject of the email
                subject = msg["Subject"]

                # Store Body
                body = ""
                temp = msg
                if temp.is_multipart():
                    for part in temp.walk():
                        content_type = part.get_content_type()
                        if "text/plain" in content_type or "text/html" in content_type:
                            charset = part.get_content_charset()
                            body = part.get_payload(decode=True).decode(charset)
                            break
                else:
                    body = temp.get_payload(decode=True).decode(temp.get_content_charset())

                # Print Sender, Subject, Body
                print("-" * 50)  # To divide the messages
                print("From    : ", sender)
                print("Subject : ", subject)
                if (contain_body):
                    print("Body    : ", body)
                    return body


import time
import random
import string
from user_agent import generate_user_agent, generate_navigator
from extension import proxies

def generate_unique_username(base_name="user"):
    # Using the current timestamp (to the microsecond) to ensure uniqueness
    timestamp = str(int(time.time() * 1000000))

    # Generate a random string of 5 characters for added uniqueness
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=30))

    return f"{base_name}_{random_str}_{timestamp}"


def convertTuple(tup):
    strc = ''
    c = len(tup)

    for item in range(25):
        strc = strc + strc.join(tup[item])

    return strc


letters = string.ascii_lowercase
usernameStr = ['zahidkamal78978@gmail.com', 'zahid60@gmail.com', '78978@gmail.com']

Str = ''

from selenium.webdriver.chrome import service

mobile_emulation = {"deviceName": "iPhone SE"}
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
count = 0
recount = 20
total = 0
t = 0
if __name__ == "__main__":
    while (1):

        numb = "0123456789"
        if (total >= 10):
            break

        url = 'https://get.checkfront.com/start/'

        fnumbers = ["3352628810","3362301004","3363959595","3345142631","3355469077","3337353429","3333225353","3363480355","3349081886","3319692443","3300792049","3317455868","3312497145","3366154014","3366618812","3329318723","3335540871","3330503839","3306438216","3358740101","3360736895","3364683690","3317446026","3329355075","3351581387","3317073734","3379233650","3345557510","3322763377","3337889913","3368631992","3356439899","3306910101","3347863434","3314316013","3333352007","3364198004","3359257022","3359287244","3343388053","3325863550","3349191221","3376180390","3326232746","3328130868","3330417378","3352367897","3345119881","3346377390","3342862326","3335346073","3357137760","3365754450","3363298506","3334492703","3318857549","3337861414","3324416273","3314737936","3334348894","3300792210","3326172241","3336589780","3346209218","3346889664","3317397805","3364799001","3352740259","3302881044","3304154265","3300329019","3349443048","3366051410","3325158799","3312317585","3315305905","3335737453","3338507935","3353830247","3331002006","3361281077","3357905531","3361655600","3343660649","3335597242","3362249895","3340340021","3328224321","3369184959","3358768700","3343926222","3335456500","3378093069","3308260816","3344979366","3337784947","3319087652","3367003632","3368948034","3330727321","3330519924","3330519883","3330519827","3330519811","3330519794","3330519787","3330519693","3330519606","3330519594","3330519569","3330519564","3330519511","3330519503","3330519323","3330519319","3330519244","3330519243","3330519145","3330519011","3330518998","3330518901","3330518872","3330518788","3330518773","3330518723","3330518566","3330518512","3330518488","3330518377","3330518334","3330518319","3330518133","3330518129","3330518121","3330518092","3330517961","3330517958","3330517934","3330517930","3330517888","3330517738","3330517563","3330517498","3330517492","3330517311","3330517275","3330517268","3330517122","3330517046","3330516950","3330516712","3330516702","3330516649","3330516356","3330516345","3330516314","3330516298","3330516295","3330516055","3330516035","3330516007","3330515948","3330515874","3330515854","3330515811","3330515733","3330515722","3330515681","3330515587","3330515546","3330515464","3330515451","3330515342","3330515254","3330515073","3330515064","3330515006","3330515003","3330514995","3330514972","3330514903","3330514726","3330514704","3330514667","3330514634","3330514588","3330514527","3330514525","3330514414","3330514351","3330514330","3330514262","3330514094","3330514082","3330513953","3330513935","3330513851","3330513824","3330513688","3330513607","3330513593","3330513576","3330513434","3330513337","3330513311","3330513301","3330513150","3330512930","3330512567","3330512367","3330512308","3330512241","3330511983","3330511943","3330511921","3330511878","3330511867","3330511818","3330511785","3330511777","3330511735","3330511451","3330511328","3330511299","3330511271","3330510943","3330510901","3330510840","3330510820","3330510786","3330510581","3330510491","3330510486","3330510399","3330510375","3330510368","3330510347","3330510291","3330510267","3330510257","3330509923","3330509762","3330509714","3330509700","3330509689","3330509669","3330509631","3330509540","3330509514","3330509332","3330509245","3330509160","3330509088","3330509071","3330509067","3330509060","3330508950","3330508933","3330508871","3330508791","3330508657","3330508578","3330508529","3330508505","3330508461","3330508436","3330508429","3330508376","3330508317","3330508289","3330508277","3330508242","3330508220","3330508192","3330508178","3330508047","3330507962","3330507883","3330507865","3330507752","3330507595","3330507551","3330507367","3330507260","3330507151","3330507131","3330507119","3330506980","3330506957","3330506863","3330506832","3330506818","3330506806","3330506791","3330506784","3330506766","3330506575","3330506525","3330506473","3330506415","","3329717578","3329717527","3329717505","3329717444","3329717402","3329717401","3329717375","3329717207","3329717112","3329717089","3329717043","3329716972","3329716930","3329716912","3329716875","3329716869","3329716847","3329716817","3329716779","3329716775","3329716718","3329716695","3329716569","3329716565","3329716555","3329716548","3329716485","3329716389","3329716342","3329716334","3329716322","3329716316","3329716299","3329716292","3329716161","3329716155","3329716112","3329715903","3329715884","3329715858","3329715839","3329715763","3329715743","3329715661","3329715616","3329715581","3329715570","3329715553","3329715276","3329715264","3329715017","3329714950","3329714938","3329714885","3329714874","3329714872","3329714780","3329714505","3329714487","3329714466","3329714294","3329714233","3329714147","3329714124","3329714072","3329714023","3329714009","3329714002","3329713988","3329713905","3329713858","3329713847","3329713840","3329713815","3329713778","3329713744","3329713719","3329713676","3329713639","3329713581","3329713516","3329713481","3329713311","3329713269","3329713238","3329713219","3329713205","3329713033","3329712921","3329712906","3329712855","3329712766","3329712738","3329712686","3329712665","3329712647","3329712578","3329712445","3329712404","3329712397","3329712393","3329712390","3329712288","3329712232","3329712215","3329712202","3329712179","3329712118","3329712094","3329712046","3329711915","3329711893","3329711864","3329711804","3329711766","3329711541","3329711535","3329711522","3329711516","3329711490","3329711480","3329711423","3329711325","3329711226","3329711222","3329711200","3329711092","3329711023","3329710998","3329710956","3329710939","3329710860","3329710774","3329710765","3329710694","3329710667","3329710562","3329710544","3329710464","3329710346","3329709898","3329709882","3329709849","3329709775","3329709719","3329709672","3329709620","3329709605","3329709600","3329709596","3329709561","3329709501","3329709454","3329709424","3329709393","3329709185","3329709178","3329708593","3329708584","3329708581","3329708571","3329708558","3329708534","3329708525","3329708501","3329708478","3329708364","3329708222","3329708037","3329708027","3329707913","3329707860","3329707853","3329707796","3329707762","3329707750","3329707728","3329707716","3329707685","3329707662","3329707636","3329707494","3329707421","3329707338","3329707212","3329707167","3329707142","3329707129","3329707110","3329707109","3329707058","3329706984","3329706802","3329706794","3329706673","3329706658","3329706644","3329706635","3329706634","3329706615","3329682194","3329682181","3329682041","3329682037","3329682032","3329681948","3329681905","3329681789","3329681689","3329681611","3329681518","3329681446","3329681331","3329681198","3329681162","3329681102","3329681083","3329681031","3329680918","3329680770","3329680681","3329680566","3329680526","3329680517","3329680504","3329680493","3329680469","3329680405","3329680367","3329680350","3329680341","3329680319","3329680278","3329680246","3329680235","3329680138","3329680110","3329680107","3329679985","3329679975","3329679949","3329679923","3329679920","3329679919","3329679892","3329679830","3329679644","3329679616","3329679579","3329679521","3329679484","3329679397","3329679395","3329679388","3329679372","3329679360","3329679322","3329679301","3329679280","3329679227","3329679207","3329679193","3329679183","3329679179","3329679172","3329679134","3329679059","3329679021","3329678937","3329678867","3329678847","3329678842","3329678787","3329678752","3329678728","3329678676","3329678633","3329678610","3329678564","3329678551","3329678529","3329678505","3329678476","3329678459","3329678310","3329678159","3329678151","3329678138","3329678031","3329678025","3329678000","3329677988","3329677963","3329677932","3329677892","3329677851","3329677812","3329677740","3329677714","3329677662"]

        fnumbers = fnumbers[::-1]
        # random.shuffle(fnumbers)
        mailcount = 0

        numbers = []
        mai = random.randint(0, len(user) - 1)

        while (1):
            if (total >= 10):
                break
            try:
                options = webdriver.ChromeOptions()
                # options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')
                ag = str(generate_user_agent('win'))
                print(ag)


                options.add_argument("--disable-renderer-backgrounding")
                options.add_argument("--disable-backgrounding-occluded-windows")
                # profile_directory = 'C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 4'
                # options.add_argument(f'user-data-dir={profile_directory}')
                username = 'sphm1kztal'
                 = 'ohdKQ8aHJnig7v87it'
                endpoint = 'gate.smartproxy.com'
                port = '10010'

                proxies_extension = proxies(username, , endpoint, port)

                options.add_argument(
                    '--load-extension=D:\\autologinbot-master\\chromium_automation,D:\\autologinbot-master\\fingerprint,D:\\autologinbot-master\\buster,D:\\autologinbot-master\\WISE\\APPLE\\proxies_extension')
                # options.add_argument(
                #    '--user-agent='+ag)

                # options.add_extension(proxies_extension)
                browser = webdriver.Chrome(options=options)


                # profile_directory = 'C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 4'
                # options.add_argument(f'user-data-dir={profile_directory}')
                # options.add_argument('--load-extension=D:\\autologinbot-master\\surf')


                # = webdriver.Chrome(options=options)
                i = random.randint(2, 57)
                inb = 'infozahid@gmail.com'


                while (1):

                    try:

                        print('h')
                        email = EMail()
                        print(email.address)
                        m = email.address

                        browser.delete_all_cookies()


                        browser.get(
                            'https://www.google.com/search?client=opera-gx&q=textanywhere&sourceid=opera&ie=UTF-8&oe=UTF-8')





                        while (1):

                            browser.get(url)
                            #browser.refresh()

                            try:
                             usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#firstName'))).send_keys('')
                            except:
                                print('a')
                                pass
                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#lastName'))).send_keys('zahid')


                            usernap = WebDriverWait(browser, 155).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#email'))).send_keys(m)


                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#')))
                            text_to_type = 'jamal@123J'

                            # Send the keys one by one with a delay to simulate human typing
                            for char in text_to_type:
                                usernap.send_keys(char)
                                time.sleep(0.1)
                            time.sleep(5)
                            while(1):
                                try:
                                    usernap = WebDriverWait(browser, 25).until(
                                        EC.presence_of_element_located((By.XPATH,
                                                                        '/html/body/div[2]/div[2]/div[1]/div/div[1]/div/form/div[5]/button')))
                                    browser.execute_script("arguments[0].click();", usernap)


                                    print('a')
                                    break

                                except:
                                    browser.get(url)
                                    # browser.refresh()

                                    try:
                                        usernap = WebDriverWait(browser, 25).until(
                                            EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                            '#firstName'))).send_keys('')
                                    except:
                                        print('a')
                                        pass
                                    usernap = WebDriverWait(browser, 25).until(
                                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        '#lastName'))).send_keys('zahid')

                                    usernap = WebDriverWait(browser, 155).until(
                                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        '#email'))).send_keys(m)

                                    usernap = WebDriverWait(browser, 25).until(
                                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        '#')))
                                    text_to_type = 'jamal@123J'

                                    # Send the keys one by one with a delay to simulate human typing
                                    for char in text_to_type:
                                        usernap.send_keys(char)
                                        time.sleep(0.1)

                                    button_element = WebDriverWait(browser, 10).until(
                                        EC.element_to_be_clickable((By.XPATH,
                                                                    "//button[contains(@class, 'create-account')]//span[text()='Create my account']"))).click()
                                    break

                            time.sleep(2)


                            usernap = WebDriverWait(browser, 60).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                '/html/body/div[2]/div[2]/div[1]/form/div/div[2]/div/div[1]/div/div[2]/div')))
                            usernap.click()
                            time.sleep(1)
                            time.sleep(5)
                            usernap = WebDriverWait(browser, 60).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                '/html/body/div[2]/div[2]/div[1]/form/div/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div[2]/input'))).send_keys('staff'+Keys.ENTER)

                            action= ActionChains(browser)
                            action.send_keys(Keys.RETURN)
                            time.sleep(5)



                            time.sleep(3)
                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                '/html/body/div[2]/div[2]/div[1]/form/div/div[2]/div/div[2]/div/label[1]')))
                            usernap.click()
                            time.sleep(5)
                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                '/html/body/div[2]/div[2]/div[1]/form/div/div[2]/div/div[4]/div/div/label[2]')))
                            usernap.click()
                            time.sleep(5)
                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                '/html/body/div[2]/div[2]/div[1]/form/div/div[2]/div/div[6]/div[1]'))).click()
                            time.sleep(5)
                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                '/html/body/div[2]/div[2]/div[1]/form/div/div[2]/div/div[8]/div[2]/button')))
                            usernap.click()
                            time.sleep(5)
                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                '/html/body/div[2]/div[2]/div[1]/form/div/div[2]/div/div[1]/div/label[2]')))
                            usernap.click()
                            time.sleep(5)
                            username_length = random.randint(5, 10)
                            usernap = WebDriverWait(browser, 205).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                '/html/body/div[2]/div[2]/div[1]/form/div/div[2]/div/div[2]/div[2]/input'))).send_keys( "user"+ generate_random_string(username_length))
                            time.sleep(3)
                            usernap = WebDriverWait(browser, 205).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                '/html/body/div[2]/div[2]/div[1]/form/div/div[2]/div/div[4]/div[2]/button'))).click()
                            msg = email.wait_for_message()
                            print(msg)


                            pattern = r'href="(https://user[^"]+)"'

                            # Use re.findall to extract all matches of the pattern
                            matches = re.findall(pattern, msg.body)


                            link = matches[0]
                            browser.get(link)
                            time.sleep(5)
                            base_url = link.split('.com')[0]  # Extract everything before .com
                            new_link = base_url + '.com/account/'
                            browser.get(new_link)
                            button_element = WebDriverWait(browser, 20).until(
                                EC.element_to_be_clickable((By.XPATH, "//button[text()='Account Settings']"))).click()

                            time.sleep(2)


                            checkbox_element = WebDriverWait(browser, 10).until(
                                EC.element_to_be_clickable((By.NAME, "twoFactorEnabled")))
                            browser.execute_script("arguments[0].click();", checkbox_element)
                            time.sleep(1)
                            time.sleep(5)

                            try:
                             usernap = WebDriverWait(browser, 10).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                '/html/body/div[6]/div[2]/div/div[3]/div/div/div/button[2]'))).click()
                            except:
                                button_element = WebDriverWait(browser, 10).until(
                                    EC.element_to_be_clickable((By.XPATH,
                                                                "//button[contains(@class, 'Button__primary')]//span[text()='Save']"))).click()

                            time.sleep(1)
                            usernap = WebDriverWait(browser, 205).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                '/html/body/main/section/div/div/div/form/div[2]/div/div[1]/div/input'))).send_keys(
                                m)
                            time.sleep(1)
                            time.sleep(5)
                            usernap = WebDriverWait(browser, 205).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                '/html/body/main/section/div/div/div/form/div[2]/div/div[2]/div/input'))).send_keys(
                                'jamal@123J')
                            time.sleep(2)
                            usernap = WebDriverWait(browser, 205).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                '/html/body/main/section/div/div/div/form/div[3]/button'))).click()
                            time.sleep(1)
                            time.sleep(5)
                            usernap = WebDriverWait(browser, 205).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                '/html/body/main/section/div/div/div/div[3]/form/button'))).click()
                            time.sleep(2)
                            usernap = WebDriverWait(browser, 205).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                '/html/body/main/section/div/div/div/ul/li[2]/form/button'))).click()
                            time.sleep(1)
                            time.sleep(5)
                            usernap = WebDriverWait(browser, 205).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                '/html/body/main/section/div/div/div/div[1]/div/form[1]/button'))).click()
                            time.sleep(2)
                            usernap = WebDriverWait(browser, 205).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                '/html/body/main/section/div/div/div/ul/li[169]/form/button'))).click()  # pakistan 169
                            time.sleep(1)
                            time.sleep(5)
                            while(1):
                                usernap = WebDriverWait(browser, 205).until(
                                    EC.presence_of_element_located((By.XPATH,
                                                                    '/html/body/main/section/div/div/div/div[1]/div/form[2]/div[1]/div/div/div/input')))
                                usernap.send_keys(Keys.CONTROL+'a')
                                usernap.send_keys(
                                    fnumbers[recount])
                                time.sleep(2)
                                usernap = WebDriverWait(browser, 205).until(
                                    EC.presence_of_element_located((By.XPATH,
                                                                    '/html/body/main/section/div/div/div/div[1]/div/form[2]/div[2]/button'))).click()
                                time.sleep(5)
                                usernap = WebDriverWait(browser, 205).until(
                                    EC.presence_of_element_located((By.XPATH,
                                                                    '/html/body/main/section/div/div/div/div[1]/div/div[1]/div/a'))).click()
                                time.sleep(1)

                                if (recount < (len(fnumbers) - 1)):
                                    recount = recount + 1
                                else:
                                    recount = 0
                                count += 1
                                print(count)
                                if(count!=0):
                                    if(count%10==0):
                                        print(a)





















                    except  Exception as e:








                        browser.delete_all_cookies()


                        if (recount < (len(fnumbers) - 1)):
                            recount = recount + 1
                        else:
                            recount = 0

            except:







                browser.quit()
                print('biggest exception')
