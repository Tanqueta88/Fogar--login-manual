from selenium.webdriver.common.by import By


class PageDashAdmin:

    def __init__(self, my_driver):
        self.reports_menu = (By.XPATH, '//*[@id="main_navbar"]/div/div/div/ul[8]/li/a/span[2]/span')
        self.masive_G_reports_menu = (By.XPATH, '//*[@id="main_navbar"]/div/div/div/ul[8]/li/ul/div[2]/li/a/span/span')
        self.masive_N_reports_menu = (By.XPATH, '//*[@id="main_navbar"]/div/div/div/ul[8]/li/ul/div[3]/li/a/span/span')
        self.driver = my_driver

    def reports_drop_down_menu_guarentee(self):
        self.driver.find_element(*self.reports_menu).click()
        self.driver.find_element(*self.masive_G_reports_menu).click()

    def reports_drop_down_menu_novelties(self):
        self.driver.find_element(*self.reports_menu).click()
        self.driver.find_element(*self.masive_N_reports_menu).click()
