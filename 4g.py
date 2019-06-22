from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#user speed choice
choice = int(input("Enter Speed(1, 2, 5, 21): "))
browser = webdriver.Chrome('path to chrome web driver')
browser.minimize_window()
browser.get("http://smile.co.tz/scp")

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")
#time.sleep(2)

#Credentials
username.send_keys("youremail")
password.send_keys("yourpassword!")

login_attempt = browser.find_element_by_xpath('//*[@id="loginform"]/input[4]').click()
#time.sleep(1)
manage = browser.find_element_by_xpath('//*[@id="content"]/div[4]/div[2]/div/div[2]/div[1]/div[2]/table[2]/tbody/tr[2]/td[4]/form/input').click()
#changing the speed then closing out
#time.sleep(2)
if choice == 21:
    upspeed = browser.find_element_by_xpath('//*[@id="category_speed21"]').click()
    time.sleep(1)
    confirm = browser.find_element_by_xpath('//*[@id="content"]/div[4]/div[2]/div/div[2]/div[2]/div/div/form/div[6]/div/input[6]').click()
    #time.sleep(4)
    print("Success")
    browser.close()
elif choice == 2:
    upspeed = browser.find_element_by_xpath('//*[@id="category_speed2"]').click()
    time.sleep(1)
    confirm = browser.find_element_by_xpath('//*[@id="content"]/div[4]/div[2]/div/div[2]/div[2]/div/div/form/div[6]/div/input[6]').click()
    #time.sleep(4)
    print("Success")
    browser.close()
elif choice == 5:
    upspeed = browser.find_element_by_xpath('//*[@id="category_speed5"]').click()
    time.sleep(1)
    confirm = browser.find_element_by_xpath('//*[@id="content"]/div[4]/div[2]/div/div[2]/div[2]/div/div/form/div[6]/div/input[6]').click()
    #time.sleep(4)
    print("Success")
    browser.close()
elif choice == 1:
    upspeed = browser.find_element_by_xpath('//*[@id="category_speed1"]').click()
    time.sleep(1)
    confirm = browser.find_element_by_xpath('//*[@id="content"]/div[4]/div[2]/div/div[2]/div[2]/div/div/form/div[6]/div/input[6]').click()
    #time.sleep(4)
    print("Success")
    browser.close()
else:
    import sys
    sys.exit()
exit()
    
