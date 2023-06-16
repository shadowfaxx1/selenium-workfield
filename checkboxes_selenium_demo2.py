
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os 
from selenium.webdriver.common.by import By

import time
webdriver_path = r"C:\path\to\chromedriver.exe"
os.environ['PATH']+=r"C:\Users\kaifk\lpth\.vscode" + webdriver_path

driver=webdriver.Chrome()
driver.get("http://demo.seleniumeasy.com/basic-checkbox-demo.html")
driver.implicitly_wait(10)

e=driver.find_element(by='id' , value='isAgeSelected')
e.click()

wait= WebDriverWait(driver,20)

try:
    btn= wait.until(ec.visibility_of_element_located((By.ID , 'check1')))
except:
    print("error finding button ")

btn.click()
# wait.until(ec.text_to_be_present_in_element((By.ID, 'isChkd'), 'true'))
time.sleep(3)
# if(btnz.text =="Uncheck All" ):
#     print(btnz.text)
chck=driver.find_element(By.CLASS_NAME,"cb1-element")
chck.click()

time.sleep(10)
driver.quit()