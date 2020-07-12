from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome('/home/harsh/VS-Code/chrome_driver/chromedriver')
driver.get("http://newtours.demoaut.com/")
print(driver.title)
driver.get("https://harshblog.xyz/")
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)