from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("/home/harsh/VS-Code/chrome_driver/chromedriver")
driver.get("http://newtours.demoaut.com/")
ele=driver.find_element_by_name("userName")
print(ele.is_displayed())   #It returns true or false based on elements state
print(ele.is_enabled())   # It returns true or false on basis os element enable

pas=driver.find_element_by_name('password')
ele.send_keys("mercury")
pas.send_keys('mercury')
but=driver.find_element_by_name('login')
but.click()
round_trip_radio=driver.find_element_by_css_selector("input[value=roundtrip]")
one_way_trip_radio=driver.find_element_by_css_selector("input[value=oneway]")

print(round_trip_radio.is_selected())
print(one_way_trip_radio.is_selected())