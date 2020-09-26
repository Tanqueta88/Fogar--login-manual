import unittest
from selenium import webdriver
from pagelogin import PageLogin
from selenium.webdriver.chrome.options import Options


class SearchCases(unittest.TestCase):

    def setUp(self):
        option = Options()
        # option.add_argument("--headless")
        self.driver = webdriver.Chrome(
            '/home/tanqueta/PycharmProjects/pythonProject/FOGAR-Automation/Fogar--test/Driver/chromedriver',
            chrome_options=option)

        self.driver.get('https://URL_GLOBANT.com.ar')
        self.driver.implicitly_wait(5)
        self.loginPage = PageLogin(self.driver)

    def test_LogIn_globant(self):
        self.loginPage.search('jolivera@mail.com', '12345, 'Argentina')

        def test_search_no_elements(self):  # los metodos se definen con la palabra reservada DEF
            self.indexPage.search('hola')
            time.sleep(2)
            self.assertEqual(self.itemsPage.return_no_element_text(), "No results were found for your search \"hola\"")

    def tearDown(self):
            self.driver.close()
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class PageLogin:

    def __init__(self, my_driver):
        self.input_MAIL = (By.NAME, 'NAME-MAIL')
        self.input_Password = (By.ID, 'ID-PASSWORD')
        self.Select_country = (By.ID, 'ID-country')
        self.Submit_button = (By.ID, 'ID-button')
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