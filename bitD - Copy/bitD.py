from selenium import webdriver
import time

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import base64
from solver1 import PuzleSolver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
#options.add_argument('--load-extension=D:\\autologinbot-master\\UltraSur')

options.add_argument("--disable-renderer-backgrounding")
options.add_argument("--disable-backgrounding-occluded-windows")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
mobile_emulation = {"deviceName": "iPhone SE"}
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"


fnumbers=["3369572855","3370338065","3370771132","3324974328","3314418195","3368059184","3368669489","3368988439","3369571599","3370337850","3370770693"]
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
                EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.geetest_holder.geetest_mobile.geetest_ant.geetest_popup > div.geetest_popup_box > div.geetest_popup_wrap > div.geetest_wrap > div.geetest_widget > div > a > div.geetest_canvas_img.geetest_absolute > div > canvas.geetest_canvas_slice.geetest_absolute')))
        canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)

        canvas_png = base64.b64decode(canvas_base64)

        with open(r"shot.png", 'wb') as f:
            f.write(canvas_png)

        canvas1 = driver.find_element(By.CSS_SELECTOR,'body > div.geetest_holder.geetest_mobile.geetest_ant.geetest_popup > div.geetest_popup_box > div.geetest_popup_wrap > div.geetest_wrap > div.geetest_widget > div > a > div.geetest_canvas_img.geetest_absolute > div > canvas.geetest_canvas_bg.geetest_absolute')
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
while(1):
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.bitdcehk.com/en_US/register')

    while (1):
        try:
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#app > div.page-content.page-content-chain > div > div.page-register-content > div > div.common-select.select-value.select-filterable > div.input_line_content.a-2-bd > input')))
            phonee.click()



            phonee = WebDriverWait(driver, 40).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#app > div.page-content.page-content-chain > div > div.page-register-content > div > div.common-select.select-visible.select-filterable > div.input_line_content.a-2-bd > input')))
            phonee.send_keys(Keys.CONTROL,"a")
            phonee.send_keys('pakistan')

            #driver.execute_script("""
             #  var attr = document.querySelector('div[class^=" css-1f36k5w"]');
            #   attr.remove();
            #""")

            phonssee = driver.find_element(By.CSS_SELECTOR,("#app > div.page-content.page-content-chain > div > div.page-register-content > div > div.common-select.select-visible.select-value.select-filterable > div.select-options-box.a-5-bg.b-1-cl > div.select-option-list > div > div > div > ul > li"))
            phonssee.click()

            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'#app > div.page-content.page-content-chain > div > div.page-register-content > div > section:nth-child(3) > div.input-line-baseStance.a-2-bd > div > input')))
            phonee.send_keys(fnumbers[recount])

            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#app > div.page-content.page-content-chain > div > div.page-register-content > div > section:nth-child(4) > div.input-line-baseStance.a-2-bd > div > input')))
            phonee.send_keys('')

            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#app > div.page-content.page-content-chain > div > div.page-register-content > div > section:nth-child(5) > div.input-line-baseStance.a-2-bd > div > input')))
            phonee.send_keys('')




            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#app > div.page-content.page-content-chain > div > div.page-register-content > div > div.resgister-opions > section')))
            phonee.click()

            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#app > div.page-content.page-content-chain > div > div.page-register-content > div > button')))
            phonee.click()
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#captchaBox > div > div.geetest_btn > div.geetest_radar_btn > div.geetest_radar_tip')))
            phonee.click()


            time.sleep(5)
            check=1


            while(1):
                try:

                    if(check%5==0):
                        break
                    time.sleep(2)
                    capcha(driver)

                    phonee = WebDriverWait(driver, 7).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        '#app > div.page-content.page-content-chain > div > section.common-dialog > div.dialog-frame.a-5-bg > div.dialog-frame-body > section > div.input-line-baseStance.a-2-bd > div > input')))
                    break
                except:


                     check=check+1
                     pass


            if (check % 5 == 0):
                driver.quit()
                break

            time.sleep(2)
            driver.get('https://www.bitdcehk.com/en_US/register')
            count = count + 1
            #if (count % 10 == 0):
            #    driver.quit()
             #   break
            if (recount < (len(fnumbers) - 1)):
                recount = recount + 1
            else:
                recount = 0
            print(count)
        except Exception as e:

            try:


              driver.quit()
            except Exception  as e:


                pass
            break



