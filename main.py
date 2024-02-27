# Starting use of selenium
# The code just opens and closes the chrome in 10 seconds

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service=Service(executable_path="chromedriver.exe")
driver=webdriver.Chrome(service=service)

driver.get("hhtps://google.com")

time.sleep(10)
driver.quit()