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

        url = 'https://login.nandos.co.uk/signin/register'

        fnumbers = ["3304110689","3375357221","3304119166","3375359556","3304116389","3375352244","3304116220","3375358766","3375355599","3375357621","3304115927","3375353604","3304118490","3375352040","3375354437","3375358148","3304119592","3375352727","3375352346","3304116648","3304112134","3304114772","3375356197","3375353229","3375359645","3304112007","3375355833","3375355891","3375355761","3304112316","3304116056","3304119536","3304119172","3304118993","3304116571","3375359889","3304114714","3375359491","3304117494","3375350331","3304116506","3304116715","3304119700","3304117288","3304113493","3304115478","3375354755","3304117277","3304113694","3375352253","3304113092","3304116714","3375351064","3375356060","3304119782","3375353866","3304112012","3304113019","3304116943","3375353932","3375351394","3375350348","3304112338","3304114026","3375352860","3375358167","3375357663","3304110408","3375355626","3375359005","3375351075","3375353217","3375358331","3304115239","3304112967","3375353631","3375359991","3304110947","3375354911","3304113456","3304115367","3304114514","3304114701","3375353052","3375355166","3375358112","3304117648","3304112800","3304112926","3375350327","3375351942","3375353375","3375355223","3304111983","3375359996","3375352850","3304117022","3304112043","3375357330","3304113633","3375351579","3375354439","3304112078","3304110880","3304113952","3375354038","3304114667","3304117779","3304114406","3304113246","3304118720","3375354999","3304112277","3375351400","3375356543","3304118202","3375350681","3375359396","3304116404","3375358917","3304118283","3375355073","3375358785","3375352059","3304112769","3304110771","3304111185","3375353476","3304118080","3375354750","3375350129","3375350741","3375351410","3375352416","3304117818","3375351278","3304112655","3375350054","3375359417","3304114720","3304115310","3375354342","3304113089","3375359406","3375356276","3304116952","3304118563","3375358062","3375353894","3375352779","3304115586","3304112242","3304117111","3304118349","3304113010","3375357523","3375355441","3375352914","3375351804","3304110935","3375355898","3304111127","3304113572","3375356533","3375358624","3375350588","3375352974","3375353745","3304116423","3375358819","3375357835","3375357922","3375355912","3375356716","3304111932","3304119889","3304112762","3304115117","3304113595","3375350424","3375351011","3304115300","3304112103","3304114544","3304113049","3304113213","3375354612","3375357747","3304110766","3375355269","3375350584","3375355370","3375357462","3375359260","3304113964","3304117659","3304110875","3304111269","3375354325","3375355889","3375353150","3304113900","3304119980","3375358180","3304114513","3304114583","3304117706","3375356496","3375358308","3375353867","3375351563","3375352234","3304116578","3304116663","3375357142","3304111866","3304112360","3375351744","3375352527","3375350186","3304110167","3375358958","3304113307","3375354760","3304111649","3375351099","3375353249","3375350155","3375359153","3304118925","3375352198","3375355213","3304114789","3304113504","3304115231","3304114319","3375352668","3304116840","3375355361","3375350575","3304115161","3304113497","3304114423","3304117733","3375359042","3304119861","3304116182","3304116209","3304111608","3375355759","3375351140","3304112998","3304114111","3375352117","3375354283","3304111581","3304118991","3375353202","3304111226","3375352443","3304113776","3304111176","3304115486","3304111543","3375356483","3304114853","3304112812","3304119163","3304118029","3304113426","3304117740","3375352350","3375359769","3375358694","3375359876","3304116115","3375351775","3304113737","3375356164","3375359257","3304114459","3304117177","3375354347","3375352771","3304115564","3375351121","3304117230","3375359437","3375351527","3304110494","3304114947","3304117731","3304118976","3375359045","3375352348","3304111992","3375351938","3304113583","3304119704","3375351846","3375355456","3304115207","3304110885","3375357837","3375351780","3375354178","3375352579","3375354085","3375353133","3304114666","3304110585","3304114694","3375352106","3304119190","3375356131","3304114025","3304119873","3375354241","3304116886","3375358137","3375353590","3375356461","3304117928","3304117727","3304116503","3375357692","3375352436","3304118365","3304117057","3304111352","3304119641","3375357767","3375359753","3375359814","3375357832","3375354917","3304116291","3304118377","3304118215","3304117449","3304119527","3304112923","3304111609","3304112313","3304112764","3375352107","3375351150","3375355729","3375359852","3304118069","3375357076","3304117644","3375358599","3375358233","3375352977","3304116660","3304118382","3304119144","3304112502","3375351672","3375351716","3375351291","3375357672","3375352002","3304118749","3304113173","3375350017","3375351420","3304117861","3304117948","3375353845","3304118402","3304113458","3304110126","3304114746","3375357277","3304111830","3375359576","3304112698","3375350949","3304115328","3304112513","3375356079","3375355331","3375359198","3375355588","3375352623","3375354056","3304113175","3375354397","3375358113","3304114658","3304110198","3375354761","3304117109","3304117115","3304115655","3375351063","3375358716","3375351302","3375355831","3304114290","3375350016","3375353649","3375352360","3304110451","3375353642","3375352580","3304110203","3375353494","3375359480","3375352953","3304119610","3375359020","3375354120","3304114034","3375358928","3375354837","3304119346","3375354971","3375352783","3375353059","3375353799","3304119299","3304111299","3375355636","3375350573","3304115335","3375350899","3375354952","3375355984","3375356370","3304119906","3304110044","3304116370","3304113862","3304117244","3375352276","3304116348","3375358931","3375355611","3375352669","3375355450","3375353717","3375351971","3304119103","3304119749","3375353724","3375358393","3375357743","3304113601","3304119375","3304118357","3375358298","3304113690","3375359791","3304114072","3375354583","3375352738","3304115987","3375353454","3375359614","3304117790","3375352243","3375354982","3375356838","3304116314","3304113828","3304112775","3375355125","3304114473","3304118838","3304119167","3375358669","3304111775","3375351569","3304114949","3304119259","3375359819","3375353355","3375355222","3375351678","3304118876","3304113464","3304119813","3304118278","3304110865","3375358726","3375353697","3304110427","3304113970","3375359570","3304114174","3304118257","3375353614","3304110630","3304110996","3375350049","3304116010","3304113860","3375354463","3375350386","3304110274","3375358879","3375353147","3304119528","3304111060","3375351476","3304119205","3375357235","3304117720","3375352246","3304114447","3304115661","3375350183","3375354046","3304110918","3375354229","3375350413","3304119817","3375352396","3375357234","3304113566","3304111683","3375351435","3304118174","3375353428","3375355002","3375351866","3304118755","3375359750","3304115180","3375357224","3375354953","3375352996","3375358915","3304110769","3375353750","3304116386","3304117461","3375356070","3304118632","3375353738","3375359046","3375354631","3375359288","3304115833","3375351506","3304118493","3375357585","3375355864","3304118026","3375353462","3375353542","3375353131","3375352263","3304110919","3375357959","3304116752","3304119754","3304110191","3304118315","3375357491","3304112824","3375352853","3304110122","3304119483","3304116075","3375354965","3304117474","3304111181","3375350787","3304112261","3304117010","3304114633","3375352266","3304114310","3375356441","3304117050","3375358090","3375355613","3304115124","3375357763","3304114336","3304110877","3304110942","3375351552","3304117623","3304114547","3304116530","3304111242","3304112428","3375351789","3304116826","3375356914","3375357279","3304116594","3375358621","3375350743","3304112336","3375354447","3304119347","3304115984","3375350144","3375357733","3304118266","3304115215","3375354440","3304112525","3375351333","3304117700","3375353192","3375353071","3375350302","3375356409","3375350784","3304112471","3304115428","3304118173","3375359425","3304113061","3304116858","3304117282","3375354293","3304115406","3304118527","3375357506","3375357867","3375352823","3304112637","3375355255","3304114797","3375358472","3375351566","3375358666","3304110234","3375356474","3304114083","3304117654","3304111441","3375359236","3304113586","3304119087","3375353530","3375359982","3304117985","3375352786","3375359212","3375350933","3304115446","3375354931","3304111100","3304115387","3304117933","3304118812","3304112667","3304110917","3375352060","3375358421","3304110889","3375354487","3304112282","3304119467","3304112223","3304114831","3304110021","3304112254","3304116457","3304117622","3304119890","3375355169","3375358630","3375354872","3375354467","3304113944","3375359158","3304114144","3304114213","3304114062","3375359872","3304118932","3375353184","3304111277","3304111758","3304114430","3304117643","3375359747","3375354399","3375356715","3375352021","3304116369","3304110052","3304114783","3304119046","3375353931","3375359623","3375350697","3375358755","3304113051","3304111599","3375356337","3375351652","3304116674","3304115762","3375358107","3304113530","3304119371","3375359588","3375358605","3304116701","3304115362","3375354316","3304111679","3375359817","3304111548","3304114371","3304119043","3375356418","3375353060","3304111546","3304115951","3375359926","3304116603","3375354736","3304118884","3304119161","3304114470","3304110685","3304116889","3304118213","3304119214","3375358126","3375352725","3375354113","3375359106","3375353081","3375353850","3375358911","3304115491","3304113293","3375353777","3304111045","3375358025","3375357773","3375352052","3304112825","3304118664","3375356739","3375355410","3304117590","3375359776","3375356767","3375353771","3304115507","3304114946","3304110317","3304111178","3375353688","3375350234","3304118814","3375354748","3304118235","3375357488","3375353248","3304118456","3375353186","3375356841","3304118953","3304110934","3304112469","3375351232","3304114102","3375358648","3304110855","3304117365","3304111718","3375359434","3375359440","3375357667","3375351604","3304119025","3304116874","3375351529","3375354776","3304117020","3304118165","3304110289","3304116709","3304112135","3375359032","3304114707","3304110079","3375350874","3304110966","3304115804","3375357343","3304114926","3304116021","3304116123","3304114285","3375355548","3375359868","3375356469","3304115345","3375356648","3375357041","3304113063","3375352189","3375353669","3375356706","3304114392","3304117180","3304118694","3375358796","3375350522","3304113185","3304117343","3304119284","3375357455","3375357754","3304118839","3304117864","3375351998","3304110548","3304113663","3304110536","3304112878","3304116290","3375358675","3375359169","3304112807","3375351681","3304113544","3304117617","3304112356","3304111220","3304115183","3375350811","3304113202","3375351795","3304110697","3375352063","3375356349","3375356700","3375356177","3375359644","3375355652","3304111306","3375353444","3304117149","3375351848","3375358251","3304115349","3375351357","3375352923","3304117367","3375354721","3375359788","3304118010","3304119625","3375359286","3375358807","3304111355","3304111465","3375357288","3375352810","3304114699","3304116609","3304118973","3375355343","3304112876","3304117264","3304111989","3304111246","3304116163","3304110429","3304117530","3304118588","3304118687","3375355711","3375359337","3304114837","3304118427","3304111489","3375356302","3304118140","3375359084","3375358742","3304115789","3304117608","3375357075","3304117247","3375355241","3375352600","3375359584","3304119359","3304110084","3375352791","3304112872","3375350430","3375355154","3375356696","3375358536","3304110251","3375357172","3375351068","3375358372","3304116266","3304119200","3375357393","3375358338","3304113306","3304118376","3375351643","3375353392","3375351408","3304110286","3304112801","3304110586","3304111760","3375355629","3304118770","3375353886","3375358176","3375351396","3304113667","3304116412","3304119655","3304119260","3304115284","3304118969","3375357769","3375353526","3375354792","3304119545","3304113402","3304115295","3304110031","3304118769","3304117340","3375352336","3304114073","3375355350","3375352846","3304116280","3304117707","3304113330","3375359028","3375353306","3304116755","3304112239","3304116963","3375355277","3375356875","3304116595","3304118046","3375353065","3375355294","3375353737","3375352157","3304117968","3375350231","3304112887","3304114880","3304119377","3304112399","3304118900","3304112970","3375354479","3304118989","3304110682","3304114422","3304119959","3304117747","3304110458","3304111284","3375357705","3375359453","3304116955","3375357768","3375357644","3304112675","3375359160","3375359431","3375359966","3375350594","3304117576","3304110083","3375356088","3304118018","3375353073","3304110155","3304113746","3375353864","3375356482","3304110757","3375355576","3375357231","3375359110","3375357159"]

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
                username = 'sphm1kztal'
                 = 'ohdKQ8aHJnig7v87it'
                endpoint = 'pk.smartproxy.com'
                port = '10010'

                proxies_extension = proxies(username, , endpoint, port)

                options.add_argument(
                    '--load-extension=D:\\autologinbot-master\\chromium_automation,D:\\autologinbot-master\\fingerprint,D:\\autologinbot-master\\surf')
                # options.add_argument(
                #    '--user-agent='+ag)

                #options.add_extension(proxies_extension)
                browser = webdriver.Chrome(options=options)
                browser.get(
                    "chrome-extension://aghniddgckgpmiiikjjfkgajlhpfladl/index.html")

                # usernap = WebDriverWait(browser, 120).until(
                #   EC.presence_of_element_located((By.XPATH,
                #                                   '/html/body/div/div/div[1]/div/div[1]/a[2]'))).click()
                # time.sleep(1)
                random_number = random.randint(1, 142)
                print(random_number)
                p = '#root > div > div.Zt5Rf.fade-enter-done > div:nth-child(1) > div > div.JzV3Q._1GKSy.m0fte > div > div > div:nth-child(3) > div:nth-child(' + str(
                    random_number) + ')'
                print(p)

                usernap = WebDriverWait(browser, 50).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    p))).click()
                time.sleep(3)
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

                            #browser.get('https://www.textanywhere.com/action/free-trial/')
                            time.sleep(2)
                            try:
                             usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#input44'))).send_keys(email)
                             usernap = WebDriverWait(browser, 25).until(
                                 EC.presence_of_element_located((By.XPATH,
                                                                 '/html/body/div/div[1]/main/div[2]/div/div/form/div[1]/div[3]/div[2]/div[2]/span/input[2]'))).send_keys('jamal@123J')
                            except:
                                print('a')
                                pass
                            time.sleep(2)


                            usernap = WebDriverWait(browser, 155).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#input64'))).send_keys('')
                            time.sleep(0.5)

                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#input71')))
                            text_to_type = 'zahid'

                            # Send the keys one by one with a delay to simulate human typing
                            for char in text_to_type:
                                usernap.send_keys(char)
                                time.sleep(0.1)
                            usernap = WebDriverWait(browser, 25).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                '#form35 > div.o-form-button-bar > input'))).click()
                            time.sleep(5)


                            usernap = WebDriverWait(browser, 60).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                '/html/body/div/div[1]/main/div[2]/div/div/form/div[2]/input')))
                            usernap.click()
                            time.sleep(0.5)
                            while (1):
                                try:
                                    usernap = WebDriverWait(browser, 25).until(
                                        EC.presence_of_element_located((By.XPATH,
                                                                        '/html/body/div/div[1]/main/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/span/div')))
                                    usernap.click()
                                except:
                                    usernap = WebDriverWait(browser, 60).until(
                                        EC.presence_of_element_located((By.XPATH,
                                                                        '/html/body/div/div[1]/main/div[2]/div/div/form/div[2]/input')))
                                    usernap.click()
                                    time.sleep(2)
                                    usernap = WebDriverWait(browser, 25).until(
                                        EC.presence_of_element_located((By.XPATH,
                                                                        '/html/body/div/div[1]/main/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/span/div')))
                                    usernap.click()

                                usernap = WebDriverWait(browser, 25).until(
                                    EC.presence_of_element_located((By.XPATH,
                                                                    '/html/body/div[2]/div/div/input')))
                                usernap.send_keys('pakistan')
                                usernap.send_keys(Keys.ENTER)
                                time.sleep(2)
                                # usernap = WebDriverWait(browser, 25).until(
                                #    EC.presence_of_element_located((By.XPATH,
                                #                                    '/html/body/div[1]/div[1]/main/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/span/select/option[162]'))).click()

                                usernap = WebDriverWait(browser, 25).until(
                                    EC.presence_of_element_located((By.XPATH,
                                                                    '/html/body/div/div[1]/main/div[2]/div/div/form/div[1]/div[2]/div[2]/div[2]/span/span[2]/input')))
                                text_to_type = fnumbers[recount]

                                # Send the keys one by one with a delay to simulate human typing
                                for char in text_to_type:
                                    usernap.send_keys(char)
                                    time.sleep(0.1)
                                usernap = WebDriverWait(browser, 25).until(
                                    EC.presence_of_element_located((By.XPATH,
                                                                    '/html/body/div/div[1]/main/div[2]/div/div/form/div[1]/div[2]/a[1]')))
                                usernap.click()
                                try:

                                    usernap = WebDriverWait(browser, 5).until(
                                        EC.presence_of_element_located((By.XPATH,
                                                                        '//div[@class="okta-form-infobox-error infobox infobox-error"]')))
                                    print(a)
                                except:
                                    pass

                                usernap = WebDriverWait(browser, 10).until(
                                    EC.presence_of_element_located((By.XPATH,
                                                                    '/html/body/div/div[1]/main/div[2]/div/div/form/div[1]/div[2]/div[4]/div[1]')))
                                time.sleep(90)

                                browser.refresh()
                                count += 1
                                print(count)
                                if (recount < (len(fnumbers) - 1)):
                                    recount = recount + 1
                                else:
                                    recount = 0
                                if (count!=0):
                                    if (count%10==0):
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
