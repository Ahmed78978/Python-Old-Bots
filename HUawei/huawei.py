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
#options.add_argument('--load-extension=C:\\Users\\Administrator\\Desktop\\Booking\\UltraSur')
options.add_extension('coordinates.crx')
options.add_argument("--disable-renderer-backgrounding")
options.add_argument("--disable-backgrounding-occluded-windows")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
mobile_emulation = {"deviceName": "iPhone SE"}
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"


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


        canvas = driver.find_element(By.CSS_SELECTOR,'#app-index > div > div > div.login-content > div.content-wrap-pc > div > div > div.jss11 > div.jss59 > div.jss63 > div.jss65 > div > div.jss125 > img.jss127')

        #canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)
        canvas_base64=canvas.get_attribute('src')

        canvas_png =urllib.request.urlretrieve(canvas_base64, "screen.png")
        #canvas_png = base64.b64decode(canvas_base64)

        #with open(r"shot.png", 'wb') as f:
         #   f.write(canvas_png)

        canvas1 = driver.find_element(By.CSS_SELECTOR,'#app-index > div > div > div.login-content > div.content-wrap-pc > div > div > div.jss11 > div.jss59 > div.jss63 > div.jss65 > div > div.jss125 > img.jss126.jss142')
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
        button = driver.find_element(By.XPATH, '//div[@class="jss132 jss142"]')
        ActionChains(driver).click_and_hold(button).perform()
        while(1):
         print(solution)


         ActionChains(driver).move_by_offset(xoffset=solution, yoffset=0).perform()
         time.sleep(4)

         solution+=1

         if(solution==(solution+20)):
            break
        ActionChains(driver).release().perform()



        print("done")

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
                    print("this is a solution: ",solution)

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

        print("error")
        print(a)


        pass
while(1):
    while(1):
     try:
      driver = webdriver.Chrome(options=options, desired_capabilities=capa)

      time.sleep(10)
      while(1):
       try:
         driver.get('https://passport.webull.com/auth/simple/signup?source=seo-google-home&hl=en&redirect_uri=https%3A%2F%2Fwww.webull.com%2F')
         break
       except:
         driver.quit()
         break

     except:
        pass
     break
    while (1):
        try:
            time.sleep(5)

            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//div[@class="jss27"]')))
            phonee.click()
            time.sleep(1)
            phonee = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Pakistan(+92)')]")))
            phonee.click()
            time.sleep(1)
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Phone Number"]')))
            phonee.send_keys(fnumbers[recount])
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//div[@class="jss74"]')))
            phonee.click()



            time.sleep(15)
            print("ab check kr rha hun")



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

                #pass

            time.sleep(10)
            driver.refresh()
            if(count%10==0):
                count=count+1
                driver.quit()
            else:
              count = count + 1
            if (recount < (len(fnumbers) - 1)):
                recount = recount + 1
            else:
                recount = 0
            print(count)

        except Exception as e:
            try:
              print(a)


              driver.quit()
            except Exception  as e:

                print(a)

                pass
            break
