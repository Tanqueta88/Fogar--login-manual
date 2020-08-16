from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class PageIndex:
	def __init__(self,my_driver):
		'''self.user = (By.id,"username")
		self.contra = (By.id,"password")
		self.boton = (By.xpath,"/html/body/jhi-main/jhi-app-layout/div/div/div/jhi-login/div/form/button/span")'''
		self.user = 'username'
		self.contra = 'password'
		self.boton = '/html/body/jhi-main/jhi-app-layout/div/div/div/jhi-login/div/form/button/span'
		self.order = '//*[@id="foga"]/div[2]/div/div[2]/jhi-guarantee-update/div/div[2]/div[3]/select'
		self.driver = my_driver

	def search(self, item):
		self.driver.find_element_by_id(self.user).send_keys(item)
		self.driver.find_element_by_id(self.contra).send_keys('admin')
		self.driver.find_element_by_xpath(self.boton).click()
		self.driver.find_element_by_xpath(self.order).click()

	def select_by_text(self, text):
		order = Select(self.driver.find_element(self.order))
		order.select_by_visible_text(text)

	'''def search(self, user, password): #correccion de franco
		self.driver.find_element_by_id(self.user).send_keys(user)
		self.driver.find_element_by_id(self.contra).send_keys(password)
		self.driver.find_element_by_xpath(self.boton).click()'''

