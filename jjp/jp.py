from selenium import webdriver
import time
import urllib.request
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import base64
from solver import PuzleSolver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--load-extension=C:\\Users\\Administrator\\Desktop\\Booking\\UltraSur')
options.add_argument("--disable-renderer-backgrounding")
options.add_argument("--disable-backgrounding-occluded-windows")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
mobile_emulation = {"deviceName": "iPhone SE"}
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"


fnumbers=["3007982112"]
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


        canvas = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/img[1]')

        #canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)
        canvas_base64=canvas.get_attribute('src')

        canvas_png =urllib.request.urlretrieve(canvas_base64, "screen.png")
        #canvas_png = base64.b64decode(canvas_base64)

        #with open(r"shot.png", 'wb') as f:
         #   f.write(canvas_png)

        canvas1 = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/img[2]')
        #canvas_base641 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas1)

        canvas_base641 = canvas1.get_attribute('src')
        #canvas_png1 = base64.b64decode(canvas_base641)
        canvas_png1 = urllib.request.urlretrieve(canvas_base641, "shot.png")

        #with open(r"screen.png", 'wb') as f:
         #   f.write(canvas_png1)
        y="shot.png"

        o="screen.png"




        solver = PuzleSolver(y, o)
        solution = solver.get_position()

        button = driver.find_element(By.ID,'slider_btn')
        ActionChains(driver).click_and_hold(button).perform()
        ActionChains(driver).move_by_offset(xoffset=solution, yoffset=0).perform()
        time.sleep(0.41)
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
        print(a)

        print("error")


        pass
while(1):
    while(1):
     try:
      driver = webdriver.Chrome(options=options, desired_capabilities=capa)

      time.sleep(10)
      while(1):
       try:
         driver.get('https://jp-ex.io/en/register')
         break
       except:
         driver.quit()
         break

     except:
        pass
     break
    while (1):
        try:




            phonee = WebDriverWait(driver, 40).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#root > div > section > main > div > div.ant-row.login-container > div > div:nth-child(3) > div > div.ant-card-head > div.ant-tabs.ant-tabs-top.ant-tabs-large.ant-card-head-tabs > div.ant-tabs-nav > div.ant-tabs-nav-wrap > div > div:nth-child(2)')))
            phonee.click()

            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#horizontal_login_username > div.ant-col.selection > button')))
            phonee.click()
            time.sleep(2)

            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                'body > div:nth-child(6) > div > div > div > div.ant-popover-inner > div.ant-popover-title > div > div > span > span > input')))
            phonee.send_keys("pakistan")

            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                'body > div:nth-child(6) > div > div > div > div.ant-popover-inner > div.ant-popover-inner-content > div > div > div > ul > li > div > div:nth-child(1)')))
            phonee.click()
            time.sleep(1)
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#horizontal_login_username > div.ant-col.selection > button')))
            phonee.click()
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#horizontal_login_username > div:nth-child(2) > input')))
            phonee.send_keys(fnumbers[recount])

            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#horizontal_login_')))
            phonee.send_keys("")

            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#horizontal_login_repeat')))
            phonee.send_keys("")
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#horizontal_login_agreement')))
            phonee.click()
            time.sleep(1)
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#horizontal_login > div:nth-child(5) > div > div > div > div > button')))
            phonee.click()
            time.sleep(1)
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                'body > div:nth-child(7) > div > div.ant-modal-wrap > div > div.ant-modal-content > div > div > div:nth-child(2) > button')))
            phonee.click()
            tr=1

            while(1):
              try:
                if(tr%100==0):
                    driver.quit()
                    break
                phonee = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#verification > div:nth-child(3) > div > div > div > button')))
                break
              except:

                tr=tr+1
                print("retrying")
                capcha(driver)
                pass
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#verification > div:nth-child(2) > div > div > div > div > span > span')))
            phonee.click()

            time.sleep(10)
            driver.refresh()
            if(count%10==0):
                count=count+1

            else:
              count = count + 1
            if (recount < (len(fnumbers) - 1)):
                recount = recount + 1
            else:
                recount = 0
            print(count)

        except Exception as e:
            print(a)
            try:


              driver.quit()
            except Exception  as e:


                pass
            break
