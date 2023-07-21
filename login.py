import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import select
import selenium.webdriver.common.by
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import bot
def loginuser(username):
    browser=webdriver.Chrome()
    wait = WebDriverWait(browser, 10)
    browser.get("https://www.instagram.com")
    wait.until(EC.presence_of_element_located((By.NAME,"username"))).send_keys(username)
    wait.until(EC.presence_of_element_located((By.NAME,"password"))).send_keys("İnsPars5404")
    wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='loginForm']/div[1]/div[3]/button/div"))).click()
    time.sleep(8)
    browser.get("https://www.instagram.com")
    time.sleep(10)
    if wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.wbloks_1:nth-child(2) > .wbloks_1 > .wbloks_1 > .wbloks_1 > .wbloks_1 > .wbloks_1:nth-child(2) > .wbloks_1 > .wbloks_1 > .wbloks_1'))):
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.wbloks_1:nth-child(2) > .w*bloks_1 > .wbloks_1 > .wbloks_1 > .wbloks_1 > .wbloks_1:nth-child(2) > .wbloks_1 > .wbloks_1 > .wbloks_1'))).click()
    else:
        pass
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Şimdi Değil')]"))).click()
    time.sleep(20)
    browser.get("https://www.instagram.com/"+(username))