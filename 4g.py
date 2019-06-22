from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

class Smile4g():

	def login():
		
		#choice = int(input("Enter Speed(1, 2, 5, 21): "))
		global choice 
		global browser
		choice = 2
		browser = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\chromedriver.exe')
		browser.maximize_window()
		browser.get("http://smile.co.tz/scp")
		username = browser.find_element_by_name("username")
		password = browser.find_element_by_name("password")
		#time.sleep(2)

		#Credentials
		username.send_keys("example@email.com")
		password.send_keys("password")

		login_attempt = browser.find_element_by_xpath('//*[@id="loginform"]/input[4]').click(); time.sleep(2);

	def confirm():
		return browser.find_element_by_xpath('//*[@id="content"]/div[4]/div[2]/div/div[2]/div[2]/div/div/form/div[6]/div/input[6]').click()

	def ChangeSpeed():
		manage = browser.find_element_by_xpath('//*[@id="content"]/div[4]/div[2]/div/div[2]/div[1]/div[2]/table[2]/tbody/tr[2]/td[4]/form/input').click(); time.sleep(0.5);
		if choice == 1:
			return browser.find_element_by_xpath('//*[@id="category_speed1"]').click()
		elif choice == 2:
			return browser.find_element_by_xpath('//*[@id="category_speed2"]').click()
		elif choice == 5:
			return browser.find_element_by_xpath('//*[@id="category_speed5"]').click()
		elif choice == 21:
			return browser.find_element_by_xpath('//*[@id="category_speed21"]').click()
		else:
			return 0
		
	def main():

		login()
		time.sleep(0.5)
		ChangeSpeed()
		time.sleep(0.5)
		confirm()
		browser.close()
		sys.exit()
		
if __name__=='__main__':
	Smile4g.main()

