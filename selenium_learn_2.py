import selenium 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from selenium import webdriver
import os 
import requests

os.environ['PATH']+= r"C:\Users\kaifk\lpth\.vscode"

driver=webdriver.Chrome()

driver.get("http://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.implicitly_wait(40)

element=driver.find_element(by="id", value= "user-message")

element.send_keys("hello kaif")
input()

driver.quit()
