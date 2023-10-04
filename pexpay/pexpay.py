import undetected_chromedriver.v2 as webdriver
import time
import  random
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import base64
from solver1 import PuzleSolver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import re



fnumbers=["1958661276","1958664089","1958540958","1958662632","1958665270","1958543297","1958663948","1958541426","1958663426","1941345642","1958651595","1958663806","1958540719","1958661501","1958664239","1958666778","1958662689","1958665208","1958651955","1958663521","1958652164","1958661697","1958664434","1958669499","1958663081","1963929059","1958651805","1958663812","1958652636","1958661817","1958664485","1958541675","1958546642","1931488114","1958662027","1958664833","1958549143","1958663037","1971810682","1958651708","1958663721","1958540026","1958662699","1952571201","1958541833","1958546919","1948178411","1958661473","1958664211","1958667408","1958663401","1937216913","1958661431","1958664169","1958662870","1932579589","1958542862","1958663694","1958541388","1958663061","1919750576","1976987089","1958663698","1958652906","1958661948","1958664612","1958540504","1958662677","1958665254","1958541798","1958663749","1958652369","1958650550","1958661976","1958662766","1958663394","1958663595","1958664117","1958664599","1958544681","1958546184","1958653078","1958540606","1958658025","1958661391","1958664137","1958541271","1958662684","1958665370","1958543246","1958663996","1958666604","1958663476","1929863663","1958650014","1958663854","1958540807","1958661549","1958664287","1958667073","1958662737","1958665287","1958651751","1958663569","1958652249","1958661810","1958664482","1958550229","1958663132","1955790038","1958651703","1958663860","1958652941","1958661917","1958664533","1946368958","1958546704","1948504594","1958662090","1958664882","1958542034","1958663086","1947849630","1958651402","1958663769","1958540116","1958662747","1951457173","1958665325","1958546971","1958544782","1958661521","1958664259","1958669121","1958663450","1948557309","1958661479","1958664217","1958662930","1962570313","1958651158","1958663742","1958541464","1958663109","1960795811","1958651772","1958663746","1958652977","1958662000","1958664813","1958540596","1958662725","1958665357","1958541747","1958663797","1958652522","1958650335","1958661992","1958662769","1958663402","1958663597","1958664118","1958664603","1958544682","1958546211","1958653126","1958540621","1958666010","1958661447","1958664185","1958541499","1958662732","1959456633","1958665870","1958664044","1958668256","1958546631","1952525534","1958543503","1958663902","1958541040","1958661597","1958664335","1958667522","1958662788","1958665375","1958650833","1958663617","1958652402","1958661914","1958664530","1958551395","1958663182","1963928987","1958651652","1958663908","1958653017","1958661968","1958664581","1945089278","1958546769","1966469578","1958662258","1958664930","1958541779","1958663138","1963928610","1958651096","1958663817","1958540468","1958662799","1935262691","1958660011","1958547023","1958544864","1958661569","1958664307","1958670034","1958663499","1973693553","1958661527","1958664265","1958663009","1945088976","1958650903","1958663790","1958657349","1958663162","1960817032","1958650497","1958663794","1958540246","1958662064","1958664862","1958540678","1958662776","1954575270","1958651216","1958663845","1958652600","1958650091","1958661994","1958662802","1958663403","1958663600","1958664119","1958664606","1958544731","1958546212","1958653153","1958540622","1958666011"]
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
        #bg = body > div.bcapc - popup.bs - popup.bcapc - popup - lang - en > div > div.bs - content > div.bs - main - image
        #pic = body > div.bcapc - popup.bs - popup.bcapc - popup - lang - en > div > div.bs - content > div.bs - main - image > div
        canvas = driver.find_element(By.CSS_SELECTOR,
                                     'body > div.bcapc-popup.bs-popup.bcapc-popup-lang-en > div > div.bs-content > div.bs-main-image')

        # canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)
        canvas_base64 = canvas.get_attribute('style')
        canvas_b= re.findall('\(\"(.*?)\"\)', str(canvas_base64))
        canvas_b=str(canvas_b)
        canvas_b= canvas_b[:-2]
        canvas_b=canvas_b[2:]
        canvas_b=canvas_b[5:]

        print('str',str(canvas_b))
        scr='http'+str(canvas_b)
        print(scr)

        canvas_png = urllib.request.urlretrieve(scr, "screen.png")
        from PIL import Image, ImageDraw as D
        i = Image.open("D:\\autologinbot-master\\bling x\\pexpay\\screen.png")
        #draw = D.Draw(i)
        #draw.rectangle([(1, 0), (65, 195)], outline="white",fill ="#ffff33")
        box = (60, 0, 369, 190)
        i = i.crop(box)
        i.save("D:\\autologinbot-master\\bling x\\pexpay\\screen.png")
        # canvas_png = base64.b64decode(canvas_base64)

        # with open(r"shot.png", 'wb') as f:
        #   f.write(canvas_png)

        canvas1 = driver.find_element(By.CSS_SELECTOR,
                                      'body > div.bcapc-popup.bs-popup.bcapc-popup-lang-en > div > div.bs-content > div.bs-main-image > div')
        # canvas_base641 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas1)

        canvas_base641 = canvas1.get_attribute('style')
        canvas_base641 = re.findall('\(\"(.*?)\"\)', str(canvas_base641))
        canvas_base641 = str(canvas_base641)
        canvas_base641 = canvas_base641[:-2]
        canvas_base641 = canvas_base641[2:]
        canvas_base641 = canvas_base641[5:]


        sho = 'http' + str(canvas_base641)
        print(sho)
        # canvas_png1 = base64.b64decode(canvas_base641)
        canvas_png1 = urllib.request.urlretrieve(str(sho), "shot.png")
        i = Image.open("D:\\autologinbot-master\\bling x\\pexpay\\shot.png")
        # draw = D.Draw(i)
        # draw.rectangle([(1, 0), (65, 195)], outline="white",fill ="#ffff33")
        box = (1, 0, 60, 195)
        i = i.crop(box)
        i.save("D:\\autologinbot-master\\bling x\\pexpay\\shot.png")

        # with open(r"screen.png", 'wb') as f:
        #   f.write(canvas_png1)
        y="shot.png"

        o="screen.png"



        solver = PuzleSolver(y, o)
        solution,x_inf, y_sup, y_inf,w = solver.get_position()
        print(x_inf, y_sup, y_inf,w)


        button = driver.find_element(By.CSS_SELECTOR,'body > div.bcapc-popup.bs-popup.bcapc-popup-lang-en > div > div.bs-content > div.verify-slider.bs-slide-container > div.bs-slide-thumb')
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
        print(a)
        print("yaha n")

        pass
while(1):
    options = webdriver.ChromeOptions()
    options.add_argument('--load-extension=D:\\autologinbot-master\\Urbanvpn')
    options.add_argument("--window-size=500,800")
    options.add_argument("--disable-renderer-backgrounding")
    options.add_argument("--disable-backgrounding-occluded-windows")
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option('useAutomationExtension', False)
    mobile_emulation = {"deviceName": "iPhone SE"}
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"
    driver = webdriver.Chrome(options=options,use_subprocess=True)
    i = random.randint(2, 57)
    driver.get("chrome-extension://ecokmenakcanpnkbgifdiacoapdmhdjf/popup/index.html#/welcome-consent")
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "body > div > div > div.simple_layout__header > div"))).click()
    except:
        pass

    WebDriverWait(driver, 120).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR,
             "body > div > div > div.simple_layout__body > div > div > div > button.button_pink.agreement_agree"))).click()
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        "body > div > div > div.main_layout__body > div.location-box > div > div:nth-child(1) > input"))).click()
    time.sleep(2)
    ph = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div/div[3]/div[2]/div/div[2]/div/ul/li[" + str(i) + "]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", ph);
    ph.click()
    time.sleep(2)
    print('country is: ' + str(i))
    i = 0
    driver.get('https://accounts.pexpay.co/en/register')

    while (1):
        try:

            time.sleep(5)

            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#tab-mobile')))
            phonee.click()

            #driver.execute_script("""
             #  var attr = document.querySelector('div[class^=" css-1f36k5w"]');
            #   attr.remove();
            #""")

            phonssee = driver.find_element(By.CSS_SELECTOR,("div[class^=' css-jt6etj']"))
            phonssee.click()

            time.sleep(1)
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH,'//input[@placeholder="Search"]')))
            phonee.send_keys("bangladesh")
            time.sleep(1)
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#\\38 80-BD-Bangladesh\ \(বাংলাদেশ\)')))

            phonee.click()
            time.sleep(2)
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//input[@inputmode="numeric"]')))
            phonee.send_keys(fnumbers[recount])
            time.sleep(1)

            phonees = driver.find_elements(By.XPATH,
                                                '//input[@name=""]')
            phonees[1].send_keys("")
            time.sleep(2)
            phonee = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH,
                                                '/html/body/div[1]/div[2]/main/div/div/div[1]/div[2]/div[1]/div[3]/form/button')))
            phonee.click()

            time.sleep(5)
            check=1


            while(1):
                try:

                    if(check%5==0):
                        break
                    time.sleep(9)
                    capcha(driver)

                    phonee = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        '#__APP > div.css-1aombpc > main > div > div.css-vurnku > div.css-1tht3pd > div.css-1e9qqgu > div:nth-child(1) > div > input')))
                    break
                except:

                    try:
                     check=check+1
                     print("ni  hua captcha")
                     phonee = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        'body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_panelshowslide > div.geetest_panel_next > div > div.geetest_panel > div > a.geetest_refresh_1')))
                     phonee.click()
                     print("refreshing")
                    except:
                        pass
            if (check % 5 == 0):
                driver.quit()
                break

            time.sleep(5)
            driver.get('https://accounts.pexpay.co/en/register')
            count = count + 1
            if (count % 10 == 0):
                driver.quit()
                break
            if (recount < (len(fnumbers) - 1)):
                recount = recount + 1
            else:
                recount = 0
            print(count)
        except Exception as e:
            try:
              print(a)


              driver.close()
            except Exception  as e:

                print(a)
                pass

            break



