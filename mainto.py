import random
import select
import selenium.webdriver.common.by
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import bot
ad=bot.ad
soyad=bot.soyad
browser = webdriver.Chrome()
tobrowser = webdriver.Chrome()
tobrowser.get('https://gecicimail.com.tr/')
time.sleep(6)
tobrowser.find_element(By.CSS_SELECTOR, "#deleteEmailAddress > i").click()
time.sleep(3)
kopya = tobrowser.find_element(By.CSS_SELECTOR, "#copyEmailAddress > i").click()
browser.get('https://www.instagram.com/accounts/emailsignup/')
time.sleep(4)
email = browser.find_element(By.XPATH,"//input[@name='emailOrPhone']")
email.send_keys(ad+soyad)
fullname=browser.find_element(By.NAME,"fullName")
fullname.send_keys(ad,soyad)
time.sleep(5)
userline=random.randint(1,3)
userlink = browser.find_element(By.XPATH,"//div/div/button/span")
if userline==1:
    userlink.click()
elif userlink==2:
    userlink.click()
    time.sleep(2)
    userlink.click()
elif userline==3:
    userlink.click()
    userlink.click()
    userlink.click()

email.send_keys(Keys.CONTROL,"a")
email.send_keys(Keys.DELETE)
time.sleep(2)
email.send_keys(Keys.CONTROL,"v")
email=email.text
password=browser.find_element(By.NAME,"password")
password.send_keys("İnsPars5404")
c1=browser.find_element(By.CSS_SELECTOR,".x1xmf6yo:nth-child(1) > .\_acan").click()
time.sleep(4)
moon=browser.find_element(By.CSS_SELECTOR,".\_aav3:nth-child(1) > .\_aau-")
drp=Select(moon)
ay=random.randint(1,12)
drp.select_by_value(str(ay))
day=browser.find_element(By.CSS_SELECTOR,".\_aav3:nth-child(2) > .\_aau-")
drp=Select(day)
gun=random.randint(1,28)
drp.select_by_value(str(gun))
year=browser.find_element(By.CSS_SELECTOR,".\_aav3:nth-child(3) > .\_aau-")
drp=Select(year)
yil=random.randint(1981,2004)
drp.select_by_value(str(yil))
c2=browser.find_element(By.CSS_SELECTOR,".\_acap").click()
time.sleep(4)
ekontrol=browser.find_element(By.NAME,"email_confirmation_code")
print("E posta kontrol ediliyor")
def SystemState():
    try:
        time.sleep(15)
        code=tobrowser.find_element(By.XPATH,"//*[@id='inboxTable']/tbody/tr/td[2]").text
        code=code.split()
        print(code[0])
        code=code[0]
        if code=="Herhangi":
            print("tekrar deniyorum")
            return SystemState()
        else:
            print("kod bulundu")
            return code
    except:
        return SystemState()
SystemState()
ekontrol.send_keys(SystemState())
c3=browser.find_element(By.CSS_SELECTOR,".\_acan").click()
time.sleep(25)
browser.close()
tobrowser.close()
browser=webdriver.Chrome()
browser.get("https://www.instagram.com")
time.sleep(8)
browser.find_element(By.NAME,"username").send_keys(Keys.CONTROL,"v")
browser.find_element(By.NAME,"password").send_keys("İnsPars5404")
c4=browser.find_element(By.XPATH,"//*[@id='loginForm']/div[1]/div[3]/button/div").click()
time.sleep(10)
browser.get("https://www.instagram.com")
time.sleep(8)
browser.close()
browser=webdriver.Chrome
browser.get("https://www.instagram.com")
time.sleep(8)
browser.find_element(By.NAME,"username").send_keys(Keys.CONTROL,"v")
browser.find_element(By.NAME,"password").send_keys("İnsPars5404")
time.sleep(5)
browser.get("https://www.instagram.com")
time.sleep(5)
c7=browser.find_element(By.XPATH,"//*[@id='mount_0_0_/C']/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[6]/div/div/a").click
time.sleep(8)
profile=browser.find_element(By.XPATH,"//*[@id='mount_0_0_/C']/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/a/h2").text
print(profile)