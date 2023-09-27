from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

# install/upgrade chromedriver 
# choco install chromedriver
# choco upgrade chromedriver

# generate exe
# pyinstaller --onefile play-rcv-selenium.py

url = "https://radios.vpn.sapo.pt/CV/radio7.mp3"

options = Options()
options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
driver = webdriver.Chrome(options = options)
# driver = webdriver.Chrome(chrome_options = options, executable_path=r'C:\ProgramData\chocolatey\lib\chromedriver\tools\chromedriver.exe')

driver.get(url)

while True:
    current_minute = time.localtime().tm_min
    if current_minute in [1, 31]:
        print('Refreshing page ...')    
        driver.refresh()
    
    print('Sleeping ...')
    time.sleep(45)
