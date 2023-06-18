import selenium 
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
import os 
import time 
webz = r"C:\users\kaifk\chromedriver.exe"
os.environ['PATH']+=r"C:\Users\kaifk\lpth\selenium" + webz

driver=webdriver.Chrome()
driver.get('http://demo.seleniumeasy.com/basic-radiobutton-demo.html')

radio = driver.find_element(By.XPATH,'//input[contains(@value,"Male")]')
radio.click()
wait=WebDriverWait(driver,5)
condition = ec.visibility_of_element_located((By.ID, 'buttoncheck'))
btn_check=wait.until(condition)
btn_check.click()
time.sleep(3)
# radio2 = wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@class="panel-body" and contains(@value, "Male")]')))
radio2 = driver.find_element(By.XPATH, '//input[@type="radio" and @value="Female" and @name="gender"]')
time.sleep(3)

radio3 = driver.find_element(By.XPATH, '//input[@type="radio" and @value="5-15" and @name="ageGroup"]')
radio2.click()
radio3.click()


time.sleep(10)
driver.quit()
