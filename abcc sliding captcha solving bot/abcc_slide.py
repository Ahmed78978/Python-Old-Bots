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


fnumbers=["3324974299","3310156215","3368060237","3368670587","3368988458","3369574568","3370338067","3370771209","3324974310","3314385265","3368059750","3368670488","3368988454","3369572855","3370338065","3370771132","3324974328","3314418195","3368059184","3368669489","3368988439","3369571599","3370337850","3370770693","3359115878","3359115083","3359114637","3359114395","3359114352","3359114307","3359112784","3359105219","3359105217","3359104168","3359104135"]
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
        y="D:\\autologinbot-master\geetest_slider-captha-master\shot.png"

        o="D:\\autologinbot-master\geetest_slider-captha-master\screen.png"



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
  try:


      # options.add_experimental_option("mobileEmulation", mobile_emulation)
      count = 0
      recount = 0
      while (1):
          while (1):
              numb = "0123456789"

              url = 'https://abcc.com/en/settings/bind/phone'





              numbers = []

              while (1):
                  browser = webdriver.Chrome(options=options, desired_capabilities=capa)
                  time.sleep(10)
                  chwd = browser.window_handles
                  actions = ActionChains(browser)
                  if (len(chwd) >= 2):
                      browser.switch_to.window(chwd[1])

                      browser.close()
                      browser.switch_to.window(chwd[0])

                  # userna = WebDriverWait(browser, 30).until(
                  #  EC.presence_of_element_located((By.XPATH, '//*[@id="answerForm"]/div[1]/div/div[1]/div/div[1]/div/div/select/option[198]')))
                  # userna.click()
                  # phone = WebDriverWait(browser, 120).until(
                  # EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button')))
                  # phone = browser.find_element_by_class_name('hwid-input hwid-input-pwd')
                  # phone.click()
                  browser.get((url))
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div[2]/div[2]/div/button')))

                  usernap.click()
                  phonee = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.XPATH, '//*[@id="form"]/div[1]/div[1]/input')))

                  phonee.send_keys(usernameStr)
                  time.sleep(3)
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.XPATH, '//*[@id="form"]/div[1]/div[2]/input')))

                  usernap.send_keys(Str)
                  time.sleep(5)
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located((By.XPATH, '//*[@id="submit"]/button')))

                  usernap.click()
                  time.sleep(10)
                  capcha(browser)

                  time.sleep(10)
                  usernap = WebDriverWait(browser, 120).until(
                      EC.presence_of_element_located(
                          (By.XPATH, '/html/body/div[1]/main/div/div[11]/div[2]/div/button')))

                  usernap.click()
                  while (1):
                      browser.get((url))
                      time.sleep(5)
                      phone = WebDriverWait(browser, 120).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          'body > div > main > div > div > div.profile_content > div > div > div.remove-bind_form > div:nth-child(1) > div.v-phone_code > div.code-select_wrap')))
                      phone.click()
                      time.sleep(1)
                      phonesp = WebDriverWait(browser, 120).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          'body > div > main > div > div > div.profile_content > div > div > div.remove-bind_form > div:nth-child(1) > div.v-phone_code > div.code-select_wrap > ul > li:nth-child(159) > span.iti-flag.pk')))
                      phonesp.click()

                      time.sleep(3)
                      phones = WebDriverWait(browser, 120).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          'body > div > main > div > div > div.profile_content > div > div > div.remove-bind_form > div:nth-child(1) > div.v-phone_code > div.input-wrap > input[type=text]')))
                      phones.send_keys(fnumbers[recount])
                      time.sleep(1)
                      phonesp = WebDriverWait(browser, 120).until(
                          EC.presence_of_element_located((By.CSS_SELECTOR,
                                                          'body > div > main > div > div > div.profile_content > div > div > div.remove-bind_form > div.input-wrap.flex.jcsb.message-wrap > div.v-btn.send-code > button')))
                      phonesp.click()
                      time.sleep(10)

                      count = count + 1

                      if (recount <= len(fnumbers) - 1):
                          recount = recount + 1
                      else:
                          recount = 0

                      print(count)
  except Exception as e:
      driver.close()
      break


