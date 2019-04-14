from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time


class DriverClass:
	def __init__(self):
		self.driver = webdriver.Chrome()

	def _get_owl(self, site = "https://www.twitch.tv/overwatchleague"):	
		self.driver.get(site)
	
	def _login(self, username, password):
		login_button = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/nav/div/div[4]/div/div[1]/div[1]/button')
		login_button.click()
		time.sleep(2)
		username_textarea = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div/div/form/div/div[1]/div/div[2]/input')
		password_textarea  = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div/div[1]/div[2]/div[1]/input')
		time.sleep(2)
		username_textarea.send_keys(username)
		password_textarea.send_keys(password + Keys.ENTER)
	 
