import unittest
from selenium import webdriver
from Fogar_test.FOGAR_page_object.pagelogin import PageLogin
from Fogar_test.FOGAR_page_object.pagedash import PageDash
from Fogar_test.FOGAR_page_object.pagecliente import PageCliente
from Fogar_test.FOGAR_page_object.pageguarantee import PageGuarantee
import time
from selenium.webdriver.chrome.options import Options


class SearchCases(unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument("start-maximized")
        # option.add_argument("incognito")
        # option.add_argument("--headless")
        self.driver = webdriver.Chrome('/home/tanqueta/PycharmProjects/pythonProject/FOGAR-Automation/Fogar--test/Driver/chromedriver', options=option)
        # self.driver.set_window_size(1400, 800)
        self.driver.get('https://uat-guaranteefunds.mobeats.com.ar/#/')
        self.driver.implicitly_wait(45)
        self.loginPage = PageLogin(self.driver)
        self.dashPage = PageDash(self.driver)
        self.clientePage = PageCliente(self.driver)
        self.guaranteePage = PageGuarantee(self.driver)


    def test_5CULTURA_BNA_pporcent(self):
        self.loginPage.search('20173983523', 'admin')
        self.dashPage.search()
        self.clientePage.search('30-71297570-5', 'Préstamo ARS - FAE MiPyMEs')
        self.guaranteePage.search('1000', '50', '500', '19442', None, None, '24', None, '28')
        self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Mensual', 'Cultura')
        time.sleep(6)
        self.guaranteePage.guardar()
        time.sleep(8)
        self.assertEqual(self.guaranteePage.return_no_element_text(),
                         'Los puntos porcentuales no pueden ser distintos de 24 para el destino de fondos seleccionado.')
        time.sleep(3)



    def test_CULTURA_BNA_toperacion(self): # revisar no funciona el test
        self.loginPage.search('20173983523', 'admin')
        self.dashPage.search()
        self.clientePage.search('30-71297570-5', 'Préstamo ARS - FAE MiPyMEs')
        self.guaranteePage.search('1000', '50', '500', '19442', None, None, '12', None, '24')
        self.guaranteePage.select_by_operation('Refinanciación', 'Fija', 'Alemán', 'Mensual', 'Cultura')
        time.sleep(6)
        self.guaranteePage.guardar()
        time.sleep(8)
        self.assertEqual(self.guaranteePage.return_no_element_text(),
                         'El Plazo total (en meses) no puede ser distinto de 24 para el destino de fondos seleccionado.')
        time.sleep(3)

    def test_7CULTURA_BNA_samort(self):
        self.loginPage.search('20173983523', 'admin')
        self.dashPage.search()
        self.clientePage.search('30-71297570-5', 'Préstamo ARS - FAE MiPyMEs')
        self.guaranteePage.search('1000', '50', '500', '19442', '28-08-2020', '01-12-2020', '12', '28-08-2021', '24')
        self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Francés', 'Mensual', 'Cultura')
        time.sleep(6)
        self.guaranteePage.guardar()
        time.sleep(8)
        self.assertEqual(self.guaranteePage.return_no_element_text(),
                         'El sistema de amortización no se corresponde con el destino de fondos seleccionado.')
        time.sleep(3)

    def test_8CULTURA_BNA_ptotal(self):
        self.loginPage.search('20173983523', 'admin')
        self.dashPage.search()
        self.clientePage.search('30-71297570-5', 'Préstamo ARS - FAE MiPyMEs')
        self.guaranteePage.search('1000', '50', '500', '19442', '28-08-2020', '01-12-2020', '12', '28-08-2021', '24')
        self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Mensual', 'Cultura')
        time.sleep(6)
        self.guaranteePage.guardar()
        time.sleep(8)
        self.assertEqual(self.guaranteePage.return_no_element_text(),
                         'El Plazo total (en meses) no puede ser distinto de 24 para el destino de fondos seleccionado.')
        time.sleep(3)

    def test_9CULTURA_BNA_ptotal(self):
        self.loginPage.search('20173983523', 'admin')
        self.dashPage.search()
        self.clientePage.search('30-71297570-5', 'Préstamo ARS - FAE MiPyMEs')
        self.guaranteePage.search('1000', '50', '500', '19442', None, None, '24', None, '24')
        self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Al vencimiento', 'Cultura')
        time.sleep(6)
        self.guaranteePage.guardar()
        time.sleep(8)
        self.assertEqual(self.guaranteePage.return_no_element_text(),
                         'La frecuencia de amortización no se corresponde con el destino de fondos seleccionado.')
        time.sleep(3)

    def test_10CULTURA_BNA_cuitEMPRESA(self):
        self.loginPage.search('20173983523', 'admin')
        self.dashPage.search()
        self.clientePage.search('20336888280', 'Préstamo ARS - FAE MiPyMEs')
        self.guaranteePage.search('1000', '50', '500', '19442', None, None, '24', None, '24')
        self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Mensual', 'Cultura')
        time.sleep(6)
        self.guaranteePage.guardar()
        time.sleep(8)
        self.assertEqual(self.guaranteePage.return_no_element_text(),
                         'El CUIT beneficiario debe ser una empresa para el destino de fondos seleccionado.')
        time.sleep(3)

    def test_12CULTURA_BNA_mtotalgarantizado(self):
        self.loginPage.search('20173983523', 'admin')
        self.dashPage.search()
        self.clientePage.search('30-71297570-5', 'Préstamo ARS - FAE MiPyMEs')
        self.guaranteePage.search('7500000', '100', '7500000', '19442', None, None, '24', None, '24')
        self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Mensual', 'Cultura')
        time.sleep(6)
        self.guaranteePage.guardar()
        time.sleep(8)
        self.assertEqual(self.guaranteePage.return_no_element_text(),
                         'El monto garantizado no puede superar los $7000000 para el destino de fondos seleccionado.')
        time.sleep(3)

    def test_12CULTURA_BNA_incompleta(self):
        self.loginPage.search('20173983523', 'admin')
        self.dashPage.search()
        self.clientePage.search('30-71297570-5', 'Préstamo ARS - FAE MiPyMEs')
        self.guaranteePage.search('7500', '100', '7500', None, None, None, None, None, '24')
        self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Mensual', 'Cultura')
        time.sleep(6)
        self.guaranteePage.guardar()
        time.sleep(18)

    def tearDown(self):
            self.driver.save_screenshot('esto funciona cda.png')
            self.driver.close()
            self.driver.quit()

if __name__ == '__main__':
        unittest.main()

