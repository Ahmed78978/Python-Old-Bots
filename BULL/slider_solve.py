from selenium import webdriver
import time

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import base64
from solver import PuzleSolver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
#options.add_extension('extension_1_6_6_0.crx')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
mobile_emulation = {"deviceName": "iPhone SE"}
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"


fnumbers=["1954634697","1952367631","1942914216","1963716732","1925257455","1934839955","1966475775","1937660693","1932198114","1931957774","1949874132","1974805429","1939095820","1922566397","1977486889","1931383102","1939778923","1952348616","1952579448","1953028242","1946843509","1958542550","1958659606","1401791954","1937597392","1939640556","1937181769","1999561253","1936255456","1975426982","1934656551","1934111357","1984743949","1929971104","1935197912","1932783329","1960633526","1931588225","1946880867","1978429426","1947847076","1953878082","1938107981","1981497507","1951195737","1930391371","1979842668","1934081928","1930898846","1952275317"]
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


        canvas = driver.find_element(By.CSS_SELECTOR,'body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_panelshowslide > div.geetest_panel_next > div > div.geetest_wrap > div.geetest_widget > div > a > div.geetest_canvas_img.geetest_absolute > div > canvas.geetest_canvas_slice.geetest_absolute')

        canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)

        canvas_png = base64.b64decode(canvas_base64)

        with open(r"shot.png", 'wb') as f:
            f.write(canvas_png)

        canvas1 = driver.find_element(By.CSS_SELECTOR,'body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_panelshowslide > div.geetest_panel_next > div > div.geetest_wrap > div.geetest_widget > div > a > div.geetest_canvas_img.geetest_absolute > div > canvas.geetest_canvas_bg.geetest_absolute')

        canvas_base641 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas1)

        canvas_png1 = base64.b64decode(canvas_base641)

        with open(r"screen.png", 'wb') as f:
            f.write(canvas_png1)
        y="D:\\autologinbot-master\\bling x\geetest_slider-captha-master\shot.png"

        o="D:\\autologinbot-master\\bling x\geetest_slider-captha-master\screen.png"



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

        pass
while(1):
    driver = webdriver.Chrome(options=options)
    driver.get('https://passport.webull.com/auth/simple/signup?source=seo-google-home&hl=en&redirect_uri=https%3A%2F%2Fwww.webull.com%2F')

    while (1):
        try:

            time.sleep(5)

            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//div[@class="jss27"]')))
            phonee.click()
            time.sleep(1)
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                'body > div:nth-child(11) > ul > li:nth-child(131)')))
            phonee.click()
            time.sleep(1)
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH,'//input[@placeholder="Phone Number"]')))
            phonee.send_keys[fnumbers[recount]]
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//div[@class="jss74"]')))
            phonee.click()

            time.sleep(20)


            capcha(driver)
            time.sleep(5)
            driver.refresh()
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



