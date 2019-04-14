from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time


class DriverClass:
	def __init__(self):
		self.driver = webdriver.Chrome()

	def get_owl(self, site = "https://www.twitch.tv/overwatchleague"):	
		selfdriver.get(site)

