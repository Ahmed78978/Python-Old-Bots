# coding:utf-8
__author__ = 'xxj'


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
from yidun_slider_captcha import slider_captcha


sys.setdefaultencoding('utf-8')


def wangyiyun():
    url = 'https://id.163yun.com/login'
    driver = webdriver.Chrome(
        executable_path=r'C:\Users\xj.xu\Downloads\chromedriver_win32\chromedriver.exe',
    )
    wait = WebDriverWait(driver, 20)
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)

    account = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="account"]')),
                         message='account not exist...')
    account.send_keys('*******')
     = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name=""]')),
                          message=' not exist...')
    .send_keys('******')

    slider_captcha(wait, driver)    # 滑块接口

    button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@class="m-btn m-btn-primary m-btn-large m-btn-submit"]')),
                          message='button not exist...')
    button.click()
    time.sleep(10)


def main():
    wangyiyun()


if __name__ == '__main__':
    main()