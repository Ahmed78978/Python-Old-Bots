import undetected_chromedriver.v2 as uc
import time
import freetempmail as ft
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import base64
from solver1 import PuzleSolver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import  re
mobile_emulation = {"deviceName": "iPhone SE"}
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
#url = 'https://www.larksuite.com/en/accounts/page/global_register?redirect_uri=https://www.larksuite.com/download&registration_process=global_register&app_id=1'
url='https://xmf9yr2lvg.larksuite.com/messenger/setting/'
fnumbers=["3324974902","3358079281","3367956840","3368634399","3368988235","3369522534","3370335881","3370745103","3324974923","3358366138","3367947513","3368634390","3368988202","3369521468","3370335878","3370743891","3324974951","3358718461","3367936495","3368628137","3368988201","3369515080","3370335872","3370741263","3324975036","3359085530","3367935506","3368621483","3368988185","3369512768","3370335870","3370738516","3324975069","3362044735","3367934492","3368619838","3368988168","3369508629","3370335864","3370736987","3324975071","3362504974","3367931638"]
recount=0
count=1
def wait_for_selector(drivers, selector, by=By.XPATH, timeout=30, EC_condtion=None):
    wait = WebDriverWait(drivers, timeout=timeout)
    el = wait.until(lambda d: d.find_element(by, selector))
    if EC_condtion:
        el = wait.until(EC_condtion(by, selector))
    return el


def capcha(driver):
    try:


        canvas = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_panelshowslide > div.geetest_panel_next > div > div.geetest_wrap > div.geetest_widget > div > a > div.geetest_canvas_img.geetest_absolute > div > canvas.geetest_canvas_slice.geetest_absolute')))

        canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)

        canvas_png = base64.b64decode(canvas_base64)

        with open(r"shot.png", 'wb') as f:
            f.write(canvas_png)

        canvas1 = driver.find_element(By.CSS_SELECTOR,'body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_panelshowslide > div.geetest_panel_next > div > div.geetest_wrap > div.geetest_widget > div > a > div.geetest_canvas_img.geetest_absolute > div > canvas.geetest_canvas_bg.geetest_absolute')

        canvas_base641 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas1)

        canvas_png1 = base64.b64decode(canvas_base641)

        with open(r"screen.png", 'wb') as f:
            f.write(canvas_png1)
        y="shot.png"

        o="screen.png"



        solver = PuzleSolver(y, o)
        solution = solver.get_position()

        button = driver.find_element(By.CLASS_NAME,'geetest_slider_button')
        ActionChains(driver).click_and_hold(button).perform()
        ActionChains(driver).move_by_offset(xoffset=solution, yoffset=0).perform()
        time.sleep(1.41)
        ActionChains(driver).release().perform()

        try:
            while True:
                try:
                    time.sleep(8)
                    driver.execute_script("document.querySelector('.geetest_refresh_1').click()")
                    time.sleep(8)

                    canvas = driver.find_element(By.XPATH,"33//canvas[2]")

                    canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);",
                                                          canvas)

                    canvas_png = base64.b64decode(canvas_base64)

                    with open(r"imgcap/screenshot1.png", 'wb') as f:
                        f.write(canvas_png)

                    canvas1 = driver.find_element(By.XPATH,"33//canvas[1]")

                    canvas_base641 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);",
                                                           canvas1)

                    canvas_png1 = base64.b64decode(canvas_base641)

                    with open(r"imgcap/screenshot2.png", 'wb') as f:
                        f.write(canvas_png1)

                    solver = PuzleSolver("imgcap/screenshot1.png", "imgcap/screenshot2.png")
                    solution = solver.get_position()

                    button = driver.find_element_by(By.CLASS_NAME,'geetest_slider_button')
                    ActionChains(driver).click_and_hold(button).perform()
                    ActionChains(driver).move_by_offset(xoffset=solution, yoffset=0).perform()
                    time.sleep(1.43)
                    ActionChains(driver).release().perform()
                except:
                    break
        except:
            pass
    except:
        print("yaha n")

        pass
import os
import shutil
import tempfile
def force_patcher_to_use(directory):
    # copy the chromedriver in directory
    exe = uc.Patcher.exe_name
    src = os.path.join(uc.Patcher.data_path, exe)
    executable_path = os.path.join(directory, exe)
    shutil.copyfile(src, executable_path)

    # monkey patch the Patcher class
    class PatcherWithForcedExecutablePath(uc.Patcher):
        def __init__(self, *args, **kwargs):
            kwargs["executable_path"] = executable_path
            super().__init__(*args, **kwargs)

    uc.Patcher = PatcherWithForcedExecutablePath

    return executable_path
if __name__ == "__main__":
    while (1):
        while(1):
           try:
              limit = False

              ft.generateMail()
              options = uc.ChromeOptions()
              options.add_argument('--load-extension=D:\\autologinbot-master\\UltraSur')

              options.add_argument("--disable-renderer-backgrounding")
              options.add_argument("--disable-backgrounding-occluded-windows")
              tmp_directory = os.path.normpath(tempfile.mkdtemp())
              executable_path = force_patcher_to_use(tmp_directory)
              driver = uc.Chrome(options=options,executable_path=executable_path)
              driver.get(url)
              email = ft.getEmail()
              break
           except:


               pass
        while (1):
            try:
                if(limit==True):
                    driver.quit()
                    break

                time.sleep(8)
                while (1):
                    try:
                        phonee = WebDriverWait(driver, 50).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR,
                                                            '#root > div > div.web-login-left > div.web-main-content > div.login-content-container > div.new-account-login-box.passport-process-container.new-account-login-box-hide-back > div > div > div > div.pp-base-tabs.base-tabs-container.login-with-account-tabs > div.base-tabs > div:nth-child(1) > div > div > div > input')))
                        phonee.send_keys(email)
                        break
                    except:
                        pass

                time.sleep(2)

                usernap = WebDriverWait(driver, 60).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#root > div > div.web-login-left > div.web-main-content > div.login-content-container > div.new-account-login-box.passport-process-container.new-account-login-box-hide-back > div > div > div > div.terms-and-policy-container > label > span.ud__checkbox > input')))

                ac = ActionChains(driver)
                ac.move_to_element(usernap).click().perform()


                usernap = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#root > div > div.web-login-left > div.web-main-content > div.login-content-container > div.new-account-login-box.passport-process-container.new-account-login-box-hide-back > div > div > div > button')))
                ac = ActionChains(driver)
                ac.move_to_element(usernap).click().perform()
                time.sleep(30)
                messages = ft.getMessages()  # get messages
                print(messages)
                otp1=re.findall("'\d{6}", str(messages))
                print(otp1)
                otp=re.findall("\d",str(otp1))
                x=" ".join(otp)
                y=x.replace(" ", "")
                print(y)
                coutn=1


                usernap = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#root > div > div.web-login-left > div.web-main-content > div.login-content-container > div > div > div:nth-child(2) > div > div.pp-base-tabs.base-tabs-container.verify-identity-tabs > div > div > div.pp-base-code-box.base-code-box-container > div.base-code-box > div:nth-child(1) > input')))
                usernap.send_keys(otp[0])
                while (1):

                 actions = ActionChains(driver)
                 actions.send_keys(otp[coutn])
                 actions.perform()
                 coutn+=1
                 time.sleep(1)
                 if(coutn==6):
                     break
                time.sleep(2)

                usernap = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#root > div > div.web-login-left > div.web-main-content > div.login-content-container > div > div > div:nth-child(3) > div > div:nth-child(6) > div > button')))
                ac = ActionChains(driver)
                ac.move_to_element(usernap).click().perform()
                time.sleep(2)


                usernap = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    '//div[@class="pp-choose-register-item"]')))
                ac = ActionChains(driver)
                ac.move_to_element(usernap).click().perform()


                usernap = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#root > div > div.web-login-left > div.web-main-content > div.login-content-container > div > div > div:nth-child(4) > div > div._pp-ud-input-wrapper > div > div > input')))
                usernap.send_keys('')
                time.sleep(1)
                usernap = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#root > div > div.web-login-left > div.web-main-content > div.login-content-container > div > div > div:nth-child(4) > div > button')))
                ac = ActionChains(driver)
                ac.move_to_element(usernap).click().perform()
                usernap = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#root > div > div.web-login-left > div.web-main-content > div.login-content-container > div > div > div:nth-child(5) > div > div:nth-child(3) > div._pp-ud-input-wrapper > div > div > input')))
                usernap.send_keys('')
                usernap = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#root > div > div.web-login-left > div.web-main-content > div.login-content-container > div > div > div:nth-child(5) > div > div._pp-ud-input-wrapper > div > div > input')))
                usernap.send_keys('')
                time.sleep(2)
                usernap = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#root > div > div.web-login-left > div.web-main-content > div.login-content-container > div > div > div:nth-child(5) > div > button')))
                ac = ActionChains(driver)
                ac.move_to_element(usernap).click().perform()

                usernap = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    '//div[@class="appNavbar_avatarContainer-inside"]')))
                ac = ActionChains(driver)
                ac.move_to_element(usernap).click().perform()

                time.sleep(2)
                try:
                  usernap = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#root-ternantCardModal > div > div.tenantUserCard_links > div:nth-child(2)')))
                  ac = ActionChains(driver)
                  ac.move_to_element(usernap).click().perform()
                except:
                    usernap = WebDriverWait(driver, 120).until(
                        EC.presence_of_element_located((By.XPATH,
                                                        '//img[@alt="Avatar"]')))
                    usernap.click()
                    time.sleep(2)
                    usernap = WebDriverWait(driver, 120).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        '#root-ternantCardModal > div > div.tenantUserCard_links > div:nth-child(2)')))
                    usernap.click()
                    time.sleep(2)

                while (1):
                 if(limit==True):

                        break

                 while(1):
                  try:

                    time.sleep(5)
                    usernap = WebDriverWait(driver, 60).until(
                       EC.presence_of_element_located((By.XPATH,
                                                        '//input[@placeholder="Enter phone number or email address"]')))
                    actions = ActionChains(driver)
                    actions.send_keys(fnumbers[recount])
                    actions.perform()


                    time.sleep(2)

                    try:

                      usernap = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        '#__larkc-modall-container__ > div:nth-child(3) > div > div.larkc-modall-content > div > div.UnitedInvite_container > div > div > div.ExternalContact_frame.search > div > div.ExternalContactsSearch_list > div.ExternalContactsSearch_empty')))
                      ac = ActionChains(driver)
                      ac.move_to_element(usernap).click().perform()

                    except:
                        print("dobara  number  likh rha ")
                        actions = ActionChains(driver)
                        actions.send_keys(fnumbers[recount])
                        actions.perform()
                        usernap = WebDriverWait(driver, 20).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR,
                                                            '#__larkc-modall-container__ > div:nth-child(3) > div > div.larkc-modall-content > div > div.UnitedInvite_container > div > div > div.ExternalContact_frame.search > div > div.ExternalContactsSearch_list > div.ExternalContactsSearch_empty')))
                        usernap.click()


                    usernap = WebDriverWait(driver, 60).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        '#__larkc-modall-container__ > div:nth-child(3) > div > div.larkc-modall-content > div > div.UnitedInvite_container > div > div > div.ExternalContact_frame.search > div > div.ExternalContactsSearch_list > div > button')))
                    ac = ActionChains(driver)
                    ac.move_to_element(usernap).click().perform()
                    time.sleep(2)
                    usernap = WebDriverWait(driver, 65).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        '#__larkc-modall-container__ > div.larkc-modalx-wrapper.larkc-modalx-wrapper-mask > div > div > main > div.SendInviteSms_inputGroup > div')))
                    ac = ActionChains(driver)
                    ac.move_to_element(usernap).click().perform()
                    time.sleep(2)
                    usernap = WebDriverWait(driver, 60).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        '#__overlay-container__ > div.larkc-portal > div > div > div:nth-child(57)')))
                    usernap.click()
                    time.sleep(2)
                    usernap = WebDriverWait(driver, 60).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        '#__larkc-modall-container__ > div.larkc-modalx-wrapper.larkc-modalx-wrapper-mask > div > div > footer > div > button.larkc-btn.larkc-btn-normal.larkc-btn-primary.larkc-btn-large')))
                    usernap.click()
                    ac = ActionChains(driver)
                    ac.move_to_element(usernap).click().perform()



                    count = count + 1
                    x = (len(fnumbers)) - 1
                    if (recount < (x)):
                        recount = recount + 1
                    else:
                        recount = 0
                    if(count%100==0):
                        print(a)
                    print(count)
                  except:

                      print(a)






            except:


               driver.quit()
               break


