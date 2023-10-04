#import undetected_chromedriver.v2 as webdriver
from selenium import webdriver
from selenium.webdriver.opera.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import string
import random
import time
count=0
recount=0
letters = string.ascii_lowercase
usernameStr = 'zahidkamal78978@gmail.com'
Str = '3007982112'
options = Options()
options.add_argument("--disable-renderer-backgrounding")
options.add_argument("--disable-backgrounding-occluded-windows")

options.binary_location = r'D:\\autologinbot-master\\careem\\operadriver.exe'

options.add_argument('--load-extension=D:\\autologinbot-master\\LOBBY\\Nope,D:\\autologinbot-master\\Urbanvpn')
browser = webdriver.Opera(options=options, executable_path=r' location_of_operadriver.exe')
"""
while(1):
 try:
    i = random.randint(2, 57)
    time.sleep(5)
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
 except:
    pass
"""
while(1):
    try:
        browser.get(
            ('https://www.zee5.com'))
        fnumbers = ["1401791930","1958900463","1958896724","1958847481","1958799012","1958922952","1958979684","1958718957","1958828716","1958977225","1958742315","1958987885","1958945736","1958886672","1958901402","1958972053","1958784747","1958831139","1958707476","1958887583","1958872074","1958854643","1958768352","1958877940","1958974444","1958773709","1958743268","1958974578","1958739698","1958988357","1958997591","1958753373","1958925278","1958838239","1958737810","1958932529","1958964913","1958924031","1958767957","1958747742","1958732848","1958912386","1958808655","1958820329","1958877519","1958805370","1958790481","1958758492","1958847649","1958788816","1958740300","1958845698","1958855746","1958769903","1958802227","1958864169","1958823218","1958868688","1958787266","1958919986","1958997249","1958864847","1958730706","1958958363","1958856350","1958838735","1958953015","1958776117","1958727821","1958771783","1958881151","1958755316","1958879244","1958740284","1958814522","1958712387","1958870245","1958944063","1958903184","1958857102","1958971734","1958707957","1958706012","1958966988","1958859697","1958987294","1958718860","1958900632","1958835023","1958884066","1958996747","1958815097","1958912419","1958949780","1958820000","1958752453","1958869754","1958926538","1958786238","1958793378","1958842809","1958747116","1958840644","1958768987","1958917485","1958711160","1958997546","1958835003","1958804393","1958779234","1958715031","1958985010","1958879147","1958970607","1958989394","1958708101","1958735049","1958906138","1958957829","1958914389","1958817221","1958804553","1958902204","1958937623","1958952108","1958766342","1958891279","1958904175","1958993161","1958745259","1958795783","1958826667","1958976934","1958968844","1958937564","1958968322","1958907822","1958923483","1958816963","1958901538","1958832598","1958802660","1958787239","1958905478","1958776151","1958953306","1958739331","1958994168","1958760498","1958760954","1958793749","1958819876","1958822193","1958807060","1958876225","1958735819","1958742426","1958977878","1958820437","1958710971","1958992475","1958827090","1958720274","1958995788","1958988579","1958833097","1958718120","1958947029","1958921460","1958927922","1958901880","1958792550","1958840481","1958775902","1958954057","1958750872","1958732890","1958944332","1958973819","1958799119","1958801399","1958998621","1958987948","1958907972","1958717803","1958860979","1958881780","1958727421","1958833926","1958801129","1958706580","1958857761","1958985067","1958768775","1958815094","1958777724","1958738943","1958962910","1958981885","1958839105","1958948320","1401791927","1958876370","1958859310","1958724220","1958922517","1958831086","1958758385","1958862354","1958816898","1958924645","1958710009","1958899941","1958710108","1958788933","1958905703","1958782844","1958895889","1958706941","1958994727","1958906472","1958782606"]
        # fill in username and hit the next button
        userna = WebDriverWait(browser, 120).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='selected-dial-code']")))
        userna.click()
        # username = browser.find_element_by_class_name('hwid-input userAccount')
        usernap = WebDriverWait(browser, 120).until(
            EC.presence_of_element_located((By.XPATH, "//li[@data-dial-code='880']")))
        usernap.click()

        phone = WebDriverWait(browser, 120).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='tel']")))
        phone.send_keys(fnumbers[recount])

        phonee = WebDriverWait(browser, 120).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='verify-recover-btn']")))
        phonee.click()

        try:
            phonee = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.XPATH,
                                                ("//*[contains(text(), 'Something went wrong. Please try again later.')]"))))
            print('sent')
            browser.delete_all_cookies()

            break
        except:
            pass
        if (recount < (len(fnumbers) - 1)):

            recount += 1
        else:

            recount = 0
        count = count + 1
        print(count)
        browser.delete_all_cookies()
    except:
        try:
            i = random.randint(2, 57)
            time.sleep(5)
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
        except:
            pass
        pass


