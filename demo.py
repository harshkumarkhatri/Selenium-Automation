import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/home/harsh/VS-Code/chrome_driver/chromedriver')  # This is the executable path showing there the driver is located
driver.get('http://www.google.com/');     # For opening up a url in the webrowser
print(driver.title)   # Gives us the title of the page

print(driver.current_url)   # Currenting the current url for the page

print(driver.page_source)   # It return the html code for the page

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')

search_box.send_keys('Jai hind dosto')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.close()  # Clsing the web browser