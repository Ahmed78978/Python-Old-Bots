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

        url = 'https://www.textanywhere.com/pricing/'

        fnumbers = ["03310504637","03310504636","03310504634","03310504633","03310504630","03310504629","03310504625","03310504624","03310504623","03310504620","03310504618","03310504615","03310504614","03310504612","03310504611","03310504606","03310504603","03310504599","03310504596","03310504595","03310504593","03310504587","03310504582","03310504581","03310504580","03310504575","03310504573","03310504572","03310504571","03310504566","03310504565","03310504563","03310504562","03310504561","03310504560","03310504556","03310504554","03310504553","03310504499","03310504491","03371851139","03371859678","03371852131","03371855824","03371856481","03371851141","03371856687","03371850472","03371853813","03371857003","03371850653","03371852226","03371852685","03371852616","03371853538","03371850473","03371852227","03371859746","03371855586","03371855064","03371850178","03371854882","03371858800","03371850573","03371858990","03371850985","03371856586","03371857486","03371857671","03371856091","03371858909","03371857124","03371855315","03371859352","03371858645","03371851173","03371853630","03371855907","03371858032","03371853782","03371856791","03371858322","03371858001","03371855856","03371853015","03371853657","03371853578","03371855656","03371857283","03371859290","03371852035","03371859125","03371857744","03371851650","03371858378","03371859440","03371859101","03371858257","03371858629","03371853591","03371854102","03371858571","03371852695","03371855397","03371858469","03371856203","03371855992","03371858338","03371859925","03371856966","03371856484","03371857595","03371857031","03371855478","03371858115","03371857397","03371855409","03371854231","03371853534","03371856419","03371857730","03371851535","03371859611","03371859016","03371859304","03371857804","03371853676","03371859066","03371857777","03371856405","03371853588","03371850357","03371850282","03371856418","03371855162","03371851762","03371855504","03371854015","03371851368","03371850728","03371851454","03371854449","03371855207","03371856816","03371855259","03371859039","03371854537","03371856371","03371856456","03371859676","03371858951","03371856352","03371859671","03371856830","03371854262","03371856606","03371852507","03371858107","03371859027","03371853874","03371859072","03371855591","03371858283","03371859615","03371850841","03371853194","03371857477","03371852143","03371856067","03371850911","03371853148","03371859283","03371856584","03371856561","03371853231","03371853975","03371850310","03371858450","03371856383","03371851836","03371852007","03371852599","03371859205","03371855413","03371854376","03371854332","03371857145","03371853394","03371855042","03371859824","03371858041","03371856684","03371857082","03371854511","03371851419","03371851098","03371855449","03371857805","03371857464","03371851874","03371850053","03371858552","03371855950","03371859454","03371852237","03371854372","03371853575","03371855962","03371858603","03371859478","03371850095","03371851896","03371856955","03371854768","03371857147","03371857259","03371852217","03371856370","03371857916","03371851558","03371855301","03371855887","03371852655","03371851397","03371852889","03371851737","03371853432","03371850140","03371851307","03371855428","03371851544","03371855545","03371856263","03371858842","03371855177","03371858096","03371858364","03371855523","03371858574","03371855897","03371854276","03371852063","03371855344","03371850714","03371852595","03371857510","03371852235","03371852994","03371856409","03371855019","03371851324","03371858070","03371859071","03371858443","03371850933","03371857331","03371858707","03371858702","03371859239","03371851815","03371856287","03371850643","03371858970","03371858218","03371856291","03371854699","03371858527","03371859961","03371854163","03371853634","03371856748","03371852869","03371856328","03371855271","03371859706","03371857837","03371858745","03371856426","03371856663","03371857369","03371855646","03371859825","03371857791","03371858486","03371853433","03371851090","03371857912","03371854440","03371856666","03371851212","03371859067","03371856952","03371855104","03371856682","03371850096","03371857162","03371859211","03371859941","03371856516","03371855247","03371855751","03371850587","03371859584","03371858535","03371850870","03371855619","03371856089","03371855431","03371853070","03371855755","03371852290","03371851722","03371859517","03371858313","03371854857","03371857829","03371856372","03371858870","03371854518","03371859977","03371853016","03371851616","03371858720","03371856296","03371855069","03371853074","03371853225","03371853406","03371854828","03371858501","03371858212","03371852104","03371850374","03371855456","03371850122","03371859263","03371854117","03371856571","03371859563","03371859845","03371856386","03371859830","03371858031","03371856471","03371851184","03371855149","03371854149","03371859355","03371852993","03371858658","03371858831","03371855532","03371853850","03371851372","03371855361","03371859390","03371852592","03371853779","03371853121","03371855692","03371856544","03371853854","03371859883","03371855084","03371855991","03371856619","03371855325","03371855894","03371853853","03371856131","03371850963","03371857793","03371854103","03371850072","03371859533","03371850378","03371854769","03371859449","03371851810","03371856881","03371855370","03371850383","03371858279","03371859375","03371859240","03371852750","03371850521","03371853735","03371852262","03371859451","03371858948","03371858680","03371855296","03371853331","03371858864","03371853085","03371850115","03371858955","03304111874","03375356080","03375350708","03375354895","03304118926","03304115186","03304117337","03304111858","03304118504","03375355369","03375350747","03375356154","03304113927","03375353915","03304114903","03304119156","03304117141","03375350167","03375356432","03375351282","03304118002","03304110004","03304115568","03304119379","03375357472","03304119973","03304112034","03375353032","03304117420","03375358324","03375356169","03304110354","03375351109","03304116061","03375358984","03375351307","03304114449","03304111415","03375351595","03375353025","03375356913","03304110999","03375359204","03304113270","03375357532","03375355285","03304114103","03304111291","03304117371","03304113312","03375354450","03304119455","03304113996","03304110228","03304116031","03304114393","03304114050","03304114313","03375353088","03304113451","03304114874","03304111300","03304111339","03375355741","03304118072","03304110504","03304114040","03375351429","03375358534","03375356855","03375354133","03375353974","03375356316","03304115368","03375359171","03304110229","03304110708","03304115778","03304117538","03375356594","03375359818","03375354407","03375353948","03304119738","03304118431","03375358619","03304119804","03375353291","03375352535","03304119708","03304116366","03375352205","03304114791","03375350665","03375357748","03304117074","03304110011","03304111909","03375358027","03375352242","03375358610","03304113453","03304118848","03304116321","03304110974","03375356089","03304119930","03375354985","03375353545","03375358861","03375354909","03375350587","03375358096","03304118792","03304119597","03375355345","03304119228","03375355608","03304113473","03375357792","03304114261","03304114629","03375355631","03304114338","03375359512","03304118623","03304110194","03375357218","03375356049","03304112619","03304116891","03304113355","03304114189","03375358232","03304114209","03375356327","03304119942","03304114029","03375355372","03304115702","03304113965","03375350367","03375358457","03304115485","03304110361","03304112693","03375354619","03304115518","03375352116","03304114212","03375354626","03304118887","03375357617","03304113767","03375358424","03375351636","03304117935","03304115318","03304119475","03304111860","03375350829","03304112649","03304116105","03304112774","03375358391","03304113769","03304113762","03375355662","03375358920","03304112782","03375356313","03304112553","03304115980","03375356613","03304113924","03304115593","03304119774","03304113109","03304115641","03375359019","03304110241","03304119492","03375355893","03304116710","03304112757","03375356183","03304110704","03304111169","03375353629","03304117456","03304118168","03304118359","03375354804","03304116547","03304117520","03304117712","03375352602","03304117863","03304110457","03375352584","03304111426","03375355049","03304118183","03304115546","03375356701","03304110679","03375352128","03375359101","03375351324","03304114886","03304117855","03375352521","03375355519","03304112418","03304113494","03304112027","03375355794","03304114510","03304116644","03375353548","03304116303","03375357123","03375353748","03375358656","03304112865","03304116673","03304119183","03304117298","03375350204","03304115384","03375354576","03375355511","03375358192","03304117717","03375350378","03375351691","03304110190","03304112068","03304115015","03375353041","03304113093","03375356015","03304114859","03304110124","03375359324","03304118561","03375355398","03375353029","03375353569","03304114309","03375353565","03375358968","03375351929","03304112796","03304114527","03304110025","03304114774","03304116850","03304114943","03375354001","03304111012","03375355937","03375356702","03375357813","03375352661","03304112197","03304115547","03375355279","03304117759","03304114284","03304115745","03375351454","03304112627","03304116170","03304112572","03304119570","03304113933","03375358155","03375353535","03304117526","03375352576","03375357650","03304111736","03375351533","03304118704","03375358632","03304110125","03304112567","03304117135","03375356291","03304113366","03304111671","03304115607","03375357395","03304117362","03304118781","03304116447","03304110146","03375356436","03375353427","03304113472","03304115041","03304114271","03304119523","03304115700","03375359381","03375359918","03375357154","03375355595","03375352586","03375353580","03375355472","03375350785","03304111137","03304112692","03304119881","03375354602","03375350683","03375359602","03304117784","03304119253","03375356481","03375356499","03375350540","03304113410","03375350093","03375352211","03375355845","03304110209","03304115698","03375355648","03375357002","03375355787","03304116338","03375355194","03375357206","03375350156","03304119319","03304113419","03375354424","03304114195","03375353936","03304117112","03375350215","03304111931","03304114253","03304113797","03304119590","03304113070","03375356975","03304113652","03375358390","03375358243","03304116137","03304119132","03304115066","03304119962","03304119694","03304119042","03375356067","03304116337","03375356272","03375354786","03375352444","03375359865","03375355260","03375356955","03304112462","03304115010","03375356804","03304116153","03375359125","03375350956","03375351613","03375355515","03304119136","03304116201","03375359717","03304110812","03304115701","03375354185","03304113274","03304113749","03375351018","03375351549","03375350861","03375356180","03304115479","03304110314","03375352072","03304116466","03375351755","03375353061","03375359853","03304111101","03375351817","03375351754","03375356502","03304116410","03304113411","03375356730","03375357512","03375353918","03375350177","03304118774","03375353985","03304113824","03304114255","03375350882","03304119422","03304119373","03304119792","03304119781","03375352621","03304111907","03304113150","03375355880","03304112153","03304114672","03304114262","03375353973","03375356037","03304118747","03375353434","03375354443","03375353752","03304112151","03375351831","03375359997","03375359334","03375357762","03375351861","03304110689","03375357221","03304119166","03375359556","03304116389","03375352244","03304116220","03375358766","03375355599","03375359106","03375353081","03375353850","03375358911","03304115491","03304113293","03375353777","03304111045","03375358025","03375357773","03375352052","03304112825","03375356739","03375355410","03304117590","03375359776","03375356767","03375353771","03304115507","03304114946","03304110317","03304111178","03375353688","03375350234","03304118814","03375354748","03304118235","03375357488","03375353248","03304118456","03375353186","03375356841","03304118953","03304110934","03304112469","03375351232","03304110855","03304117365","03304111718","03375359434","03375359440","03375357667","03375351604","03304119025","03304116874","03375351529","03375354776","03304117020","03304118165","03304110289","03304116709","03304112135","03375359032","03304114707","03304110079","03375350874","03304110966","03304115804","03375357343","03304114926","03304116021","03304116123","03304114285","03375355548","03375359868","03375356469","03304115345","03375356648","03375357041","03304113063","03375352189","03375353669","03375356706","03304114392","03304117180","03304118694","03375358796","03375350522","03304113185","03304117343","03304119284","03375357455","03375357754","03304118839","03304117864","03375351998","03304110548","03304113663","03304110536","03304112878","03304116290","03375358675","03375359169","03304112807","03375351681","03304113544","03304112356","03304111220","03304115183","03375350811","03304113202","03375351795","03304110697","03375352063","03375356349","03375356700","03375356177","03375359644","03375355652","03304111306","03375353444","03304117149","03375351848","03375358251","03304115349","03375351357","03375352923","03304117367","03375354721","03375359788","03304118010","03304119625","03375359286","03375358807","03304111355","03304111465","03375357288","03375352810","03304114699","03304116609","03304118973","03375355343","03304112876","03304117264","03304111989","03304111246","03304116163","03304110429","03304117530","03304118588","03304118687","03375355711","03375359337","03304114837","03304118427","03304111489","03375356302","03304118140","03375359084","03375358742","03304115789","03304117608","03375357075","03304117247","03375355241","03375352600","03375359584","03304110084","03375352791","03304112872","03375350430","03375355154","03375356696","03375358536","03304110251","03375357172","03375351068","03375358372","03304116266","03304119200","03375357393","03375358338","03304113306","03304118376","03375351643","03375353392","03375351408","03304110286","03304112801","03304110586","03304111760","03375355629","03304118770","03375353886","03375358176","03375351396","03304113667","03304116412","03304119655","03304119260","03304115284","03304118969","03375357769","03375353526","03375354792","03304119545","03304113402","03304115295","03304110031","03304118769","03304117340","03375352336","03304114073","03375355350","03375352846","03304116280","03304117707","03304113330","03375359028","03375353306","03304116755","03304112239","03304116963","03375355277","03375356875","03304116595","03304118046","03375353065","03375355294","03375353737","03375352157","03304117968","03375350231","03304112887","03304114880","03304119377","03304112399","03304118900","03304112970","03375354479","03304118989","03304110682","03304114422","03304119959","03304117747","03304110458","03375356075","03304112556","03375353423","03304110027","03375356821","03375354258","03375352228","03304111557","03304113408","03304115250","03304110698","03375356691","03304116606","03375354328","03304112905","03375355566","03375358313","03304112735","03304113879","03304115838","03304114061","03304116658","03375354754","03304111813","03375357991","03304115739","03375357359","03304112180","03375356476","03375350208","03375353903","03375354867","03304112351","03304112682","03375359109","03304113196","03375358896","03375359943","03375359007","03304114159","03375355400","03375357648","03375353117","03375356458","03375353311","03375357824","03375359550","03375358882","03375351576","03375356850","03304113133","03304113935","03304112238","03304115571","03304113283","03304114844","03304111996","03375350173","03375350182","03375356326","03304113994","03375355060","03375355767","03375355691","03375355916","03375355268","03375359712","03375353026","03304113938","03375353119","03304111067","03375354381","03304112733","03304116557","03304111399","03304116913","03304118388","03304117065","03375352995","03304114415","03304115622","03375350453","03375350055","03304119101","03375357510","03304115297","03304117723","03304119458","03375358471","03304114162","03375357864","03304115078","03304113644","03304115975","03304113395","03304112795","03304118153","03304115852","03375357772","03375351860","03304112322","03304118578","03304117216","03375355569","03375350290","03375358343","03375359122","03304118300","03375351664","03304119658","03375351032","03304114409","03304111122","03375353206","03304111952","03375357854","03304112152","03375357853","03304116790","03375356057","03304113273","03304114624","03375351802","03304113421","03375356287","03304116589","03304110749","03304112081","03304119056","03304118482","03304116630","03375356470","03304118420","03375352284","03375355851","03304112361","03375352626","03375354506","03304111550","03375353641","03375358965","03375359628","03304118626","03304117441","03304117943","03304115292","03304110492","03304113738","03304117504","03375353084","03375358444","03375356864","03304114885","03375353816","03304113455","03375350616","03304115457","03375353764","03375355367","03375355553","03375357056","03304111115","03375353018","03304113846","03375355806","03375358959","03375350449","03375356275","03375350318","03375350675","03375354970","03375351372","03375357811","03375358848","03375359217","03375359174","03304116932","03304118067","03304110358","03375354022","03375352505","03304113888","03375357833","03375351540","03304113227","03304118022","03304115857","03304116225","03375353274","03304119304","03304119656","03304110416","03375354313","03375357685","03304119991","03375359485","03375354307","03304113794","03375356194","03375358071","03375353606","03304115776","03375353994","03304116334","03375353245","03375357328","03304112233","03375355772","03375358480","03304118081","03375357611","03304111645","03375359263","03304117854","03375352490","03304113780","03304118205","03375356097","03304116597","03304110197","03304110753","03304111026","03375354926","03304110707","03304114863","03375354546","03375354788","03304114134","03304110824","03304114515","03375357179","03304116700","03304116707","03304117681","03304114258","03304112465","03304116525","03304117138","03304112106","03375355723","03375355574","03304111590","03304116267","03375354577","03375351624","03375354405","03304111593","03375355104","03375350289","03375357040","03375358019","03304115519","03304110088","03375350762","03375350275","03304112969","03304112055","03375353933","03304115522","03375359973","03304118474","03375350789","03304110424","03304110297","03304110613","03304114411","03375358854","03375355592","03375351431","03304111190","03304116717","03375355163","03304110722","03304112470","03304114673","03304116649","03375352613","03375357826","03375352009","03304116212","03375350153","03375353300","03304116741","03304119944","03375352878","03375354644","03304114889","03304116096","03375354991","03304117055","03375356647","03375351198","03375356106","03375359971","03304114214","03375357414","03375354089","03304114172","03304110721","03304113623","03304111212","03304113665","03304111958","03375355558","03375358860","03304119015","03375352395","03375359281","03304112004","03375359764","03375358618","03304110945","03375351057","03375357794","03304119793","03375353962","03304119918","03304116776","03375350198","03304110418","03375351421","03304119128","03375352193","03375354435","03304112060","03304115665","03375356284","03304111646","03375352871","03375359922","03304116953","03375353622","03304115064","03375353705","03304118285","03375354921","03375350210","03304114403","03375354706","03304113197","03304112092","03304119280","03375358302","03375358850","03304116463","03375350912","03375357447","03304112900","03375350684","03304113688","03375350913","03375357281","03304119928","03304116817","03375351138","03304117778","03375356919","03375355657","03304111921","03375355905","03375354400","03304118378","03375354415","03375350642","03304110677","03304118409","03375350724","03375355635","03375352380","03375353458","03375355052","03304110736","03375354392","03375357314","03375359100","03375356399","03375353099","03304115356","03375352963","03375354565","03304110353","03375353258","03375351954","03375358901","03375353758","03304110984","03375357890","03304115416","03375354889","03304119622","03304117705","03375354879","03375351593","03304118612","03375356606","03375354171","03304114168","03304116798","03375358894","03304115377","03304113850","03304116358","03304110528","03304115866","03304112524","03304115283","03304118320","03375354150","03304111123","03304110859","03375357429","03375353849","03304113211","03375354597","03304119635","03375353882","03375353365","03375355039","03304119331","03375353167","03304119512","03304111559","03304118590","03304113772","03375355327"]

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
                endpoint = 'pk.smartproxy.com'
                port = '10010'

                proxies_extension = proxies(username, , endpoint, port)

                options.add_argument(
                    '--load-extension=D:\\autologinbot-master\\chromium_automation,D:\\autologinbot-master\\fingerprint,D:\\autologinbot-master\\buster')
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
                        browser.delete_all_cookies()


                        browser.get(
                            'https://www.google.com/search?client=opera-gx&q=textanywhere&sourceid=opera&ie=UTF-8&oe=UTF-8')

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

                            browser.get('https://www.textanywhere.com/action/free-trial/')
                            time.sleep(2)
                            try:
                             usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#ccc-notify-accept'))).click()
                            except:
                                print('a')
                                pass
                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#name'))).send_keys('')
                            time.sleep(0.5)

                            usernap = WebDriverWait(browser, 155).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#company'))).send_keys(email)
                            time.sleep(0.5)

                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#email')))
                            text_to_type = email

                            # Send the keys one by one with a delay to simulate human typing
                            for char in text_to_type:
                                usernap.send_keys(char)
                                time.sleep(0.1)
                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#'))).send_keys('jamal@123J')
                            time.sleep(2)


                            usernap = WebDriverWait(browser, 60).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#terms')))
                            usernap.click()
                            time.sleep(0.5)
                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                'body > div.container > main > div > div > div:nth-child(5) > div > div > div > div > form > div.wp-block-commify-button.text-center.my-0 > button')))
                            usernap.click()

                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                'body > div.container > main > div > div > div:nth-child(5) > div > div > div > div > form > div.input-group > div > div > div')))
                            usernap.click()
                            time.sleep(0.5)
                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#iti-item-pk'))).click()

                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#phone')))
                            text_to_type = fnumbers[recount]

                            # Send the keys one by one with a delay to simulate human typing
                            for char in text_to_type:
                                usernap.send_keys(char)
                                time.sleep(0.1)
                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                'body > div.container > main > div > div > div:nth-child(5) > div > div > div > div > form > div.wp-block-commify-button.text-center.mt-4 > button')))
                            usernap.click()

                            usernap = WebDriverWait(browser, 205).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#code')))
                            time.sleep(5)
                            headers = {
                                "Host": "smart.telcotest.net",
                                "Cookie": "CELLSID=808384a9c5ef4396472d16c903291b8c; TZ=-300,0; TZM=Asia/Karachi",
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36",
                                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                                "Referer": "https://smart.telcotest.net/sms",
                                "Accept-Encoding": "gzip, deflate",
                                "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
                                "Connection": "close"
                            }

                            number_as_string = str(fnumbers[recount])

                            # Remove the first digit by slicing the string
                            new_number_as_string = number_as_string[1:]

                            phone_number = '92' + new_number_as_string  # Replace this with the desired phone number

                            url = f"https://smart.telcotest.net/sms?sms_to=%2B{phone_number}&dup=2&sms_time_start=&sms_time_end=&count=1000&order=id%3Adesc"
                            print(url)

                            response = requests.get(url, headers=headers)
                            soup = BeautifulSoup(response.content, 'html.parser')
                            table = soup.find('table', class_='table table-hover')
                            digit_code = ''

                            if table:
                                rows = table.find_all('tr')
                                if len(rows) > 1:  # Check if there's at least one data row
                                    first_data_row = rows[1]  # Skip the header row
                                    columns = first_data_row.find_all(['td', 'th'])
                                    row_data = [column.text.strip() for column in columns]
                                    print(row_data)
                                    print(row_data[7])
                                    pattern = r'\d+'  # Regular expression pattern to match one or more digits

                                    matches = re.findall(pattern, row_data[7])
                                    if matches:
                                        digit_code = matches[0]
                                        print("Extracted Digit Code:", digit_code)
                                    else:
                                        print("No digit code found in the line.")
                                else:
                                    print("No data rows found in the table.")
                            else:
                                print("Could not find the specified table.")

                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#code')))
                            usernap.send_keys(digit_code)
                            time.sleep(0.5)
                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                'body > div.container > main > div > div > div:nth-child(5) > div > div > div > div > form > div.wp-block-commify-button.text-center > button')))
                            usernap.click()
                            time.sleep(0.5)
                            try:
                                usernap = WebDriverWait(browser,10).until(
                                    EC.presence_of_element_located((By.XPATH,
                                                                    '//div[@class="errorMessage"]')))
                                if (recount < (len(fnumbers) - 1)):
                                    recount = recount + 1
                                else:
                                    recount = 0
                                count += 1
                                print(count)
                                break
                            except:
                                pass

                            browser.get('https://app.textanywhere.com/login')
                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#username')))
                            text_to_type = email

                            # Send the keys one by one with a delay to simulate human typing
                            for char in text_to_type:
                                usernap.send_keys(char)
                                time.sleep(0.1)
                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#')))
                            usernap.send_keys('jamal@123J')
                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#main-container > wsb-login-component > div > div:nth-child(4) > div > div > div > form > wsb-atlas-button:nth-child(4) > button')))
                            usernap.click()
                            time.sleep(2)
                            browser.get('https://app.textanywhere.com/sms/sendTrial')
                            c=0
                            while(1):
                                if(c>=16):
                                    print(a)
                                new_length = random.choice([4, 5, 6])
                                new_code = generate_verification_code(new_length)

                                usernap = WebDriverWait(browser, 25).until(
                                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                    '#sms-textarea')))
                                usernap.send_keys('Your Verification code is ' + new_code)
                                time.sleep(2)
                                usernap = WebDriverWait(browser, 25).until(
                                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                    '#main-container > wsb-send > div > div > form > div:nth-child(4) > wsb-atlas-button:nth-child(2) > button')))
                                usernap.click()
                                time.sleep(1)
                                usernap = WebDriverWait(browser, 25).until(
                                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                    '#body > ngb-modal-window > div > div > wsb-modal > div.modal-footer.ng-star-inserted > div.ng-star-inserted > wsb-atlas-button:nth-child(2) > button')))
                                usernap.click()
                                time.sleep(2)
                                browser.refresh()
                                count += 1
                                print(count)
                                if (count % 10 == 0):
                                    f = True
                                c += 1



















                    except  Exception as e:
                        count += 1
                        if (f == True):
                            f = False
                            print(a)



                        browser.delete_all_cookies()


                        if (recount < (len(fnumbers) - 1)):
                            recount = recount + 1
                        else:
                            recount = 0

            except:



                browser.quit()
                print('biggest exception')
