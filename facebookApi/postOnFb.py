from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
 
driver = webdriver.Chrome()

driver.get('https://www.facebook.com/')

user_id = 'jim150'
user_pass = '01557009976jimunna'


print ("Opened facebook...")
a = driver.find_element_by_id('email')
a.send_keys(user_id)
print("Email Id entered") 
b = driver.find_element_by_id('pass')
b.send_keys(user_pass)
c = driver.find_element_by_id('loginbutton')
c.click()
driver.get("https://www.facebook.com/apoorvu")
post_box=driver.find_element_by_xpath("//*[@name='xhpc_message']")
post_box.click()
post_box.send_keys("Automation using python test0001..")
sleep(2)
post_it=driver.find_element_by_xpath("//*[@id='u_0_1a']/div/div[6]/div/ul/li[2]/button")
post_it.click()