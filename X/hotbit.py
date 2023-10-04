import undetected_chromedriver.v2 as uc
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


fnumbers=["1401791946","1407006436","1407165690","1903727826","1913585104","1917154196","1917891548","1919319731","1921400639","1927769481","1928057658","1928658631","1928701107","1929147854","1929854801","1930929383","1930966975","1931655742","1932483300","1933622762","1933858972","1934661913","1935198284","1936920806","1937184662","1937184948","1937996067","1937997929","1937998840","1938050106","1938449829","1938489069","1938669364","1939639751","1939776243","1940093623","1941090091","1942797392","1943209906","1943210198","1943390572","1943957898","1943959357","1943959986","1944036225","1945089238","1946086356","1946842904","1947089920","1947154635","1947352518","1947780685","1948353795","1948421297","1948559867","1949090796","1950960879","1951024482","1951312506","1951994762","1952144687","1952860613","1953150212","1954626732","1958541681","1958542140","1958542242","1958542395","1958542548","1958542599","1958543211","1958546837","1958547024","1958547245","1958547274","1958547296","1958547411","1958547523","1958547579","1958547635","1958549371","1958650181","1958650385","1958651762","1958658788","1958659400","1958659706","1958660828","1958661610","1958661831","1958662154","1958662384","1958662547","1958662853","1958665214","1963834335","1963928392","1963929775","1963930974","1964285067","1965365711","1966476148","1966764413","1966765984","1967520915","1976543599","1978405956","1979685360","1982786549","1984236478","1958665046","1958661899","1958658635","1958662103","1958661338","1958541630","1958547355","1958546684","1958542701","1958541936","1958665326","1958661797","1958651456","1958650742","1958542497","1958541783","1958650793","1958541732","1958651558","1958543415","1958542752","1958541834","1931912388","1958650997","1958650436","1958650232","1958542905","1958542650","1958542191","1958661950","1958661295","1958661418","1958661466","1958661514","1958661562","1958661658","1958661720","1958661924","1958661975","1958662035","1958662095","1958662263","1958662327","1958662439","1958662496","1958662598","1958662653","1958662701","1958662749","1958662801","1958662914","1958662992","1958663042","1958663090","1958663142","1958663192","1958663242","1958663291","1958663341","1958663393","1958663442","1958663491","1958546649","1958546710","1958546775","1958546855","1958546920","1958542293","1958661389","1943957881","1958659451","1936920823","1958651864","1942413406","1974846232","1958659655","1958658686","1928041174","1958662256","1958658737","1946844671","1958546972","1958547076","1958547142","1958547190","1958663532","1958663580","1958663628","1958663676","1958663724","1958663772","1958663820","1958663868","1958663916","1958663964","1958664012","1958664060","1958664108","1958664156","1958664204","1958664252","1958664300","1958664348","1958664396","1958664444","1958664492","1958664540","1958664588","1958664692","1958664838","1958664887","1958664935","1958664983","1958665117","1958665165","1958665317","1958544629","1958544706","1958544783","1958544865","1958544941","1958545017","1958545093","1958545169","1958545245","1958545321","1958545397","1958545473","1958545702","1958545778","1958545855","1958545931","1958546007","1958546083","1958546159","1958546235","1958546311","1958546387","1958546463","1958546539","1958652178","1958652261","1958652337","1958652413","1958652489","1958652566","1958652644","1958652720","1958652797","1958652873","1958652949","1958653025","1958540030","1958540119","1958540208","1958540294","1958540381","1958540471","1958540564","1958540646","1958540738","1958540823","1958540900","1958540978","1958541214","1958541290","1958541366","1958541442","1958541518","1958541595","1958654948","1958656885","1958657819","1958666054","1958666200","1958666344","1958666798","1958666964","1958667103","1958667250","1958667393","1958667550","1958667693","1958667847","1958667990","1958668144","1958668299","1958669534","1958669743","1958669982","1958670217","1958670436","1958670641","1958670873","1958549879","1958550385","1958550496","1958550629","1958550751","1958550873","1958550990","1958551124","1958551255","1958551414","1958551553","1958551681"]

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
              options = uc.ChromeOptions()
              options.add_argument('--load-extension=D:\\autologinbot-master\\UltraSur')


              options.add_argument("--disable-renderer-backgrounding")
              options.add_argument("--disable-backgrounding-occluded-windows")

              driver = uc.Chrome(options=options,version_main=105)

              break
           except:



               pass
        while(1):

         while (1):
            try:
                while (1):
                    try:
                        driver.get('https://www.hotbit.io/register')
                        break
                    except:
                        pass

                time.sleep(5)

                phonee = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#app > div.user-common-page.register-page > div.user-container > div > div.register-form-wrap > div.button-type-box > button.__h-button.new-btn.__default')))
                phonee.click()

                # driver.execute_script("""
                #  var attr = document.querySelector('div[class^=" css-1f36k5w"]');
                #   attr.remove();
                # """)



                time.sleep(1)
                phonee = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#app > div.user-common-page.register-page > div.user-container > div > div.register-form-wrap > div.form-box > div:nth-child(1) > div > span')))
                phonee.click()
                time.sleep(1)
                phonee = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    "//*[text()='Bangladesh']")))
                phonee.click()
                time.sleep(2)
                phonee = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    '//input[@name="phone"]')))
                phonee.send_keys(fnumbers[recount])
                time.sleep(1)


                phonee = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#captchaBoxBind > div')))
                phonee.click()

                time.sleep(5)
                check = 1

                error = False

                while (1):
                    try:

                        if (check % 5 == 0):
                            break
                        time.sleep(2)
                        check = check + 1
                        capcha(driver)
                        time.sleep(2)
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
                            pass
                        phonee = WebDriverWait(driver, 2).until(
                            EC.presence_of_element_located((By.XPATH,
                                                            '//div[@data-popover="register_phone"]')))
                        resend_dis = phonee.get_attribute("style")
                        if resend_dis.find("display") == -1:
                            error = True
                            break

                        phonee = WebDriverWait(driver, 2).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR,
                                                            '#captchaBoxBind > div > button')))
                        resend = phonee.get_attribute("disabled")

                        break
                    except:
                        pass

                if (error == True):
                    driver.quit()
                    break
                if (check % 5 == 0):
                    driver.quit()
                    break


                driver.refresh()

                if (recount < (len(fnumbers) - 1)):
                    recount = recount + 1
                else:
                    recount = 0
                print(count)
                if (count % 5 == 0):
                    driver.delete_all_cookies()


                    count+=1
                    driver.get('chrome-extension://jnckhdjpjmofalipcflghpnmihgnnhee/control.html')
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





