from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("/home/harsh/VS-Code/chrome_driver/chromedriver")
driver.get("http://newtours.demoaut.com/")
driver.implicitly_wait(10)
# assert "Welcome: Mercury Tours" is driver.title
driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("login").click()