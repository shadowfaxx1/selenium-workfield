from selenium import webdriver
import os 
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from PIL import Image
import io 
import cv2 as cv



os.environ['PATH']+= r"C:\Users\kaifk\lpth\.vscode"
driver=webdriver.Chrome()
driver.get("https://ceoelection.maharashtra.gov.in/searchlist/")
driver.implicitly_wait(100)
element = driver.find_element(by='xpath', value='//img[@style="WIDTH: 200px; HEIGHT: 34px"]')
screenshot = element.screenshot
image = Image.open(io.BytesIO(screenshot))
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
# resz=cv.resize(gray,[700,400],interpolation=cv.INTER_CUBIC )
gray.save("output.jpg")

cv.imshow('f', gray)
cv.waitKey(0)
# print(element)

# WebDriverWait(driver,30).until(
#     ec.text_to_be_present_in_element(by='id',value='ctl00_Content_txtcaptcha')
#     ,
# )
input("Press Enter to close the browser...")
driver.quit()
