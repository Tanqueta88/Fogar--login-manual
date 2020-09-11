from selenium.webdriver.common.by import By


class PageLogin:

    def __init__(self, my_driver):
        self.user = (By.ID, 'username')
        self.contra = (By.ID, 'password')
        self.boton = (By.XPATH, '/html/body/jhi-main/jhi-app-layout/div/div/div/jhi-login/div/form/button')
        self.driver = my_driver

    def search(self, id, pasword):
        self.driver.find_element(*self.user).send_keys(id)
        self.driver.find_element(*self.contra).send_keys(pasword)
        self.driver.find_element(*self.boton).click()
