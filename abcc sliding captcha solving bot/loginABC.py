import undetected_chromedriver.v2 as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

import random

from PIL import Image, ImageChops
from numpy import array
from selenium.webdriver.common.by import By
import requests, io, re
import easing


def convert_css_to_offset(px):
    ps = px.replace('px', '').split(' ')
    x = -int(ps[0])
    y = -int(ps[1])
    return x, y, x + 10, y + 58


def convert_index_to_offset(index):
    row = int(index / 26)
    col = index % 26
    x = col * 10
    y = row * 58
    return x, y, x + 10, y + 58


def get_slider_offset_from_diff_image(diff):
    im = array(diff)
    width, height = diff.size
    diff = []
    for i in range(height):
        for j in range(width):
            # black is not only (0,0,0)
            if im[i, j, 0] > 15 or im[i, j, 1] > 15 or im[i, j, 1] > 15:
                diff.append(j)
                break
    return min(diff)


def get_slider_offset(image_url, image_url_bg, css):
    image_file = io.BytesIO(requests.get(image_url).content)
    im = Image.open(image_file)
    image_file_bg = io.BytesIO(requests.get(image_url_bg).content)
    im_bg = Image.open(image_file_bg)
    # im.show()
    # im_bg.show()

    # 10*58 26/row => background image size = 260*116
    captcha = Image.new('RGB', (260, 116))
    captcha_bg = Image.new('RGB', (260, 116))
    for i, px in enumerate(css):
        offset = convert_css_to_offset(px)
        region = im.crop(offset)
        region_bg = im_bg.crop(offset)
        offset = convert_index_to_offset(i)
        captcha.paste(region, offset)
        captcha_bg.paste(region_bg, offset)
    diff = ImageChops.difference(captcha, captcha_bg)
    # captcha.show()
    # captcha_bg.show()
    # diff.show()
    diff.save('D:/diff.png')
    return get_slider_offset_from_diff_image(diff)


def get_image_css(images):
    css = []
    for image in images:
        position = get_image_position_from_style(image.get_attribute("style"))
        css.append(position)
    return css


def get_image_url_from_style(style):
    match = re.match('background-image: url\("(.*?)"\); background-position: (.*?);', style)
    return match.group(1)


def get_image_position_from_style(style):
    match = re.match('background-image: url\("(.*?)"\); background-position: (.*?);', style)
    return match.group(2)


def get_slice_offset(slice):
    style = slice.get_attribute("style")
    match = re.search('background-image: url\("(.*?)"\);', style)
    url = match.group(1)
    image_file = io.BytesIO(requests.get(url).content)
    im = Image.open(image_file)
    im.save('D:/slice.png')
    return get_slider_offset_from_diff_image(im)


# refer: https://ask.hellobi.com/blog/cuiqingcai/9796
def get_track(distance):
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


def fake_drag(browser, knob, offset):
    # seconds = random.uniform(2, 6)
    # print(seconds)
    # samples = int(seconds*10)
    # diffs = sorted(random.sample(range(0, offset), samples-1))
    # diffs.insert(0, 0)
    # diffs.append(offset)
    # ActionChains(browser).click_and_hold(knob).perform()
    # for i in range(samples):
    #     ActionChains(browser).pause(seconds/samples).move_by_offset(diffs[i+1]-diffs[i], 0).perform()
    # ActionChains(browser).release().perform()

    # tracks = get_track(offset)
    offsets, tracks = easing.get_tracks(offset, 12, 'ease_out_expo')
    print(offsets)
    ActionChains(browser).click_and_hold(knob).perform()
    for x in tracks:
        ActionChains(browser).move_by_offset(x, 0).perform()
    ActionChains(browser).pause(0.5).release().perform()

    return


def do_crack(browser):
    slice = browser.find_element(By.CLASS_NAME,"gt_slice")
    slice_offset = get_slice_offset(slice)
    print(slice_offset)

    images = browser.find_elements_by_class_name("gt_cut_fullbg_slice")
    images_bg = browser.find_elements_by_class_name("gt_cut_bg_slice")
    image_url = get_image_url_from_style(images[0].get_attribute("style"))
    image_url_bg = get_image_url_from_style(images_bg[0].get_attribute("style"))
    css = get_image_css(images)
    offset = get_slider_offset(image_url, image_url_bg, css)
    print(offset)

    knob = browser.find_element(By.CLASS_NAME,"gt_slider_knob")
    # ActionChains(browser).drag_and_drop_by_offset(knob, offset - slice_offset, 0).perform()
    fake_drag(browser, knob, offset - slice_offset)
    return


import string
import random
import time
def convertTuple(tup):
        # initialize an empty string
    strc = ''
    c=len(tup)
    
    for item in range(5):
        strc=strc+strc.join(tup[item])
        
    return strc


if __name__ == "__main__":
    letters = string.ascii_lowercase

    options = uc.ChromeOptions()
    options.add_extension('extension_1_6_6_0.crx')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    mobile_emulation = {"deviceName": "iPhone SE"}
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"
    # options.add_experimental_option("mobileEmulation", mobile_emulation)
    count = 0
    recount = 0
    while (1):
        while (1):
            numb = "0123456789"

            url = 'https://abcc.com/en/settings/bind/phone'
            strr = ["099"], random.choices(numb, k=1), ["-4"], random.choices(numb, k=1), random.choices(numb,
                                                                                                         k=1), random.choices(
                numb, k=1)

            yo = convertTuple(strr)

            rt = url.replace("0995-4521", yo)

            fnumbers = ["3308697336", "3308697337", "3308697338", "3308697339", "3308697340", "3308697341",
                        "3308697342", "3308697344", "3308697345", "3308697346", "3308697347", "3308697348",
                        "3308697349", "3308697350", "3308697351", "3308697354", "3308697355", "3308697356",
                        "3308697357", "3308697358", "3308697359", "3308697362", "3308697363", "3308697364",
                        "3308697365", "3308697367", "3308697368", "3308697369", "3308697352", "3308697370",
                        "3308697371", "3308697372", "3308697374", "3308697375", "3308697376", "3308697377",
                        "3308697378", "3308697379", "3308697381", "3308697383", "3308697384", "3308697385",
                        "3308697386", "3308697387", "3308697388", "3308697393", "3308697396", "3308697398",
                        "3308697399", "3308697402", "3308697419", "3308697421", "3308697422", "3308697424",
                        "3308697425", "3308697426", "3308697427", "3308697428", "3308697431", "3308697432",
                        "3324978172", "3341597500", "3341597700", "3341597900", "3341598100", "3341598300",
                        "3341598500", "3341598700", "3341598900", "3341599100", "3341599300", "3341599500",
                        "3341599700", "3341599900", "3345740100", "3345740300", "3345740500", "3345740700",
                        "3345740900", "3345741100", "3345741300", "3345741500", "3345741700", "3345741900",
                        "3345742100", "3324978190", "3341597501", "3341597701", "3341597901", "3341598101",
                        "3341598301", "3341598501", "3341598701", "3341598901", "3341599101", "3341599301",
                        "3341599501", "3341599701", "3341599901", "3345740101", "3345740301", "3345740501",
                        "3345740701", "3345740901", "3345741101", "3345741301", "3345741501", "3345741701",
                        "3345741901", "3345742101", "3324978217", "3341597502", "3341597702", "3341597902",
                        "3341598102", "3341598302", "3341598502", "3341598702", "3341598902", "3341599102",
                        "3341599302", "3341599502", "3341599702", "3341599902", "3345740102", "3345740302",
                        "3345740502", "3345740702", "3345740902", "3345741102", "3345741302", "3345741502",
                        "3345741702", "3345741902", "3345742102", "3324978225", "3341597503", "3341597703",
                        "3341597903", "3341598103", "3341598303", "3341598503", "3341598703", "3341598903",
                        "3341599103", "3341599303", "3341599503", "3341599703", "3341599903", "3345740103",
                        "3345740303", "3345740503", "3345740703", "3345740903", "3345741103", "3345741303",
                        "3345741503", "3345741703", "3345741903", "3345742103"];

            numbers = []
            # for x  in range(len(fnumbers)):
            # c=fnumbers[x]

            # rwithout=c.replace("+880","")
            #  numbers.append(rwithout)
            # time.sleep(8)

            # get first child window

            # time.sleep(5)
            # usernas = WebDriverWait(browser, 120).until(
            #   EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Log in to rider, driver, and delivery sites"]')))
            # usernas.click()
            # time.sleep(20)
            # try:
            # usernasp = WebDriverWait(browser, 120).until(
            #   EC.presence_of_element_located((By.XPATH, '//li[@class="gu bl ij b8"]')))
            # usernasp.click()
            # usernasp = WebDriverWait(browser, 120).until(
            #  EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div/div[6]/section/div/div/div/div/div[5]/a')))
            # usernasp.click()

            # print("signin clciked")

            # except NoSuchElementException:
            #   browser.close()
            #   break

            # time.sleep(10)
            # usernas = WebDriverWait(browser, 120).until(
            # EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Log in to rider, driver, and delivery sites"]')))
            # browser.execute_script("window.stop();")

            # usernas.click()
            # time.sleep(10)
            # try:
            # usernasp =browser.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div/div[6]/section/div/div/div/div/div[3]/a')
            # usernasp.click()

            #  print("signin clciked")
            #  time.sleep(20)
            # phone = browser.find_element_by_xpath('//*[@id="answerForm"]/div[1]/div/div[1]/div/div[1]/div/div/select')
            # ph one = browser.find_element_by_class_name('hwid-input hwid-input-pwd')
            # phone.click()
            # except NoSuchElementException:
            #   browser.close()
            #   break
            while (1):
                browser = uc.Chrome()
                time.sleep(50)
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

                usernap.send_keys(passwordStr)
                time.sleep(5)
                usernap = WebDriverWait(browser, 120).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="submit"]/button')))

                usernap.click()
                time.sleep(10)
                do_crack(browser)

                time.sleep(10)
                usernap = WebDriverWait(browser, 120).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div[11]/div[2]/div/button')))

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
                    if (count % 5 == 0):
                        browser.get('chrome-extension://mjnbclmflcpookeapghfhapeffmpodij/control.html')
                        phonesp = WebDriverWait(browser, 120).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR,
                                                            'body > div > div > div > div > div > div.col-xs-4 > enable-switch > div > form > div > div > span.bootstrap-switch-label')))
                        phonesp.click()
                        time.sleep(5)
                        phonesp = WebDriverWait(browser, 120).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR,
                                                            'body > div > div > div > div > div > div.col-xs-4 > enable-switch > div > form > div > div > span.bootstrap-switch-label')))
                        phonesp.click()
                        time.sleep(5)

                        chwd = browser.window_handles

                        if (len(chwd) >= 2):
                            browser.switch_to.window(chwd[1])

                            browser.close()
                            browser.switch_to.window(chwd[0])
                            letters = string.ascii_lowercase

      




     
     
     
  
