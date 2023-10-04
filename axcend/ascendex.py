from selenium import webdriver
import time

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import base64
from solver1 import PuzleSolver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
#options.add_argument('--load-extension=C:\\Users\\Administrator\\Desktop\\Booking\\UltraSur')
options.add_argument('--load-extension=D:\\autologinbot-master\\UltraSur')
options.add_argument("--window-size=500,800")
options.add_argument("--disable-renderer-backgrounding")
options.add_argument("--disable-backgrounding-occluded-windows")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
mobile_emulation = {"deviceName": "iPhone SE"}
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"


fnumbers=["3324974902","3358079281","3367956840","3368634399","3368988235","3369522534","3370335881","3370745103","3324974923","3358366138","3367947513","3368634390","3368988202","3369521468","3370335878","3370743891","3324974951","3358718461","3367936495","3368628137","3368988201","3369515080","3370335872","3370741263","3324975036","3359085530","3367935506","3368621483","3368988185","3369512768","3370335870","3370738516","3324975069","3362044735","3367934492","3368619838","3368988168","3369508629","3370335864","3370736987","3324975071","3362504974","3367931638"]
recount=0
count=0
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
while(1):
    while (1):
        try:
            driver = webdriver.Chrome(options=options)
            break
        except:
            pass
    while (1):
        try:
            driver.get('https://ascendex.com/en/register')
            break
        except:
            pass

    while (1):
        try:

            time.sleep(5)

            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//h4[@class="tab semibold mg-s-left-32 small"]')))
            phonee.click()

            #driver.execute_script("""
             #  var attr = document.querySelector('div[class^=" css-1f36k5w"]');
            #   attr.remove();
            #""")

            phonssee = driver.find_element(By.CLASS_NAME,("el-input__prefix"))
            phonssee.click()

            time.sleep(50)
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'#main > section > div > div.wrap > div.body > div.form.text > div > form > div.el-form-item.mg-top-36.mg-s-top-20.is-required > div > div > div > span > div > div.dropdown > div.dropdown-search > div > input[type=text]')))
            phonee.send_keys("pakistan")
            time.sleep(1)
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//li[@data-code="PK"]')))
            phonee.click()
            time.sleep(2)
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//input[@placeholder="Phone Number"]')))
            phonee.send_keys(fnumbers[recount])
            time.sleep(1)

            phonees = driver.find_element(By.XPATH,
                                                '//input[@placeholder=""]')
            phonees.send_keys("")
            time.sleep(2)

            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CLASS_NAME,
                                                'box')))
            phonee.click()
            time.sleep(1)
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//div[@class="butt primary"]')))
            phonee.click()


            time.sleep(5)
            check=1


            while(1):
                try:

                    if(check%5==0):
                        break
                    time.sleep(2)
                    capcha(driver)

                    phonee = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH,
                                                        '//input[@placeholder="Enter phone verification code"]')))
                    break
                except:
                    try:
                     check=check+1
                     print("ni  hua captcha")
                     phonee = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        'body > div:nth-child(111) > div.geetest_panel_box.geetest_panelshowslide > div.geetest_panel_next > div > div.geetest_panel > div > a.geetest_refresh_1')))
                     phonee.click()
                     print("refreshing")
                    except:
                        pass
            if (check % 5 == 0):
                driver.quit()
                break

            time.sleep(5)
            try:
                driver.get('https://ascendex.com/en/register')

            except:
                break
            count = count + 1
            if (recount < (len(fnumbers) - 1)):
                recount = recount + 1
            else:
                recount = 0
            print(count)
        except Exception as e:
            try:


              driver.close()
            except Exception  as e:


                pass
            break



