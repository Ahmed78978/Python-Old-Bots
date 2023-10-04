from selenium  import  webdriver
from TempMail import TempMail #imports everything from TempMail library

import  re
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


user=['i.nfokamalhmed@gmail.com', 'in.fokamalhmed@gmail.com', 'inf.okamalhmed@gmail.com', 'info.kamalhmed@gmail.com', 'infok.amalhmed@gmail.com', 'infoka.malhmed@gmail.com', 'infokam.alhmed@gmail.com', 'infokama.lhmed@gmail.com', 'infokamal.hmed@gmail.com', 'infokamalh.med@gmail.com', 'infokamalhm.ed@gmail.com', 'infokamalhme.d@gmail.com', 'a.hmedinfozahid@gmail.com', 'ah.medinfozahid@gmail.com', 'ahm.edinfozahid@gmail.com', 'ahme.dinfozahid@gmail.com', '.infozahid@gmail.com', 'i.nfozahid@gmail.com', 'in.fozahid@gmail.com', 'inf.ozahid@gmail.com', 'info.zahid@gmail.com', 'infoz.ahid@gmail.com', 'infoza.hid@gmail.com', 'infozah.id@gmail.com', 'infozahi.d@gmail.com', 'i.nfotelcotestahymed@gmail.com', 'in.fotelcotestahymed@gmail.com', 'inf.otelcotestahymed@gmail.com', 'info.telcotestahymed@gmail.com', 'infot.elcotestahymed@gmail.com', 'infote.lcotestahymed@gmail.com', 'infotel.cotestahymed@gmail.com', 'infotelc.otestahymed@gmail.com', 'infotelco.testahymed@gmail.com', 'infotelcot.estahymed@gmail.com', 'infotelcote.stahymed@gmail.com', 'infotelcotes.tahymed@gmail.com', 'infotelcotest.ahymed@gmail.com', 'infotelcotesta.hymed@gmail.com', 'infotelcotestah.ymed@gmail.com', 'infotelcotestahy.med@gmail.com', 'infotelcotestahym.ed@gmail.com', 'infotelcotestahyme.d@gmail.com', 'i.nfokaiengeering@gmail.com', 'in.fokaiengeering@gmail.com', 'inf.okaiengeering@gmail.com', 'info.kaiengeering@gmail.com', 'infok.aiengeering@gmail.com', 'infoka.iengeering@gmail.com', 'infokai.engeering@gmail.com', 'infokaie.ngeering@gmail.com', 'infokaien.geering@gmail.com', 'infokaieng.eering@gmail.com', 'infokaienge.ering@gmail.com', 'infokaiengee.ring@gmail.com', 'infokaiengeer.ing@gmail.com', 'infokaiengeeri.ng@gmail.com', 'infokaiengeerin.g@gmail.com', 'infokaiengeering.@gmail.com', 'infokaiengeeringa.hmed@gmail.com', 'infokaiengeeringah.med@gmail.com', 'infokaiengeeringahm.ed@gmail.com', 'infokaiengeeringahme.d@gmail.com', 'i.nforipha@gmail.com', 'in.foripha@gmail.com', 'inf.oripha@gmail.com', 'info.ripha@gmail.com', 'infor.ipha@gmail.com', 'infori.pha@gmail.com', 'inforip.ha@gmail.com', 'inforiph.a@gmail.com', 'inforipha.@gmail.com', 'inforiphaa.hmed@gmail.com', 'inforiphaah.med@gmail.com', 'inforiphaahm.ed@gmail.com', 'inforiphaahme.d@gmail.com']
gmail_pass=['exbbdrfxhdedqngi', 'exbbdrfxhdedqngi', 'exbbdrfxhdedqngi', 'exbbdrfxhdedqngi', 'exbbdrfxhdedqngi', 'exbbdrfxhdedqngi', 'exbbdrfxhdedqngi', 'exbbdrfxhdedqngi', 'exbbdrfxhdedqngi', 'exbbdrfxhdedqngi', 'exbbdrfxhdedqngi', 'exbbdrfxhdedqngi', 'txplsxbiunzycygq', 'txplsxbiunzycygq', 'txplsxbiunzycygq', 'txplsxbiunzycygq', 'txplsxbiunzycygq', 'txplsxbiunzycygq', 'txplsxbiunzycygq', 'txplsxbiunzycygq', 'txplsxbiunzycygq', 'txplsxbiunzycygq', 'txplsxbiunzycygq', 'txplsxbiunzycygq', 'txplsxbiunzycygq', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'pimhjjgolgnjenid', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'twanvmlygmgchnyx', 'hbyswscrqygdwnoc', 'hbyswscrqygdwnoc', 'hbyswscrqygdwnoc', 'hbyswscrqygdwnoc', 'hbyswscrqygdwnoc', 'hbyswscrqygdwnoc', 'hbyswscrqygdwnoc', 'hbyswscrqygdwnoc', 'hbyswscrqygdwnoc', 'hbyswscrqygdwnoc', 'hbyswscrqygdwnoc', 'hbyswscrqygdwnoc', 'hbyswscrqygdwnoc']

host = "imap.gmail.com"
# Creating a storage.JSON file with authentication details
def delete_cache(driver):

    driver.switch_to.window(driver.window_handles[-1])  # Switch window to the second tab
    driver.get('chrome://settings/clearBrowserData')  # Open your chrome settings.
    perform_actions(driver, Keys.TAB * 2 + Keys.DOWN * 4 + Keys.TAB * 7 + Keys.ENTER)  # Tab to the time select and key down to say "All Time" then go to the Confirm button and press Enter


def perform_actions(driver, keys):
    actions = ActionChains(driver)
    actions.send_keys(keys)
    time.sleep(5)
    print('Performing Actions!')
    actions.perform()
def get_total_emails(mai):
    # Create server and login
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(user[mai], gmail_pass[mai])

    # Using SELECT to choose the INBOX folder
    mail.select("INBOX")

    # Get the total number of emails in the INBOX folder
    _, response = mail.search(None, "ALL")
    return len(response[0].split())
def read_email_from_gmail(count=1, contain_body=True,mai=0):

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
        res, msg = mail.fetch(str(i), "(RFC822)")
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
                print("-"*50)  # To divide the messages
                print("From    : ", sender)
                print("Subject : ", subject)
                if(contain_body):
                    print("Body    : ", body)
                    return body


import time
import random
import string


def generate_unique_username(base_name="user"):
    # Using the current timestamp (to the microsecond) to ensure uniqueness
    timestamp = str(int(time.time() * 1000000))

    # Generate a random string of 5 characters for added uniqueness
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))

    return f"{base_name}_{random_str}_{timestamp}"
def convertTuple(tup):
    strc = ''
    c=len(tup)
    
    for item in range(5):
        strc=strc+strc.join(tup[item])
        
    return strc
letters = string.ascii_lowercase
usernameStr=['zahidkamal78978@gmail.com','zahid60@gmail.com','78978@gmail.com']

Str = ''


from selenium.webdriver.chrome import service



mobile_emulation = {"deviceName": "iPhone SE"}
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
count=0
recount=0
total=0
t=0
t=0
if __name__ == "__main__":
 while(1):

  numb="0123456789"
  if (total >= 10):

      break
  
  url='https://www.hilton.com/en/hilton-honors/join/?ocode=ASPEW'
  fnumbers=["3309767426","3309767427","3309767428","3309767429","3309767430","3309767433","3309767434","3309767435","3309767436","3309767438","3309767439","3309767440","3309767441","3309767442","3309767443","3309767444","3309767445","3309767447","3309767448","3309767450","3309767451","3309767452","3309767453","3309767454","3309767455","3309767456","3309767457","3309767458","3309767459","3309767460","3309767461","3309767462","3309767463","3309767464","3309767465","3309767466","3309767467","3309767470","3309767471","3309767472","3309767475","3309767477","3309767478","3309767479","3309767480","3309767483","3309767484","3309767485","3309767486","3309767487","3309767488","3309767489","3309767490","3309767491","3309767492","3309767493","3309767495","3309767496","3309767498","3309767499","3309767500","3309767501","3309767504","3309767505","3309767506","3309767508","3309767509","3309767511","3309767512","3309767514","3309767516","3309767517","3309767518","3309767519","3309767520","3309767522","3309767523","3309767524","3309767525","3309767526","3309767528","3309767529","3309767530","3309767532","3309767533","3309767534","3309767536","3309767537","3309767540","3309767541","3309767544","3309767545","3309767546","3309767547","3309767548","3309767549","3309767550","3309767551","3309767552","3309767553","3309767555","3309767556","3309767557","3309767561","3309767562","3309767563","3309767564","3309767565","3309767566","3309767567","3309767568","3309767570","3309767572","3309767573","3309767574","3309767575","3309767576","3309767577","3309767579","3309767580","3309767581","3309767582","3309767584","3309767585","3309767586","3309767587","3309767588","3309767589","3309767590","3309767591","3309767593","3309767594","3309767595","3309767596","3309767597","3309767598","3309767599","3309767601","3309767602","3309767603","3309767604","3309767606","3309767607","3309767611","3309767612","3309767615","3309767617","3309767618","3309767619","3309767621","3309767622","3309767623","3309767624","3309767626","3309767627","3309767628","3309767629","3309767630","3309767631","3309767632","3309767633","3309767634","3309767635","3309767637","3309767638","3309767641","3309767642","3309767643","3309767646","3309767647","3309767648","3309767649","3309767650","3309767651","3309767652","3309767653","3309767654","3309767655","3309767657","3309767658","3309767659","3309767660","3309767661","3309767662","3309767663","3309767664","3309767665","3309767666","3309767667","3309767669","3309767670","3309767671","3309767672","3309767673","3309767674","3309767675","3309767676","3309767677","3309767678","3309767679","3309767680","3309767681","3309767682","3309767684","3309767685","3309767686","3309767687","3309767688","3309767690","3309767691","3309767692","3309767693","3309767694","3309767695","3309767696","3309767697","3309767698","3309767699","3309767700","3309767701","3309767703","3309767705","3309767706","3309767707","3309767709","3309767710","3309767711","3309767712","3309767713","3309767715","3309767716","3309767717","3309767718","3309767720","3309767721","3309767722","3309767724","3309767725","3309767726","3309767727","3309767728","3309767729","3309767730","3309767732","3309767733","3309767734","3309767735","3309767737","3309767738","3309767740","3309767741","3309767742","3309767743","3309767746","3309767747","3309767748","3309767749","3309767751","3309767752","3309767753","3309767754","3309767755","3309767757","3309767759","3309767760","3309767761","3309767762","3309767763","3309767764","3309767767","3309767768","3309767769","3309767770","3309767771","3309767774","3309767775","3309767776","3309767778","3309767779","3309767780","3309767781","3309767782","3309767783","3309767786","3309767787","3309767788","3309767789","3309767790","3309767791","3309767792","3309767793","3309767796","3309767799","3309767801","3309767802","3309767803","3309767804","3309767805","3309767806","3309767807","3309767808","3309767809","3309767810","3309767811","3309767812","3309767813","3309767815","3309767816","3309767818","3309767819","3309767820","3309767821","3309767824","3309767825","3309767826","3309767827","3309767830","3309767832","3309767833","3309767834","3309767835","3309767836","3309767837","3309767838","3309767839","3309767840","3309767842","3309767843","3309767844","3309767845","3309767846","3309767847","3309767848","3309767849","3309767850","3309767851","3309767852","3309767853","3309767854","3309767856","3309767857","3309767858","3309767859","3309767860","3309767861","3309767862","3309767863","3309767865","3309767866","3309767867","3309767869","3309767870","3309767872","3309767873","3309767874","3309767875","3309767876","3309767877","3309767878","3309767879","3309767880","3309767881","3309767882","3309767884","3309767885","3309767886","3309767889","3309767890","3309767891","3309767892","3309767893","3309767894","3309767895","3309767896","3309767897","3309767898","3309767899","3309767902","3309767903","3309767904","3309767905","3309767906","3309767907","3309767908","3309767909","3309767910","3309767911","3309767912","3309767913","3309767914","3309767915","3309767916","3309767917","3309767918","3309767919","3309767920","3309767921","3309767922","3309767924","3309767925","3309767926","3309767927","3309767928","3309767930","3309767931","3309767932","3309767933","3309767934","3309767935","3309767936","3309767937","3309767938","3309767939","3309767940","3309767941","3309767942","3309767943","3309767944","3309767946","3309767948","3309767949","3309767950","3309767952","3309767953","3309767954","3309767955","3309767956","3309767957","3309767958","3309767959","3309767960","3309767961","3309767962","3309767963","3309767966","3309767967","3309767968","3309767969","3309767970","3309767971","3309767973","3309767975","3309767977","3309767979","3309767981","3309767982","3309767983","3309767984","3309767985","3309767986","3309767988","3309767989","3309767990","3309767991","3309767992","3309767993","3309767994","3309767995","3309767996","3309767997","3309767998","3309768000","3309768001","3309768002","3309768003","3309768004","3309768005","3309768006","3309768008","3309768011","3309768012","3309768014","3309768015","3309768016","3309768017","3309768019","3309768020","3309768021","3309768022","3309768023","3309768024","3309768025","3309768026","3309768028","3309768029","3309768030","3309768031","3309768032","3309768033","3309768034","3309768035","3309768036","3309768037","3309768039","3309768041","3309768042","3309768045","3309768046","3309768048","3309768049","3309768051","3309768052","3309768053","3309768054","3309768055","3309768056","3309768057","3309768058","3309768059","3309768060","3309768061","3309768062","3309768063","3309768064","3309768065","3309768067","3309768068","3309768069","3309768070","3309768072","3309768073","3309768074","3309768076","3309768077","3309768079","3309768080","3309768082","3309768083","3309768084","3309768086","3309768088","3309768089","3309768090","3309768091","3309768092","3309768093","3309768094","3309768095","3309768096","3309768097","3309768098","3309768099","3309768100","3309768101","3309768102","3309768104","3309768106","3309768107","3309768108","3309768109","3309768110","3309768111","3309768112","3309768113","3309768115","3309768116","3309768117","3309768118","3309768119","3309768120","3309768121","3309768122","3309768123","3309768124","3309768125","3309768126","3309768128","3309768130","3309768131","3309768132","3309768133","3309768134","3309768135","3309768136","3309768137","3309768138","3309768139","3309768140","3309768141","3309768142","3309768143","3309768144","3309768145","3309768146","3309768148","3309768149","3309768150","3309768151","3309768153","3309768154","3309768155","3309768156","3309768158","3309768159","3309768160","3309768161","3309768163","3309768164","3309768166","3309768167","3309768169","3309768171","3309768172","3309768173","3309768174","3309768175","3309768176","3309768178","3309768179","3309768180","3309768181","3309768182","3309768183","3309768184","3309768185","3309768186","3309768187","3309768189","3309768190","3309768191","3309768192","3309768193","3309768194","3309768196","3309768197","3309768198","3309768199","3309768200","3309768201","3309768202","3309768204","3309768205","3309768206","3309768207","3309768208","3309768209","3309768211","3309768212","3309768213","3309768214","3309768215","3309768218","3309768219","3309768220","3309768221","3309768223","3309768224","3309768225","3309768226","3309768229","3309768232","3309768233","3309768235","3309768237","3309768238","3309768239","3309768240","3309768241","3309768242","3309768243","3309768244","3309768245","3309768246","3309768248","3309768249","3309768250","3309768251","3309768252","3309768253","3309768254","3309768255","3309768256","3309768257","3309768258","3309768259","3309768260","3309768261","3309768262","3309768263","3309768264","3309768265","3309768266","3309768267","3309768268","3309768269","3309768270","3309768273","3309768274","3309768275","3309768276","3309768277","3309768280","3309768281","3309768282","3309768284","3309768285","3309768286","3309768287","3309768288","3309768289","3309768290","3309768291","3309768292","3309768293","3309768294","3309768295","3309768297","3309768298","3309768300","3309768301","3309768303","3309768304","3309768305","3309768306","3309768307","3309768308","3309768309","3309768310","3309768311","3309768313","3309768314","3309768315","3309768317","3309768318","3309768319","3309768320","3309768321","3309768322","3309768324","3309768326","3309768327","3309768328","3309768329","3309768330","3309768331","3309768332","3309768333","3309768335","3309768336","3309768337","3309768338","3309768340","3309768342","3309768343","3309768347","3309768348","3309768349","3309768350","3309768352","3309768353","3309768355","3309768356","3309768357","3309768358","3309768359","3309768361","3309768362","3309768364","3309768365","3309768366","3309768367","3309768368","3309768370","3309768373","3309768375","3309768376","3309768377","3309768378","3309768379","3309768380","3309768383","3309768384","3309768385","3309768389","3309768390","3309768391","3309768392","3309768393","3309768394","3309768395","3309768396","3309768397","3309768398","3309768399","3309768402","3309768405","3309768406","3309768409","3309768410","3309768411","3309768412","3309768413","3309768414","3309768415","3309768416","3309768417","3309768418","3309768420","3309768422","3309768424","3309768425","3309768426","3309768427","3309768428","3309768429","3309768431","3309768432","3309768433","3309768434","3309768436","3309768437","3309768438","3309768439","3309768440","3309768441","3309768442","3309768443","3309768444","3309768445","3309768447","3309768448","3309768449","3309768450","3309768452","3309768454","3309768456","3309768457","3309768458","3309768459","3309768460","3309768461","3309768462","3309768463","3309768464","3309768465","3309768467","3309768469","3309768470","3309768471","3309768473","3309768474","3309768475","3309768476","3309768477","3309768478","3309768479","3309768480","3309768481","3309768483","3309768485","3309768486","3309768487","3309768488","3309768489","3309768490","3309768491","3309768492","3309768493","3309768495","3309768496","3309768497","3309768498","3309768499","3309768500","3309768502","3309768503","3309768504","3309768505","3309768506","3309768508","3309768511","3309768512","3309768513","3309768514","3309768515","3309768516","3309768517","3309768518","3309768520","3309768521","3309768523","3309768524","3309768526","3309768527","3309768528","3309768529","3309768530","3309768532","3309768535","3309768536","3309768537","3309768539","3309768541","3309768542","3309768543","3309768544","3309768547","3309768548","3309768550","3309768552","3309768553","3309768554","3309768555","3309768556","3309768557","3309768558","3309768560","3309768562","3309768563","3309768564","3309768566","3309768567","3309768568","3309768569","3309768570","3309768571","3309768572","3309768573","3309768574","3309768575","3309768576","3309768577","3309768578","3309768579","3309768580","3309768581","3309768582","3309768583","3309768584","3309768585","3309768586","3309768587","3309768589","3309768591","3309768592","3309768594","3309768595","3309768597","3309768598","3309768599","3309768601","3309768602","3309768603","3309768604","3309768605","3309768606","3309768607","3309768608","3309768610","3309768611","3309768612","3309768613","3309768614","3309768615","3309768616","3309768617","3309768618","3309768620","3309768621","3309768622","3309768623","3309768624","3309768625","3309768628","3309768629","3309768630","3309768631","3309768632","3309768633","3309768634","3309768636","3309768637","3309768638","3309768639","3309768641","3309768642","3309768643","3309768644","3309768645","3309768646","3309768647","3309768648","3309768649","3309768650","3309768651","3309768653","3309768656","3309768657","3309768658","3309768659","3309768660","3309768661","3309768662","3309768663","3309768665","3309768666","3309768667","3309768668","3309768669","3309768671","3309768672","3309768673","3309768674","3309768675","3309768678","3309768679","3309768680","3309768682","3309768683","3309768684","3309768685","3309768686","3309768687","3309768688","3309768689","3309768690","3309768691","3309768692","3309768693","3309768694","3309768695","3309768696","3309768697","3309768698","3309768699","3309768700","3309768702","3309768703","3309768704","3309768705","3309768706","3309768708","3309768709","3309768710","3309768711","3309768712","3309768713","3309768714","3309768715","3309768716","3309768717","3309768718","3309768720","3309768722","3309768723","3309768724","3309768726","3309768727","3309768728","3309768729","3309768730","3309768731","3309768732","3309768733","3309768735","3309768736","3309768737","3309768738","3309768739","3309768740","3309768741","3309768742","3309768743","3309768745","3309768746","3309768747","3309768748","3309768750","3309768751","3309768752","3309768753","3309768754","3309768755","3309768757","3309768758","3309768759","3309768760","3309768761","3309768762","3309768763","3309768764","3309768765","3309768767","3309768768","3309768769","3309768770","3309768771","3309768773","3309768774","3309768777","3309768778","3309768780","3309768782","3309768783","3309768784","3309768785","3309768786","3309768787","3309768788","3309768789","3309768791","3309768792","3309768793","3309768794","3309768796","3309768799","3309768800","3309768801","3309768802","3309768803","3309768804","3309768805","3309768806","3309768807","3309768808","3309768809","3309768811","3309768812","3309768813","3309768814","3309768815","3309768816","3309768817","3309768818","3309768819","3309768821","3309768822","3309768824","3309768825","3309768826","3309768827","3309768828","3309768829","3309768830","3309768831","3309768832","3309768833","3309768834","3309768835","3309768837","3309768838","3309768839","3309768840","3309768841","3309768843","3309768844","3309768846","3309768847","3309768848","3309768849","3309768850","3309768852","3309768853","3309768855","3309768856","3309768858","3309768859","3309768860","3309768862","3309768863","3309768864","3309768865","3309768866","3309768867","3309768869","3309768870","3309768872","3309768873","3309768874","3309768875","3309768876","3309768877","3309768878","3309768879","3309768880","3309768881","3309768882","3309768883","3309768884","3309768885","3309768886","3309768888","3309768889","3309768890","3309768892","3309768894","3309768895","3309768896","3309768900","3309768901","3309768903","3309768904","3309768905","3309768906","3309768907","3309768908","3309768909","3309768911","3309768912","3309768913","3309768915","3309768916","3309768917","3309768918","3309768919","3309768920","3309768922","3309768923","3309768924","3309768925","3309768926","3309768927","3309768928","3309768929","3309768934","3309768935","3309768936","3309768937","3309768938","3309768939","3309768940","3309768941","3309768942","3309768943","3309768944","3309768945","3309768946","3309768947","3309768949","3309768950","3309768951","3309768953","3309768955","3309768956","3309768957","3309768958","3309768960","3309768961","3309768962","3309768963","3309768964","3309768965","3309768966","3309768967","3309768968","3309768969","3309768970","3309768971","3309768972","3309768974","3309768975","3309768976","3309768977","3309768978","3309768979","3309768980","3309768981","3309768982","3309768983","3309768984","3309768985","3309768986","3309768988","3309768989","3309768990","3309768991","3309768992","3309768993","3309768994","3309768995","3309768996","3309768997","3309768999","3309769000","3309769001","3309769002","3309769003","3309769004","3309769005","3309769006","3309769007","3309769009","3309769010","3309769011","3309769012","3309769013","3309769014","3309769018","3309769019","3309769021","3309769022","3309769024","3309769026","3309769027","3309769028","3309769030","3309769031","3309769032","3309769033","3309769034","3309769036","3309769037","3309769038","3309769039","3309769043","3309769044","3309769045","3309769047","3309769048","3309769049","3309769050","3309769051","3309769052","3309769053","3309769054","3309769055","3309769056","3309769057","3309769058","3309769060","3309769061","3309769062","3309769063","3309769064","3309769065","3309769066","3309769067","3309769069","3309769070","3309769072","3309769074","3309769076","3309769077","3309769079","3309769082","3309769083","3309769084","3309769088","3309769089","3309769092","3309769093","3309769094","3309769096","3309769097","3309769098","3309769099","3309769100","3309769101","3309769102","3309769103","3309769105","3309769106","3309769110","3309769111","3309769113","3309769114","3309769115","3309769118","3309769119","3309769120","3309769121","3309769122","3309769123","3309769124","3309769125","3309769126","3309769127","3309769130","3309769131","3309769132","3309769133","3309769134","3309769135","3309769137","3309769138","3309769139","3309769140","3309769141","3309769142","3309769144","3309769145","3309769147","3309769148","3309769149","3309769150","3309769151","3309769152","3309769153","3309769154","3309769155","3309769156","3309769158","3309769162","3309769163","3309769164","3309769165","3309769166","3309769168","3309769169","3309769170","3309769171","3309769172","3309769173","3309769174","3309769176","3309769179","3309769181","3309769182","3309769183","3309769185","3309769186","3309769187","3309769188","3309769189","3309769192","3309769193","3309769194","3309769195","3309769196","3309769197","3309769198","3309769200","3309769201","3309769202","3309769203","3309769204","3309769205","3309769206","3309769207","3309769208","3309769209","3309769210","3309769211","3309769215","3309769216","3309769217","3309769218","3309769219","3309769220","3309769221","3309769222","3309769223","3309769224","3309769227","3309769229","3309769230","3309769231","3309769232","3309769233","3309769234","3309769236","3309769238","3309769240","3309769241","3309769242","3309769243","3309769245","3309769246","3309769247","3309769248"]

  #random.shuffle(fnumbers)
  mailcount=0

  numbers=[]
  mai=random.randint(0, len(user)-1)




  while(1):
      if (total >= 10):

          break
      try:
          options = webdriver.ChromeOptions()
          # options.add_argument(r'--profile-directory=C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3')

          options.binary_location = r'C:\Users\Ahmad\AppData\Local\Programs\Opera\opera.exe'
          #profile_directory = 'C:\\Users\\Ahmad\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 4'
          #options.add_argument(f'user-data-dir={profile_directory}')
          #options.add_argument('--load-extension=D:\\autologinbot-master\\surf')

          webdriver_service = service.Service('D:\\autologinbot-master\\operadriver.exe')
          webdriver_service.start()

          browser = webdriver.Remote(webdriver_service.service_url,webdriver.DesiredCapabilities.OPERA,options=options)


           #= webdriver.Chrome(options=options)
          i = random.randint(2, 57)
          inb='infozahid@gmail.com'
          time.sleep(3)
          browser.get('https://www.google.com/search?q=dg&rlz=1C1CHBF_enPK1034PK1034&oq=dg&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTINCAEQABiDARixAxiABDINCAIQABiDARixAxiKBTINCAMQLhiDARixAxiABDIHCAQQABiABDINCAUQABiDARixAxiABDITCAYQLhiDARivARjHARixAxiABDINCAcQABiDARixAxiKBTIKCAgQABixAxiABDINCAkQABiDARixAxiABNIBBzYyM2owajSoAgCwAgA&sourceid=chrome&ie=UTF-8')





          time.sleep(1)

          time.sleep(3)




          while (1):

              try:



                  print('h')


                  browser.get(url)
                  inbox = TempMail.generateInbox()
                  print("Email Address: " + inbox.address)




                  phonee = WebDriverWait(browser, 20).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR, '#main > main > div > div > div > form > div:nth-child(2) > label > input')))

                  text_to_type = ""

                  for char in text_to_type:
                      phonee.send_keys(char)
                      time.sleep(0.1)

                  time.sleep(2)
                  phonee = WebDriverWait(browser, 10).until(
                          EC.presence_of_element_located(
                              (By.CSS_SELECTOR,
                               '#main > main > div > div > div > form > div:nth-child(3) > label > input')))


                  text_to_type = "ZAhid"

                  # Send the keys one by one with a delay to simulate human typing
                  for char in text_to_type:
                      phonee.send_keys(char)
                      time.sleep(0.1)



                  t = get_total_emails(mai)
                  time.sleep(2)

                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#main > main > div > div > div > form > div:nth-child(4) > label > span.flex.flex-row > select')))

                  usernap.click()
                  time.sleep(1)
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#main > main > div > div > div > form > div:nth-child(4) > label > span.flex.flex-row > select > option:nth-child(161)')))
                  usernap.click()
                  time.sleep(1)
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#main > main > div > div > div > form > div:nth-child(4) > label > span.flex.flex-row > input')))
                  usernap.send_keys(fnumbers[recount])
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#main > main > div > div > div > form > div:nth-child(5) > label > input')))
                  usernap.send_keys(inbox.address)
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#main > main > div > div > div > form > div:nth-child(6) > label > select')))
                  usernap.click()

                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#main > main > div > div > div > form > div:nth-child(6) > label > select > option:nth-child(161)')))
                  usernap.click()

                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#main > main > div > div > div > form > div:nth-child(9) > label > input'))).click()
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.NAME,
                                                      'address.addressLine1')))
                  time.sleep(2)

                  text_to_type = "House#993 Street#40 F17/2 islamabad"

                  # Send the keys one by one with a delay to simulate human typing
                  for char in text_to_type:
                      usernap.send_keys(char)
                      time.sleep(0.1)
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#main > main > div > div > div > form > div.\!mb-10 > label > input'))).click()
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#main > main > div > div > div > form > div:nth-child(9) > label > input')))

                  text_to_type = "Islamabad"

                  # Send the keys one by one with a delay to simulate human typing
                  for char in text_to_type:
                      usernap.send_keys(char)
                      time.sleep(0.1)
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#main > main > div > div > div > form > div:nth-child(12) > label > input')))

                  text_to_type = "jamal@123J"

                  # Send the keys one by one with a delay to simulate human typing
                  for char in text_to_type:
                      usernap.send_keys(char)
                      time.sleep(0.1)
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#main > main > div > div > div > form > div.\!mb-10 > label > input')))
                  text_to_type = "jamal@123J"

                  # Send the keys one by one with a delay to simulate human typing
                  for char in text_to_type:
                      usernap.send_keys(char)
                      time.sleep(0.1)
                  time.sleep(5)
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#main > main > div > div > div > form > div.space-y-10 > button')))
                  usernap.click()
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#main > main > div > section.w-full.bg-transparent.shadow-md > div > div > div > p.font-sans.font-bold.lg\:text-xl')))
                  text = usernap.text

                  # Use regular expression to find the number
                  match = re.search(r'(\d+)', text)
                  number=''
                  if match:
                      number = match.group(1)
                      print(number)  # This should print 1896624440
                  browser.get('https://www.hilton.com/en/hilton-honors/login/?forwardPageURI=%252Fen%252Fhilton-honors%252Fguest%252Fprofile%252Fpersonal-information%252F#enhancedSecurity')
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#main > main > div > div > div.flex.flex-col.space-y-12.md\:flex-row.md\:space-y-0.md\:divide-x.md\:divide-border > div.w-full.md\:w-1\/2.md\:pr-16 > div > iframe')))
                  browser.switch_to.frame(usernap)
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.XPATH,
                                                      '/html/body/div[1]/div/form/label[1]/input')))
                  usernap.send_keys(number)
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#')))
                  text_to_type = "jamal@123J"

                  # Send the keys one by one with a delay to simulate human typing
                  for char in text_to_type:
                      usernap.send_keys(char)
                      time.sleep(0.1)

                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.CSS_SELECTOR,
                                                      '#__next > div > form > button')))
                  usernap.click()

                  while(1):
                      time.sleep(2)
                      usernap = WebDriverWait(browser, 120).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          '#enhancedSecurity > section > section.sc-dRFtgE.iOichl > button')))
                      usernap.click()
                      usernap = WebDriverWait(browser, 120).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          '#react-aria-modal-dialog > div > div.sc-hXRMBi.jXycXq > div > section > div > button')))
                      usernap.click()
                      time.sleep(2)
                      browser.refresh()
                      usernap = WebDriverWait(browser, 120).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          '#main > main > div:nth-child(2) > div > div > section.block.w-full.lg\:flex > div:nth-child(1) > section:nth-child(3) > section.sc-hUfwpO.kBVbrl > section > button')))
                      usernap.click()
                      try:
                       usernap = WebDriverWait(browser, 10).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          '#react-aria-modal-dialog > div > div.sc-hXRMBi.jXycXq > div > section > form > section > section > section:nth-child(2) > section > button')))
                       usernap.click()


                       usernap = WebDriverWait(browser, 10).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          '#phones\[0\]\.phoneCountryDropDown')))
                       usernap.click()
                      except:
                          browser.refresh()
                          usernap = WebDriverWait(browser, 120).until(
                              EC.presence_of_element_located((By.CSS_SELECTOR,
                                                              '#main > main > div:nth-child(2) > div > div > section.block.w-full.lg\:flex > div:nth-child(1) > section:nth-child(3) > section.sc-hUfwpO.kBVbrl > section > button')))
                          usernap.click()
                          usernap = WebDriverWait(browser, 120).until(
                              EC.presence_of_element_located((By.CSS_SELECTOR,
                                                              '#react-aria-modal-dialog > div > div.sc-hXRMBi.jXycXq > div > section > form > section > section > section:nth-child(2) > section > button')))
                          usernap.click()
                          usernap = WebDriverWait(browser, 120).until(
                              EC.presence_of_element_located((By.CSS_SELECTOR,
                                                              '#phones\[0\]\.phoneCountryDropDown')))
                          usernap.click()

                      usernap = WebDriverWait(browser, 120).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          '#phones\[0\]\.phoneCountryDropDown > option:nth-child(172)')))
                      usernap.click()
                      usernap = WebDriverWait(browser, 120).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          '#phones\[0\]\.phoneNumberTextInput')))
                      usernap.send_keys(fnumbers[recount])
                      usernap = WebDriverWait(browser, 120).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          '#react-aria-modal-dialog > div > div.sc-epnACN.jmSmzO > button.sc-kpOJdX.sc-ckVGcZ.sc-hZSUBg.hbAiCC')))
                      usernap.click()
                      count+=1
                      print(count)


                      if (recount < (len(fnumbers) - 1)):
                          recount = recount + 1
                      else:
                          recount = 0
                          break














              except  Exception as e:







                  if (recount < (len(fnumbers) - 1)):
                      recount = recount + 1
                  else:
                      recount = 0

      except:






          browser.quit()
          print('biggest exception')



   


     
      


     
     
     
     
  
