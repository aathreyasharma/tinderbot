from selenium import webdriver
from time import sleep
from creds import email,password

class Tinder():
	def __init__(self):
		self.driver = webdriver.Chrome()

	def login(self):
		self.driver.get('https://tinder.com')
		sleep(5)
		fbAuthBtn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
		fbAuthBtn.click()
		
		# Since login using fb button opens a new window, we have two windows now
		# Note: window_handles is an array object with all the open windows
		# Tinder webpage will be our primary window i.e, window_handles[0]
		# Any other window will be our secondary window i.e, window_handles[n]
		# Now go to login pop-up window
	
		primaryWindow = self.driver.window_handles[0]
		self.driver.switch_to_window(self.driver.window_handles[1])

		emailInput = self.driver.find_element_by_xpath('//*[@id="email"]')
		emailInput.send_keys(email)

		passwordInput = self.driver.find_element_by_xpath('//*[@id="pass"]')
		passwordInput.send_keys(password)

		fbLoginBtn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
		fbLoginBtn.click()

		# Now go back to main window
		self.driver.switch_to_window(primaryWindow)

		# Allow location access
		sleep(3)
		locationAccessBtn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
		locationAccessBtn.click()
		
		sleep(3)
		notificationBtn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
		notificationBtn.click()
		
	def like(self):
		likeBtn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
		likeBtn.click()

	def dislike(self):
		dislikeBtn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
		dislikeBtn.click()


	def autoSwipe(self):
		while True:
			self.like()
			sleep(1)

	def closePopUps(self):
		pass


autobot = Tinder()
sleep(3)
autobot.login()
sleep(3)
autobot.autoSwipe()
