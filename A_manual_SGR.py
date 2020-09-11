import unittest
from selenium import webdriver
from FOGAR_page_object.pagelogin import PageLogin
from FOGAR_page_object.pagedash import PageDash
from FOGAR_page_object.pagecliente import PageCliente
from FOGAR_page_object.pageguarantee import PageGuarantee
import time
from selenium.webdriver.chrome.options import Options


class SearchCases(unittest.TestCase):

    def setUp(self):
        option = Options()
        #option.add_argument("start-maximized")
        #option.add_argument("incognito")
        #option.add_argument("--headless")
        self.driver = webdriver.Chrome('/home/tanqueta/PycharmProjects/pythonProject/chromedriver',
                                       chrome_options=option)
        self.driver.get('https://preprod-guaranteefunds.mobeats.com.ar')
        self.driver.implicitly_wait(35)
        self.loginPage = PageLogin(self.driver)
        self.dashPage = PageDash(self.driver)
        self.clientePage = PageCliente(self.driver)
        self.guaranteePage = PageGuarantee(self.driver)

    def test_Alta_SGR(self):
        self.loginPage.search('20083898578', 'admin')
        self.dashPage.search()
        self.clientePage.search('20336888280', 'Préstamo ARS SGR ')
        self.guaranteePage.search('1000', '50', '500', '1939', '24.00', 29-7-2020, 30-7-2020, 30-10-2020, 120, 25-2-2021, 24)
        self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Al vencimiento', 'Capital de trabajo')
        time.sleep(4)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()