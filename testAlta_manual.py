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
        self.driver = webdriver.Chrome('/home/tanqueta/PycharmProjects/pythonProject/FOGAR-Automation/Fogar--test/Driver/chromedriver',
                                       chrome_options=option)
        
        self.driver.get('https://preprod-guaranteefunds.mobeats.com.ar')
        self.driver.implicitly_wait(45)
        self.loginPage = PageLogin(self.driver)
        self.dashPage = PageDash(self.driver)
        self.clientePage = PageCliente(self.driver)
        self.guaranteePage = PageGuarantee(self.driver)


    def test_LG_PREP_BNA(self):
        self.loginPage.search('20173983523', 'admin')
        self.dashPage.search()
        self.clientePage.search('20336888280', 'Préstamo ARS - FAE MiPyMEs')
        self.guaranteePage.search('1000', '50', '500', '1942', '28-08-2020', '01-12-2020', '12', '14-12-2020', '24')
        self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Al vencimiento', 'Cooperativa')
        self.guaranteePage.guardar()
        time.sleep(15)

    def test_LG_PREP_HIPOTECARIO(self):
        self.loginPage.search('27315508776', 'admin')
        self.dashPage.search()
        self.clientePage.search('20336888280', 'Préstamo ARS - FAE MiPyMEs')
        self.guaranteePage.search('1000', '50', '500', '11942', '28-08-2020', '01-12-2020', '12', '14-12-2020', '24')
        self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Al vencimiento', 'Capital de trabajo')
        time.sleep(6)
        self.guaranteePage.guardar()
        time.sleep(8)

    def test_LG_PREP_NEUQUEN(self):
        self.loginPage.search('20273233572', 'admin')
        self.dashPage.search()
        self.clientePage.search('20336888280', 'Préstamo ARS - FAE MiPyMEs')
        self.guaranteePage.search('1000', '50', '500', '19442', '28-08-2020', '01-12-2020', '12', '14-12-2020', '24')
        self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Al vencimiento', 'Capital de trabajo')
        time.sleep(6)
        self.guaranteePage.guardar()
        time.sleep(11)

    def test_LG_PREP_Patagonia(self):
        self.loginPage.search('2332830654', 'admin')
        self.dashPage.search()
        self.clientePage.search('20336888280', 'Préstamo ARS - FAE MiPyMEs')
        self.guaranteePage.search('1000', '50', '500', '19442', '28-08-2020', '01-12-2020', '12', '14-12-2020', '24')
        self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Al vencimiento', 'Capital de trabajo')
        time.sleep(6)
        self.guaranteePage.guardar()
        time.sleep(11)

    def test_LG_PREP_BAPRO(self):
        self.loginPage.search('20253160889', 'admin')
        self.dashPage.search()
        self.clientePage.search('20336888280', 'Préstamo ARS - FAE MiPyMEs')
        self.guaranteePage.search('1000', '50', '500', '19442', '28-08-2020', '01-12-2020', '12', '14-12-2020', '24')
        self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Al vencimiento', 'Capital de trabajo')
        time.sleep(6)
        self.guaranteePage.guardar()
        time.sleep(11)


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
