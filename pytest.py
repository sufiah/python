# coding : utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://172.30.0.140:18080/openplatform/")
driver.implicitly_wait(3)
driver.maximize_window()

'''driver.find_element_by_id("kw").send_keys("Selenium")
driver.find_element_by_id("su").click()'''
time.sleep(5)
print driver.title
driver.close()