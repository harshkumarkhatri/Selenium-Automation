import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome('/home/harsh/VS-Code/chrome_driver/chromedriver')
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)

driver.find_element_by_xpath("//*[@id='Tabbed']/a").click()
time.sleep(5)

# It closes only closes a single window
# driver.close()

driver.quit()   #it quits all the windows and the browser opened