from selenium.webdriver.common.by import By


class PageDash:

    def __init__(self, my_driver):
        self.altag = (By.XPATH,
                      "//div[@id='foga']/div[2]/div/div[2]/jhi-dashboard-user/jhi-guarantee/div/div/jhi-button/button"
                      "/span/span")
        self.reports_EFI_menu = (By.XPATH, '//*[@id="main_navbar"]/div/div/div/ul[6]/li/a/span[2]/span')
        self.masive_EFI_G_reports_menu = (By.XPATH, '//*[@id="main_navbar"]/div/div/div/ul[6]/li/ul/div[2]/li/a/span/span')
        self.masive_EFI_N_reports_menu = (By.XPATH, '//*[@id="main_navbar"]/div/div/div/ul[6]/li/ul/div[3]/li/a/span/span')
        self.driver = my_driver

    def search(self):
        self.driver.find_element(*self.altag).click()

    def reports_drop_down_menu_guarentee(self):
        self.driver.find_element(*self.reports_EFI_menu).click()
        self.driver.find_element(*self.masive_EFI_G_reports_menu).click()

    def reports_drop_down_menu_novelties(self):
        self.driver.find_element(*self.reports_EFI_menu).click()
        self.driver.find_element(*self.masive_EFI_N_reports_menu).click()

