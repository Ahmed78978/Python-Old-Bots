from selenium import webdriver as uc
import time

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import base64
from solver1 import PuzleSolver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

def get_track( distance):
        track = []
        current = 0
        mid = distance * 4 / 5
        t = 0.2
        v = 0

        while current < distance:
            if current < mid:
                a = 2
            else:
                a = -3
            v0 = v
            v = v0 + a * t
            move = v0 * t + 1 / 2 * a * t * t
            current += move
            track.append(round(move))
        return track
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

        button = driver.find_element(By.CLASS_NAME, 'geetest_slider_button')
        ActionChains(driver).click_and_hold(button).perform()
        ActionChains(driver).drag_and_drop_by_offset(button, solution, 0).perform()
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

        return(0)

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
              options = uc.ChromeOptions()
              options.add_argument('--load-extension=C:\\Users\\Administrator\\Desktop\\Booking\\UltraSur')
              options.add_experimental_option("mobileEmulation", mobile_emulation)
              #options.add_argument("--window-size=400,500")


              options.add_argument("--disable-renderer-backgrounding")
              options.add_argument("--disable-backgrounding-occluded-windows")

              driver = uc.Chrome(options=options)

              break
           except:
               print(a)



               pass
        while(1):

         while (1):
            try:
                while (1):
                    try:
                        driver.get('https://accounts.xt.com/en-US/register?backurl=https%3A%2F%2Fwww.xt.com%2F')
                        break
                    except:
                        pass

                time.sleep(5)

                phonee = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#__next > div > div > div.index_main__iXFtb > div > div.iWin > div > div.iForm > div.iBtn > button')))
                phonee.click()

                # driver.execute_script("""
                #  var attr = document.querySelector('div[class^=" css-1f36k5w"]');
                #   attr.remove();
                # """)



                time.sleep(2)
                phonee = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#__next > div > div > div.index_main__iXFtb > div.index_main__pLO2n.dark > div.iWin > div > div.iForm > div.iNav > button:nth-child(2)')))
                phonee.click()
                time.sleep(1)
                phonee = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#__next > div > div > div.index_main__iXFtb > div.index_main__pLO2n.dark > div.iWin > div > div.iForm > div:nth-child(2) > div.iBody > div > div.index_main__2QHrK.dark')))
                phonee.click()
                time.sleep(2)

                phonee = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    '//input[@placeholder="Search"]')))
                phonee.send_keys("p")
                phonee.send_keys("a")

                phonee.send_keys("ki")
                phonee.send_keys("st")
                time.sleep(0.5)
                phonee = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    "//li[@class='ant-list-item']")))

                phonee.click()
                time.sleep(1)
                phonee = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    '//input[@type="tel"]')))
                phonee.send_keys(fnumbers[recount])
                time.sleep(1)





                phonee = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#__next > div > div > div.index_main__iXFtb > div.index_main__pLO2n.dark > div.iWin > div > div.iForm > div:nth-child(3) > div.iBody > div > input')))
                phonee.send_keys('')
                phonee = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#__next > div > div > div.index_main__iXFtb > div.index_main__pLO2n.dark > div.iWin > div > div.iForm > button')))
                phonee.click()


                check = 1

                error = False

                while (1):
                    try:

                        if (check % 5 == 0):
                            break
                        time.sleep(2)
                        check = check + 1
                        a=capcha(driver)
                        if(a==0):
                            try:
                                button = driver.find_element_by(By.CLASS_NAME, 'geetest_slider_button')
                            except:
                                break



                        try:
                            button = driver.find_element_by(By.CLASS_NAME, 'geetest_slider_button')
                            try:

                                print("ni  hua captcha")
                                phonee = WebDriverWait(driver, 10).until(
                                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                    'body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_panelshowslide > div.geetest_panel_next > div > div.geetest_panel > div > a.geetest_refresh_1')))
                                phonee.click()
                                print("refreshing")
                            except:
                                pass
                        except:
                            break



                    except:
                        pass

                if (error == True):
                    driver.delete_all_cookies()

                    count += 1
                    driver.get('chrome-extension://addncelkdjfgpipbhnnmfmjeglhbppgl/control.html')
                    phonee = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        "body > div > div > div > div > div > div.col-xs-4 > enable-switch > div > form > div")))
                    phonee.click()
                    time.sleep(5)
                    phonee = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        "body > div > div > div > div > div > div.col-xs-4 > enable-switch > div > form > div")))
                    phonee.click()

                    break
                if (check % 5 == 0):
                    driver.delete_all_cookies()

                    count += 1
                    driver.get('chrome-extension://addncelkdjfgpipbhnnmfmjeglhbppgl/control.html')
                    phonee = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        "body > div > div > div > div > div > div.col-xs-4 > enable-switch > div > form > div")))
                    phonee.click()
                    time.sleep(5)
                    phonee = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        "body > div > div > div > div > div > div.col-xs-4 > enable-switch > div > form > div")))
                    phonee.click()

                    break

                driver.delete_all_cookies()
                driver.refresh()

                if (recount < (len(fnumbers) - 1)):
                    recount = recount + 1
                else:
                    recount = 0
                print(count)
                if (count % 5 == 0):
                    driver.delete_all_cookies()


                    count+=1
                    driver.get('chrome-extension://addncelkdjfgpipbhnnmfmjeglhbppgl/control.html')
                    phonee = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        "body > div > div > div > div > div > div.col-xs-4 > enable-switch > div > form > div")))
                    phonee.click()
                    time.sleep(5)
                    phonee = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        "body > div > div > div > div > div > div.col-xs-4 > enable-switch > div > form > div")))
                    phonee.click()
                    break
                count = count + 1
            except Exception as e:

               while(1):
                try:

                    driver.delete_all_cookies()

                    count += 1
                    driver.get('chrome-extension://addncelkdjfgpipbhnnmfmjeglhbppgl/control.html')
                    phonee = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        "body > div > div > div > div > div > div.col-xs-4 > enable-switch > div > form > div")))
                    phonee.click()
                    time.sleep(5)
                    phonee = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        "body > div > div > div > div > div > div.col-xs-4 > enable-switch > div > form > div")))
                    phonee.click()

                    break
                except Exception as e:
                    print("masla")

                    pass





