from selenium.webdriver.common.by import By


class PageDash:

    def __init__(self, my_driver):
        self.altag = (By.XPATH,
                      "//div[@id='foga']/div[2]/div/div[2]/jhi-dashboard-user/jhi-guarantee/div/div/jhi-button/button"
                      "/span/span")
        self.driver = my_driver

    def search(self):
        self.driver.find_element(*self.altag).click()
