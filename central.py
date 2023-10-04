import undetected_chromedriver.v2 as webdriver
from TempMail import TempMail  # imports everything from TempMail library

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
from extension import proxies
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
    domain = "@gmail.com"
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
f=False
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
from extension import proxies


from user_agent import generate_user_agent, generate_navigator


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
recount = 60
total = 0
t = 0
if __name__ == "__main__":
    while (1):

        numb = "0123456789"
        if (total >= 10):
            break

        url = 'https://account.f5.com/partnercentral'

        fnumbers = ["3310504637","3310504636","3310504634","3310504633","3310504630","3310504629","3310504625","3310504624","3310504623","3310504620","3310504618","3310504615","3310504614","3310504612","3310504611","3310504606","3310504603","3310504599","3310504596","3310504595","3310504593","3310504587","3310504582","3310504581","3310504580","3310504575","3310504573","3310504572","3310504571","3310504566","3310504565","3310504563","3310504562","3310504561","3310504560","3310504556","3310504554","3310504553","3310504499","3310504491","3371851139","3371859678","3371852131","3371855824","3371856481","3371851141","3371856687","3371850472","3371853813","3371857003","3371850653","3371852226","3371852685","3371852616","3371853538","3371850473","3371852227","3371859746","3371855586","3371855064","3371850178","3371854882","3371858800","3371850573","3371858990","3371850985","3371856586","3371857486","3371857671","3371856091","3371858909","3371857124","3371855315","3371859352","3371858645","3371851173","3371853630","3371855907","3371858032","3371853782","3371856791","3371858322","3371858001","3371855856","3371853015","3371853657","3371853578","3371855656","3371857283","3371859290","3371852035","3371859125","3371857744","3371851650","3371858378","3371859440","3371859101","3371858257","3371858629","3371853591","3371854102","3371858571","3371852695","3371855397","3371858469","3371856203","3371855992","3371858338","3371859925","3371856966","3371856484","3371857595","3371857031","3371855478","3371858115","3371857397","3371855409","3371854231","3371853534","3371856419","3371857730","3371851535","3371859611","3371859016","3371859304","3371857804","3371853676","3371859066","3371857777","3371856405","3371853588","3371850357","3371850282","3371856418","3371855162","3371851762","3371855504","3371854015","3371851368","3371850728","3371851454","3371854449","3371855207","3371856816","3371855259","3371859039","3371854537","3371856371","3371856456","3371859676","3371858951","3371856352","3371859671","3371856830","3371854262","3371856606","3371852507","3371858107","3371859027","3371853874","3371859072","3371855591","3371858283","3371859615","3371850841","3371853194","3371857477","3371852143","3371856067","3371850911","3371853148","3371859283","3371856584","3371856561","3371853231","3371853975","3371850310","3371858450","3371856383","3371851836","3371852007","3371852599","3371859205","3371855413","3371854376","3371854332","3371857145","3371853394","3371855042","3371859824","3371858041","3371856684","3371857082","3371854511","3371851419","3371851098","3371855449","3371857805","3371857464","3371851874","3371850053","3371858552","3371855950","3371859454","3371852237","3371854372","3371853575","3371855962","3371858603","3371859478","3371850095","3371851896","3371856955","3371854768","3371857147","3371857259","3371852217","3371856370","3371857916","3371851558","3371855301","3371855887","3371852655","3371851397","3371852889","3371851737","3371853432","3371850140","3371851307","3371855428","3371851544","3371855545","3371856263","3371858842","3371855177","3371858096","3371858364","3371855523","3371858574","3371855897","3371854276","3371852063","3371855344","3371850714","3371852595","3371857510","3371852235","3371852994","3371856409","3371855019","3371851324","3371858070","3371859071","3371858443","3371850933","3371857331","3371858707","3371858702","3371859239","3371851815","3371856287","3371850643","3371858970","3371858218","3371856291","3371854699","3371858527","3371859961","3371854163","3371853634","3371856748","3371852869","3371856328","3371855271","3371859706","3371857837","3371858745","3371856426","3371856663","3371857369","3371855646","3371859825","3371857791","3371858486","3371853433","3371851090","3371857912","3371854440","3371856666","3371851212","3371859067","3371856952","3371855104","3371856682","3371850096","3371857162","3371859211","3371859941","3371856516","3371855247","3371855751","3371850587","3371859584","3371858535","3371850870","3371855619","3371856089","3371855431","3371853070","3371855755","3371852290","3371851722","3371859517","3371858313","3371854857","3371857829","3371856372","3371858870","3371854518","3371859977","3371853016","3371851616","3371858720","3371856296","3371855069","3371853074","3371853225","3371853406","3371854828","3371858501","3371858212","3371852104","3371850374","3371855456","3371850122","3371859263","3371854117","3371856571","3371859563","3371859845","3371856386","3371859830","3371858031","3371856471","3371851184","3371855149","3371854149","3371859355","3371852993","3371858658","3371858831","3371855532","3371853850","3371851372","3371855361","3371859390","3371852592","3371853779","3371853121","3371855692","3371856544","3371853854","3371859883","3371855084","3371855991","3371856619","3371855325","3371855894","3371853853","3371856131","3371850963","3371857793","3371854103","3371850072","3371859533","3371850378","3371854769","3371859449","3371851810","3371856881","3371855370","3371850383","3371858279","3371859375","3371859240","3371852750","3371850521","3371853735","3371852262","3371859451","3371858948","3371858680","3371855296","3371853331","3371858864","3371853085","3371850115","3371858955","3304111874","3375356080","3375350708","3375354895","3304118926","3304115186","3304117337","3304111858","3304118504","3375355369","3375350747","3375356154","3304113927","3375353915","3304114903","3304119156","3304117141","3375350167","3375356432","3375351282","3304118002","3304110004","3304115568","3304119379","3375357472","3304119973","3304112034","3375353032","3304117420","3375358324","3375356169","3304110354","3375351109","3304116061","3375358984","3375351307","3304114449","3304111415","3375351595","3375353025","3375356913","3304110999","3375359204","3304113270","3375357532","3375355285","3304114103","3304111291","3304117371","3304113312","3375354450","3304119455","3304113996","3304110228","3304116031","3304114393","3304114050","3304114313","3375353088","3304113451","3304114874","3304111300","3304111339","3375355741","3304118072","3304110504","3304114040","3375351429","3375358534","3375356855","3375354133","3375353974","3375356316","3304115368","3375359171","3304110229","3304110708","3304115778","3304117538","3375356594","3375359818","3375354407","3375353948","3304119738","3304118431","3375358619","3304119804","3375353291","3375352535","3304119708","3304116366","3375352205","3304114791","3375350665","3375357748","3304117074","3304110011","3304111909","3375358027","3375352242","3375358610","3304113453","3304118848","3304116321","3304110974","3375356089","3304119930","3375354985","3375353545","3375358861","3375354909","3375350587","3375358096","3304118792","3304119597","3375355345","3304119228","3375355608","3304113473","3375357792","3304114261","3304114629","3375355631","3304114338","3375359512","3304118623","3304110194","3375357218","3375356049","3304112619","3304116891","3304113355","3304114189","3375358232","3304114209","3375356327","3304119942","3304114029","3375355372","3304115702","3304113965","3375350367","3375358457","3304115485","3304110361","3304112693","3375354619","3304115518","3375352116","3304114212","3375354626","3304118887","3375357617","3304113767","3375358424","3375351636","3304117935","3304115318","3304119475","3304111860","3375350829","3304112649","3304116105","3304112774","3375358391","3304113769","3304113762","3375355662","3375358920","3304112782","3375356313","3304112553","3304115980","3375356613","3304113924","3304115593","3304119774","3304113109","3304115641","3375359019","3304110241","3304119492","3375355893","3304116710","3304112757","3375356183","3304110704","3304111169","3375353629","3304117456","3304118168","3304118359","3375354804","3304116547","3304117520","3304117712","3375352602","3304117863","3304110457","3375352584","3304111426","3375355049","3304118183","3304115546","3375356701","3304110679","3375352128","3375359101","3375351324","3304114886","3304117855","3375352521","3375355519","3304112418","3304113494","3304112027","3375355794","3304114510","3304116644","3375353548","3304116303","3375357123","3375353748","3375358656","3304112865","3304116673","3304119183","3304117298","3375350204","3304115384","3375354576","3375355511","3375358192","3304117717","3375350378","3375351691","3304110190","3304112068","3304115015","3375353041","3304113093","3375356015","3304114859","3304110124","3375359324","3304118561","3375355398","3375353029","3375353569","3304114309","3375353565","3375358968","3375351929","3304112796","3304114527","3304110025","3304114774","3304116850","3304114943","3375354001","3304111012","3375355937","3375356702","3375357813","3375352661","3304112197","3304115547","3375355279","3304117759","3304114284","3304115745","3375351454","3304112627","3304116170","3304112572","3304119570","3304113933","3375358155","3375353535","3304117526","3375352576","3375357650","3304111736","3375351533","3304118704","3375358632","3304110125","3304112567","3304117135","3375356291","3304113366","3304111671","3304115607","3375357395","3304117362","3304118781","3304116447","3304110146","3375356436","3375353427","3304113472","3304115041","3304114271","3304119523","3304115700","3375359381","3375359918","3375357154","3375355595","3375352586","3375353580","3375355472","3375350785","3304111137","3304112692","3304119881","3375354602","3375350683","3375359602","3304117784","3304119253","3375356481","3375356499","3375350540","3304113410","3375350093","3375352211","3375355845","3304110209","3304115698","3375355648","3375357002","3375355787","3304116338","3375355194","3375357206","3375350156","3304119319","3304113419","3375354424","3304114195","3375353936","3304117112","3375350215","3304111931","3304114253","3304113797","3304119590","3304113070","3375356975","3304113652","3375358390","3375358243","3304116137","3304119132","3304115066","3304119962","3304119694","3304119042","3375356067","3304116337","3375356272","3375354786","3375352444","3375359865","3375355260","3375356955","3304112462","3304115010","3375356804","3304116153","3375359125","3375350956","3375351613","3375355515","3304119136","3304116201","3375359717","3304110812","3304115701","3375354185","3304113274","3304113749","3375351018","3375351549","3375350861","3375356180","3304115479","3304110314","3375352072","3304116466","3375351755","3375353061","3375359853","3304111101","3375351817","3375351754","3375356502","3304116410","3304113411","3375356730","3375357512","3375353918","3375350177","3304118774","3375353985","3304113824","3304114255","3375350882","3304119422","3304119373","3304119792","3304119781","3375352621","3304111907","3304113150","3375355880","3304112153","3304114672","3304114262","3375353973","3375356037","3304118747","3375353434","3375354443","3375353752","3304112151","3375351831","3375359997","3375359334","3375357762","3375351861","3304110689","3375357221","3304119166","3375359556","3304116389","3375352244","3304116220","3375358766","3375355599","3375359106","3375353081","3375353850","3375358911","3304115491","3304113293","3375353777","3304111045","3375358025","3375357773","3375352052","3304112825","3375356739","3375355410","3304117590","3375359776","3375356767","3375353771","3304115507","3304114946","3304110317","3304111178","3375353688","3375350234","3304118814","3375354748","3304118235","3375357488","3375353248","3304118456","3375353186","3375356841","3304118953","3304110934","3304112469","3375351232","3304110855","3304117365","3304111718","3375359434","3375359440","3375357667","3375351604","3304119025","3304116874","3375351529","3375354776","3304117020","3304118165","3304110289","3304116709","3304112135","3375359032","3304114707","3304110079","3375350874","3304110966","3304115804","3375357343","3304114926","3304116021","3304116123","3304114285","3375355548","3375359868","3375356469","3304115345","3375356648","3375357041","3304113063","3375352189","3375353669","3375356706","3304114392","3304117180","3304118694","3375358796","3375350522","3304113185","3304117343","3304119284","3375357455","3375357754","3304118839","3304117864","3375351998","3304110548","3304113663","3304110536","3304112878","3304116290","3375358675","3375359169","3304112807","3375351681","3304113544","3304112356","3304111220","3304115183","3375350811","3304113202","3375351795","3304110697","3375352063","3375356349","3375356700","3375356177","3375359644","3375355652","3304111306","3375353444","3304117149","3375351848","3375358251","3304115349","3375351357","3375352923","3304117367","3375354721","3375359788","3304118010","3304119625","3375359286","3375358807","3304111355","3304111465","3375357288","3375352810","3304114699","3304116609","3304118973","3375355343","3304112876","3304117264","3304111989","3304111246","3304116163","3304110429","3304117530","3304118588","3304118687","3375355711","3375359337","3304114837","3304118427","3304111489","3375356302","3304118140","3375359084","3375358742","3304115789","3304117608","3375357075","3304117247","3375355241","3375352600","3375359584","3304110084","3375352791","3304112872","3375350430","3375355154","3375356696","3375358536","3304110251","3375357172","3375351068","3375358372","3304116266","3304119200","3375357393","3375358338","3304113306","3304118376","3375351643","3375353392","3375351408","3304110286","3304112801","3304110586","3304111760","3375355629","3304118770","3375353886","3375358176","3375351396","3304113667","3304116412","3304119655","3304119260","3304115284","3304118969","3375357769","3375353526","3375354792","3304119545","3304113402","3304115295","3304110031","3304118769","3304117340","3375352336","3304114073","3375355350","3375352846","3304116280","3304117707","3304113330","3375359028","3375353306","3304116755","3304112239","3304116963","3375355277","3375356875","3304116595","3304118046","3375353065","3375355294","3375353737","3375352157","3304117968","3375350231","3304112887","3304114880","3304119377","3304112399","3304118900","3304112970","3375354479","3304118989","3304110682","3304114422","3304119959","3304117747","3304110458","3375356075","3304112556","3375353423","3304110027","3375356821","3375354258","3375352228","3304111557","3304113408","3304115250","3304110698","3375356691","3304116606","3375354328","3304112905","3375355566","3375358313","3304112735","3304113879","3304115838","3304114061","3304116658","3375354754","3304111813","3375357991","3304115739","3375357359","3304112180","3375356476","3375350208","3375353903","3375354867","3304112351","3304112682","3375359109","3304113196","3375358896","3375359943","3375359007","3304114159","3375355400","3375357648","3375353117","3375356458","3375353311","3375357824","3375359550","3375358882","3375351576","3375356850","3304113133","3304113935","3304112238","3304115571","3304113283","3304114844","3304111996","3375350173","3375350182","3375356326","3304113994","3375355060","3375355767","3375355691","3375355916","3375355268","3375359712","3375353026","3304113938","3375353119","3304111067","3375354381","3304112733","3304116557","3304111399","3304116913","3304118388","3304117065","3375352995","3304114415","3304115622","3375350453","3375350055","3304119101","3375357510","3304115297","3304117723","3304119458","3375358471","3304114162","3375357864","3304115078","3304113644","3304115975","3304113395","3304112795","3304118153","3304115852","3375357772","3375351860","3304112322","3304118578","3304117216","3375355569","3375350290","3375358343","3375359122","3304118300","3375351664","3304119658","3375351032","3304114409","3304111122","3375353206","3304111952","3375357854","3304112152","3375357853","3304116790","3375356057","3304113273","3304114624","3375351802","3304113421","3375356287","3304116589","3304110749","3304112081","3304119056","3304118482","3304116630","3375356470","3304118420","3375352284","3375355851","3304112361","3375352626","3375354506","3304111550","3375353641","3375358965","3375359628","3304118626","3304117441","3304117943","3304115292","3304110492","3304113738","3304117504","3375353084","3375358444","3375356864","3304114885","3375353816","3304113455","3375350616","3304115457","3375353764","3375355367","3375355553","3375357056","3304111115","3375353018","3304113846","3375355806","3375358959","3375350449","3375356275","3375350318","3375350675","3375354970","3375351372","3375357811","3375358848","3375359217","3375359174","3304116932","3304118067","3304110358","3375354022","3375352505","3304113888","3375357833","3375351540","3304113227","3304118022","3304115857","3304116225","3375353274","3304119304","3304119656","3304110416","3375354313","3375357685","3304119991","3375359485","3375354307","3304113794","3375356194","3375358071","3375353606","3304115776","3375353994","3304116334","3375353245","3375357328","3304112233","3375355772","3375358480","3304118081","3375357611","3304111645","3375359263","3304117854","3375352490","3304113780","3304118205","3375356097","3304116597","3304110197","3304110753","3304111026","3375354926","3304110707","3304114863","3375354546","3375354788","3304114134","3304110824","3304114515","3375357179","3304116700","3304116707","3304117681","3304114258","3304112465","3304116525","3304117138","3304112106","3375355723","3375355574","3304111590","3304116267","3375354577","3375351624","3375354405","3304111593","3375355104","3375350289","3375357040","3375358019","3304115519","3304110088","3375350762","3375350275","3304112969","3304112055","3375353933","3304115522","3375359973","3304118474","3375350789","3304110424","3304110297","3304110613","3304114411","3375358854","3375355592","3375351431","3304111190","3304116717","3375355163","3304110722","3304112470","3304114673","3304116649","3375352613","3375357826","3375352009","3304116212","3375350153","3375353300","3304116741","3304119944","3375352878","3375354644","3304114889","3304116096","3375354991","3304117055","3375356647","3375351198","3375356106","3375359971","3304114214","3375357414","3375354089","3304114172","3304110721","3304113623","3304111212","3304113665","3304111958","3375355558","3375358860","3304119015","3375352395","3375359281","3304112004","3375359764","3375358618","3304110945","3375351057","3375357794","3304119793","3375353962","3304119918","3304116776","3375350198","3304110418","3375351421","3304119128","3375352193","3375354435","3304112060","3304115665","3375356284","3304111646","3375352871","3375359922","3304116953","3375353622","3304115064","3375353705","3304118285","3375354921","3375350210","3304114403","3375354706","3304113197","3304112092","3304119280","3375358302","3375358850","3304116463","3375350912","3375357447","3304112900","3375350684","3304113688","3375350913","3375357281","3304119928","3304116817","3375351138","3304117778","3375356919","3375355657","3304111921","3375355905","3375354400","3304118378","3375354415","3375350642","3304110677","3304118409","3375350724","3375355635","3375352380","3375353458","3375355052","3304110736","3375354392","3375357314","3375359100","3375356399","3375353099","3304115356","3375352963","3375354565","3304110353","3375353258","3375351954","3375358901","3375353758","3304110984","3375357890","3304115416","3375354889","3304119622","3304117705","3375354879","3375351593","3304118612","3375356606","3375354171","3304114168","3304116798","3375358894","3304115377","3304113850","3304116358","3304110528","3304115866","3304112524","3304115283","3304118320","3375354150","3304111123","3304110859","3375357429","3375353849","3304113211","3375354597","3304119635","3375353882","3375353365","3375355039","3304119331","3375353167","3304119512","3304111559","3304118590","3304113772","3375355327"]

       #fnumbers = fnumbers[::-1]
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
                username = 'user-sphm1kztal-sessionduration-1'
                 = 'ohdKQ8aHJnig7v87it'
                endpoint = 'pk.smartproxy.com'
                port = '10010'

                proxies_extension = proxies(username, , endpoint, port)

                options.add_argument(
                    '--load-extension=D:\\autologinbot-master\\chromium_automation,D:\\autologinbot-master\\WISE\\APPLE\\proxies_extension')
                # options.add_argument(
                #    '--user-agent='+ag)

                #options.add_extension(proxies_extension)
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
                        browser.delete_all_cookies()


                        browser.get(
                            'https://www.google.com/search?client=opera-gx&q=textanywhere&sourceid=opera&ie=UTF-8&oe=UTF-8')
                        time.sleep(2)
                        browser.get(url)
                        inbox = TempMail.generateInbox()
                        print("Email Address: " + inbox.address)
                        number = '1898879786'
                        num_emails = 1
                        email = ''

                        unique_emails = set()
                        while len(unique_emails) < num_emails:
                            emails = generate_random_email()
                            unique_emails.add(emails)

                        for emails in unique_emails:
                            email = emails
                            print(email)

                        while (1):

                            browser.get('https://account.f5.com/partnercentral/signin/register')
                            time.sleep(2000)
                            try:
                             usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                '/html/body/div[2]/div/div/div/div[2]/main/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/span/input'))).send_keys('')
                             usernap = WebDriverWait(browser, 25).until(
                                 EC.presence_of_element_located((By.XPATH,
                                                                 '/html/body/div[2]/div/div/div/div[2]/main/div[2]/div/div/form/div[1]/div[2]/div[2]/div[2]/span/input'))).send_keys('zahid')
                            except:
                                print(a)
                                pass
                            time.sleep(2)


                            usernap = WebDriverWait(browser, 155).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                '/html/body/div[2]/div/div/div/div[2]/main/div[2]/div/div/form/div[1]/div[2]/div[3]/div[2]/span/input'))).send_keys(inbox.address)

                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                '/html/body/div[2]/div/div/div/div[2]/main/div[2]/div/div/form/div[1]/div[2]/div[5]/div[2]/span/input'))).send_keys('jamal@123J')
                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '/html/body/div[2]/div/div/div/div[2]/main/div[2]/div/div/form/div[2]/input'))).click()


                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#l-body > div > div > div.span-17 > div > div > p:nth-child(2) > a'))).click()

                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#l-body > div > div > div.span-17 > div > div > p:nth-child(2) > a'))).click()

                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#l-body > div > div > div.span-17 > div > div > p:nth-child(2) > a'))).click()

                            while (1):
                                usernap = WebDriverWait(browser, 25).until(
                                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                    '#new_one_time__profile > div.form-control-group > div > div.span-10 > div'))).click()
                                time.sleep(1)

                                usernap = WebDriverWait(browser, 60).until(
                                    EC.presence_of_element_located((By.XPATH,
                                                                    '//div[@class="custom-select-item-with-helper-country-flag flag-pk"]')))
                                usernap.click()
                                time.sleep(0.5)

                                usernap = WebDriverWait(browser, 25).until(
                                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        '#one_time__profile_telephone_number')))
                                usernap.send_keys(fnumbers[recount])


                                usernap = WebDriverWait(browser, 25).until(
                                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                    '#new_one_time__profile > div.one-time--profile-setup-security-questions > div:nth-child(3) > div > div.custom-select-value.form-input')))
                                usernap.click()


                                time.sleep(2)
                                # usernap = WebDriverWait(browser, 25).until(
                                #    EC.presence_of_element_located((By.XPATH,
                                #                                    '/html/body/div[1]/div[1]/main/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/span/select/option[162]'))).click()

                                usernap = WebDriverWait(browser, 25).until(
                                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                    '#new_one_time__profile > div.one-time--profile-setup-security-questions > div:nth-child(3) > div > div.custom-select-options > div:nth-child(2)'))).click()

                                usernap = WebDriverWait(browser, 25).until(
                                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                    '#one_time__profile_security_question_1_answer')))
                                usernap.send_keys('jamaligeerg')


                                usernap = WebDriverWait(browser, 10).until(
                                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                    '#new_one_time__profile > div.one-time--profile-setup-security-questions > div:nth-child(4) > div > div.custom-select-value.form-input'))).click()
                                usernap = WebDriverWait(browser, 25).until(
                                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                    '#new_one_time__profile > div.one-time--profile-setup-security-questions > div:nth-child(4) > div > div.custom-select-options > div:nth-child(3)')))
                                usernap.click()
                                usernap = WebDriverWait(browser, 25).until(
                                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                    '#one_time__profile_security_question_2_answer')))
                                usernap.send_keys('jamalireger')

                                usernap = WebDriverWait(browser, 10).until(
                                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                    '#new_one_time__profile > div.one-time--profile-setup-security-questions > div:nth-child(5) > div'))).click()
                                usernap = WebDriverWait(browser, 25).until(
                                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                    '#new_one_time__profile > div.one-time--profile-setup-security-questions > div:nth-child(5) > div > div.custom-select-options > div:nth-child(4)')))
                                usernap.click()
                                usernap = WebDriverWait(browser, 25).until(
                                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                    '#one_time__profile_security_question_3_answer')))
                                usernap.send_keys('jamaligerge')
                                usernap = WebDriverWait(browser, 25).until(
                                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                    '#new_one_time__profile > div.form-buttons > button')))
                                usernap.click( )

                                for i in range(3):
                                 time.sleep(3)
                                 usernap = WebDriverWait(browser, 25).until(
                                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                    '#l-body > div > div > div > div > form > div.one-time--profile-authenticate-secondary-actions')))
                                 usernap.click()

                                browser.get('https://app.delighted.com/one_time__profile/new')

                                time.sleep(2)

                                count += 1

                                print(count)
                                if(count%2==0):
                                    print(a)
                                if (recount < (len(fnumbers) - 1)):
                                    recount = recount + 1
                                else:
                                    recount = 0


























                    except  Exception as e:







                        browser.delete_all_cookies()


                        if (recount < (len(fnumbers) - 1)):
                            recount = recount + 1
                        else:
                            recount = 0

            except:



                browser.quit()
                print('biggest exception')
