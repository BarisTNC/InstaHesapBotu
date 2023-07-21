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
import login
import VeriBase

#BAŞKA BİR KÜTÜPHANEDEN ALDIĞIMIZ VERİLER İLE AD VE SOYAD TANITIYORUZ
ad=bot.ad
soyad=bot.soyad
#TARAYICI AÇIP E-POSTA ADRESİNE YÖNLENDİRİYORUZ
browser = webdriver.Chrome()
wait=WebDriverWait(browser,10)
tobrowser = webdriver.Chrome()
waitto=WebDriverWait(tobrowser,10)
tobrowser.get('https://gecicimail.com.tr/')
time.sleep(6)
#E-POSTA ADRESİ AYNI OLMASIN DİYE İLK ÇIKANI SİLİP 2.Yİ KOPYALAYIP DEVAM EDİYORUZ
waitto.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#deleteEmailAddress > i"))).click()
time.sleep(3)
waitto.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#copyEmailAddress > i"))).click()
#İNSTAGRAM KAYIT SAYFASINA YÖNLEDİRİYORUZ
browser.get('https://www.instagram.com/accounts/emailsignup/')
#İSMİMİZİ VE SOYİSMİMİZİ EPOSTA BÖLÜMÜNE YAPIŞTIRIYORUZ Kİ İSİMVESOYİSMİMİZE YAKIN BİR KULLANICI ADI ALALIM
email = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='emailOrPhone']")))
email.send_keys(ad+soyad)
fullname=browser.find_element(By.NAME,"fullName")
#İSİM SOYİSİM VERİLERİNİ GİRİYORUZ
fullname.send_keys(ad,soyad)
time.sleep(5)
#KULLANICI ADINI İLK ÖNCE EPOSTA VE İSİM GİRİP DAHA SONRA SİTENİN VERMİŞ OLDUĞU OTOMATİK KULLANICI ADI ÜRET BUTONUNA BASARAK KULLANOCI ADI ÜRETİYORUZ
#FAKAT AYNI TARZDA OLMASIN DİYE RASTGELE SEÇİLEN SAYILARA GÖRE YENİLEME YAPIYORUZ
userline=random.randint(1,3)
userlink = wait.until(EC.presence_of_element_located((By.XPATH,"//div/div/button/span")))
if userline==1:
    userlink.click()
elif userline==2:
    userlink.click()
    time.sleep(2)
    userlink.click()
elif userline==3:
    userlink.click()
    userlink.click()
    userlink.click()
else:
    print("yok")
#USERNAMEDEN KULLANICI ADIMIZI ALIP KAYDEDİYORUZ
username = browser.find_element(By.XPATH,"//input[@name='username']")
print(username.get_attribute('value'))
username=username.get_attribute('value')
#EMAİL BÖLMESİNİ TEMİZLEYİP,E-POSTA ADRESİNDEN ALDIĞIMIZ E-POSTAYI İNSTAGRAM E-POSTA BÖLMESİNE YAPIŞTIRIYORUZ
email.send_keys(Keys.CONTROL,"a")
email.send_keys(Keys.DELETE)
time.sleep(2)
email.send_keys(Keys.CONTROL,"v")
email=email.text
#ŞİFREMİZİ GİRİYORUZ
password=browser.find_element(By.NAME,"password")
password.send_keys("İnsPars5404")
#BİR SONRAKİ AŞAMAYA GEÇMEK İÇİN BUTONA BASIYORUZ
c1=browser.find_element(By.CSS_SELECTOR,".x1xmf6yo:nth-child(1) > .\_acan").click()
#BURADA DOĞUM TARİHİMİZİ SEÇİYORUZ TABİ SONUÇLARI RASTGELE OLARAK SEÇTİRİYORUZ...
moon=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".\_aav3:nth-child(1) > .\_aau-")))
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
#EPOSTA GÜVENLİK DOĞRULAMASI İSTİYOR BU ESNADA SYSTEMSTATE() FONKSİYONUYLA BERABER E POSTAMIZI KONTROL EDİYORUZ
ekontrol=wait.until(EC.presence_of_element_located((By.NAME,"email_confirmation_code")))
print("E posta kontrol ediliyor")
def SystemState():
    try:
        code=waitto.until(EC.presence_of_element_located((By.XPATH,"//*[@id='inboxTable']/tbody/tr/td[2]"))).text
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
time.sleep(40)
browser.close()
tobrowser.close()
VeriBase.sqlite(username,ad,soyad)
login.loginuser(username)
