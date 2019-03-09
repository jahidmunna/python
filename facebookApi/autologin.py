from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://facebook.com")

user_id = 'jim150'
user_pass = '01557009976jimunna'

email_tag = "email"
password_tag = "pass"
login_btn="loginbutton"

emailelement = driver.find_element_by_name(email_tag)
passwordelement = driver.find_element_by_name(password_tag)
emailelement.send_keys(user_id)
passwordelement.send_keys(user_pass)
loginelement = driver.find_element_by_id(login_btn)
loginelement.click()
driver.get("https://www.facebook.com/"+user_id)
post_box=driver.find_element_by_xpath("//*[@name='xhpc_message']")
post_box.click()
post_box.send_keys("Automation using python test0001..")
sleep(2)
post_it=driver.find_element_by_xpath("//*[@id='u_0_1a']/div/div[6]/div/ul/li[2]/button")
post_it.click()
# time.sleep(10)
# logout1 = driver.find_element_by_css_selector("#userNavigationLabel")
# logout1.click()
# time.sleep(10)
# logout2 = driver.find_element_by_css_selector("._w0d[action='https://www.facebook.com/logout.php']").submit()