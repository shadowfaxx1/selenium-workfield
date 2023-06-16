import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
import os 
import time
webdriver_path = r"C:\path\to\chromedriver.exe"
os.environ['PATH']+=r"C:\Users\kaifk\lpth\.vscode"

driver=webdriver.chrome()
driver.get("http://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.implicitly_wait(10)

e=driver.find_element(by='id' , value='isAgeSelected')
e.click()

time.sleep(100)
driver.quit()