import undetected_chromedriver.v2 as uc
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
def check():
    try:
        browser.find_element(By.XPATH,'//input[@aria-label="Enter phone number"]')
    except NoSuchElementException:
        return False
    return True
def convertTuple(tup):
        # initialize an empty string
    strc = ''
    c=len(tup)
    
    for item in range(5):
        strc=strc+strc.join(tup[item])
        
    return strc
letters = string.ascii_lowercase
usernameStr='z78978@gmail.com'

Str = ''


options =uc.ChromeOptions()
#options.add_extension('extension_1_6_6_0.crx')

options.add_argument("--disable-renderer-backgrounding")
options.add_argument("--disable-backgrounding-occluded-windows")

capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
#options.add_experimental_option("mobileEmulation", mobile_emulation)
count=0
recount=0
if __name__ == "__main__":
    while (1):
        while (1):
            numb = "0123456789"

            url = 'https://duo.google.com/?web&utm_source=marketing_page_button_main'

            fnumbers = ["3316129650","3316132612","3316132830","3316150037","3316150048","3316151353","3316154997","3316169159","3316169165","3316169189","3316169249","3316169303","3316169328","3316169404","3316169418","3316169448","3316169479","3316169557","3316169561","3316169613","3324973836","3363607515","3368062152","3368697810","3369059584","3369602389","3370338240","3371430335","3324973905","3363627213","3368062141","3368694964","3369057742","3369602378","3370338232","3371430321","3324973919","3363647519","3368061801","3368688946","3369047977","3369602369","3370338207","3371428732","3324973950","3363766964","3368061797","3368688335","3369047964","3369594106","3370338204","3371427143","3324973964","3364082473","3368061765","3368679642","3369047481","3369593873","3370338192","3371416314","3324973993","3367463765"]

            mailcount = 0

            numbers = []



            while (1):
                browser = uc.Chrome(options=options)



                # get first child window
                time.sleep(10)
                chwd = browser.window_handles

                if (len(chwd) >= 2):
                    browser.switch_to.window(chwd[1])

                    browser.quit()
                    browser.switch_to.window(chwd[0])

                browser.get((url))
                try:
                    time.sleep(5)
                    usernap = WebDriverWait(browser, 120).until(
                        EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Email or phone"]')))
                    usernap.send_keys('nimraimtiaz549@gmail.com')
                except Exception as e:
                    print(".")
                try:
                    time.sleep(2)
                    phonee = WebDriverWait(browser, 120).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        '#identifierNext > div > button')))

                    phonee.click()
                    time.sleep(3)
                    usernap = WebDriverWait(browser, 120).until(
                        EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Enter your "]')))

                    usernap.send_keys("")
                    time.sleep(5)
                    usernap = WebDriverWait(browser, 120).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        '#Next > div > button')))
                    usernap.click()
                    time.sleep(40)




                except  Exception as e:
                    print("exception ayatha")

                    browser.quit()
                    break


                while (1):
                   try:
                    time.sleep(10)
                    usernap = WebDriverWait(browser, 120).until(
                        EC.presence_of_element_located((By.XPATH,
                                                        '//button[@jsname="e6YUYd"]')))
                    usernap.click()
                    time.sleep(5)
                    while(1):
                        c=check()
                        if(c):
                            break
                        else:
                            usernap = WebDriverWait(browser, 120).until(
                                EC.presence_of_element_located((By.XPATH,
                                                                '//button[@jsname="e6YUYd"]')))
                            usernap.click()
                            print("RETRYING")
                            time.sleep(5)



                    try:
                     phone = WebDriverWait(browser, 20).until(
                            EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Select a country"]')))
                     phone.click()
                     phone = WebDriverWait(browser, 20).until(
                         EC.presence_of_element_located((By.CSS_SELECTOR, '#yDmH0d > div.llhEMd.iWO5td > div > div.g3VIld.WgecKb.Up8vH.Whe8ub.hFEqNb.J9Nfi.iWO5td > span > div > div.oFxDlc > div > div.G6byKc > div.cnn54 > div.qqYQWe.hBBXhd > div.r5iSrd.vjc9od.Axoxm > div > div.OA0qNb.ncFHed > div:nth-child(161)')))
                     phone.click()

                     phone = WebDriverWait(browser, 20).until(
                        EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Enter phone number"]')))
                     phone.send_keys(Keys.CONTROL + 'a')
                     phone.send_keys(fnumbers[recount])
                    except Exception as e:
                        print("check kr oo")


                        time.sleep(10)
                        usernap = WebDriverWait(browser, 120).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR,
                                                            '#YwS4Af > div.s0yXtf > div.p7DEQb > div.ZRQFOd.TaGDFc > c-wiz > div > span > div.AdBNRd > div.JGH17e > div:nth-child(2) > button'))).click()

                        phone = WebDriverWait(browser, 20).until(
                            EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Enter phone number"]')))
                        phone.send_keys(Keys.CONTROL + 'a')
                        phone.send_keys(fnumbers[recount])

                    time.sleep(2)

                    phonesp = WebDriverWait(browser, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR,
                                                            '#yDmH0d > div.llhEMd.iWO5td > div > div.g3VIld.WgecKb.Up8vH.Whe8ub.hFEqNb.J9Nfi.iWO5td > span > div > div > div > div.G6byKc > div.cnn54 > div.U26fgb.O0WRkf.zZhnYe.e3Duub.C0oVfc.ztQe4c.mO2Dyb.ehsQMd.M9Bg4d')))
                    phonesp.click()


                   except Exception as e:
                        print("..")

                        browser.quit()
                        break

                   count = count + 1
                   if (recount < (len(fnumbers) - 1)):
                        recount = recount + 1
                   else:
                    recount = 0
                   print(count)
                   time.sleep(5)
                   browser.refresh()

     
     
     
     
  
