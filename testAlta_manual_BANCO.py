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
        option.add_argument("start-maximized")
        # option.add_argument("incognito")
        # option.add_argument("--headless")
        self.driver = webdriver.Chrome('/home/tanqueta/PycharmProjects/pythonProject/FOGAR-Automation/Fogar--test/Driver/chromedriver',
                                       chrome_options=option)
        self.driver.set_window_size(1400, 800)
        self.driver.get('http://dev-guaranteefunds.mobeats.com.ar/#/')
        self.driver.implicitly_wait(45)
        self.loginPage = PageLogin(self.driver)
        self.dashPage = PageDash(self.driver)
        self.clientePage = PageCliente(self.driver)
        self.guaranteePage = PageGuarantee(self.driver)

    def test_AM_exitosa_Supervielle(self):
        self.loginPage.search('24318288506', 'admin')
        self.dashPage.search()
        self.clientePage.search('20336888280', 'Préstamo ARS Banco')
        self.guaranteePage.search('1000', None, '500', '456', '29-08-2020', '01-12-2020', '12', '29-08-2021', '24')
        self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Al vencimiento', 'Capital de trabajo')
        time.sleep(5)
        self.guaranteePage.guardar()
        time.sleep(2)

    def test_AM_VALIDACION_acreditacion_Supervielle(self):
        self.loginPage.search('24318288506', 'admin')
        self.dashPage.search()
        self.clientePage.search('20336888280', 'Préstamo ARS Banco')
        self.guaranteePage.search('1000', None, '500', '456', '09-08-2020', '01-12-2020', '12', '09-08-2021', '24')
        self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Al vencimiento', 'Capital de trabajo')
        time.sleep(18)
        self.guaranteePage.guardar()
        time.sleep(16)
        self.assertEqual(self.guaranteePage.return_no_element_text(),
                         'La fecha de acreditación no se encuentra dentro de los 30 días anteriores al día de la fecha.')
        time.sleep(16)

    def test_AM_VALIDACION_porcentage_de_cobertura_Supervielle(self):
        self.loginPage.search('27255583293', 'admin')
        self.dashPage.search()
        self.clientePage.search('20336888280', 'Préstamo ARS Banco')
        self.guaranteePage.search('0', None, '500', '456', '20-08-2020', '01-12-2020', '12', '20-08-2021', '24')
        self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Al vencimiento', 'Capital de trabajo')
        time.sleep(15)
        self.guaranteePage.guardar()
        time.sleep(15)
        self.assertEqual(self.guaranteePage.return_no_element_text(),
                         'El porcentaje de cobertura no puede superar el 75%.')
        time.sleep(1)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()