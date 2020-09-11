from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class PageLogin:

    def __init__(self, my_driver):
        self. input_MAIL = (By.NAME, 'NAME-MAIL')
        self. input_Password = (By.ID, 'ID-PASSWORD')
        self. Select_country = (By. ID, 'ID-country')
        self. Submit_button = (By. ID, 'ID-button')
        self.result_banner
        self.driver = my_driver

    def search(self, direccion_mail, contraseña, pais):
        self.driver.find_element(*self.input_MAIL).send_keys(direccion_mail)
        self.driver.find_element(*self.input_Password).send_keys(contraseña)
        self.Select_country = Select(self.driver.find_element(*self.Select_country))
        self.Select_country.select_by_visible_text(pais)
        self.driver.find_element(*self.Submit_button).click()

    def return_no_element_text(self):
        return self.driver.find_element_by_xpath(self.results_banner).text