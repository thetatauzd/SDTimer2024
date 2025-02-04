from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome()
browser.get('https://chronograph.io/bDZ6FdfU')

time.sleep(2)

div1 = browser.find_element(value='7135425933400')
# b1 = div1.find_element_by_class_name('action')
b1 = div1.find_element(By.CLASS_NAME, 'action')

div2 = browser.find_element(value='7578220432574')
# b2 = div2.find_element_by_class_name('action')
b2 = div2.find_element(By.CLASS_NAME, 'action')

time.sleep(.5)

stationTime = 121
rotationTime = 31

while True:
    b1.click()
    time.sleep(stationTime + 1)
    b1.click()
    time.sleep(.5)
    b2.click()
    time.sleep(rotationTime + 1)
    b2.click()
    time.sleep(.5)