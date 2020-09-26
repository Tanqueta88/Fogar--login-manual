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
        self.driver = webdriver.Chrome('/home/tanqueta/PycharmProjects/pythonProject/FOGAR-Automation/Fogar_test/Driver/chromedriver', options=option)
        self.driver.set_window_size(1400, 800)
        self.driver.get('https://uat-guaranteefunds.mobeats.com.ar/#/')
        self.driver.implicitly_wait(45)
        self.loginPage = PageLogin(self.driver)
        self.dashPage = PageDash(self.driver)
        self.clientePage = PageCliente(self.driver)
        self.guaranteePage = PageGuarantee(self.driver)


    def test_LG_COOPERATIVAS_CORREGIR_NO_FUNCIONA_BNA(self):
        self.loginPage.search('20173983523', 'admin')
        self.dashPage.search()
        self.clientePage.search('20336888280', 'Préstamo ARS - FAE MiPyMEs')
        self.guaranteePage.search('1000', '50', '500', '1948720', '19-08-2020', '01-12-2020', '16', '19-12-2021', '22')
        self.guaranteePage.select_by_operation(None, 'Fija', 'Americano', 'Al vencimiento', 'Cooperativa')
        time.sleep(5)
        self.guaranteePage.guardar()
        time.sleep(5)
        self.assertEqual(self.guaranteePage.return_no_element_text(),
                         # 'El tipo de operación no se corresponde con el destino de fondos seleccionado.',
                         'El sistema de amortización no se corresponde con el destino de fondos seleccionado.',
                         'El Plazo total (en meses) no puede ser mayor a 15 para el destino de fondos seleccionado.',
                         'La frecuencia de amortización no se corresponde con el destino de fondos seleccionado.',
                         'Por favor, comuníquese con fogar-fae@bicefideicomisos.com.ar para habilitar la empresa.',
                         'La fecha del primer vencimiento y la de vencimiento del préstamo deben ser iguales.')
        time.sleep(5)

    def test_AM_exitosa_BNA(self):
        try:
            self.loginPage.search('20173983523', 'admin')
            self.dashPage.search()
            self.clientePage.search('20336888280', 'Préstamo ARS - FAE MiPyMEs')
            self.guaranteePage.search('1000', '50', '500', '194472', '19-08-2020', '01-12-2020', '12', '19-08-2021', '24')
            self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Al vencimiento', 'Capital de trabajo')
            self.guaranteePage.guardar()
        except:
            self.driver.save_screenshot('no funciona.png')


    def test_AM_VALIDACION_monto_cero_HIPOTECARIO(self):
        try:
            self.loginPage.search('27315508776', 'admin')
            self.dashPage.search()
            self.clientePage.search('20336888280', 'Préstamo ARS - FAE MiPyMEs')
            self.guaranteePage.search('1000', '50', '500', '194472', '28-08-2020', '01-12-2020', '12', '28-08-2021', '24')
            self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Al vencimiento', 'Capital de trabajo')
            self.guaranteePage.guardar()
            self.assertEqual(self.guaranteePage.return_no_element_text(),
                     'El porcentaje de cobertura no puede superar el 100%.')
        except:
            self.driver.save_screenshot('error.png')


    def test_AM_VALIDACION_puntos_porcentuales_rango_HIPOTECARIO(self):
        try:
            self.loginPage.search('27315508776', 'admin')
            self.dashPage.search()
            self.clientePage.search('20336888280', 'Préstamo ARS - FAE MiPyMEs')
            self.guaranteePage.search('1000', '50', '500', '1545', '19-08-2020', '01-12-2020', '12', '19-08-2021', '44')
            self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Al vencimiento', 'Capital de trabajo')
            self.guaranteePage.guardar()
        except:
            self.driver.save_screenshot('no funciona.png')


    def test_AM_VALIDACION_Samericano_incorrecto_HIPOTECARIO(self): # ojo con este caso de prueba
        try:
            self.loginPage.search('27315508776', 'admin')
            self.dashPage.search()
            self.clientePage.search('20336888280', 'Préstamo ARS - FAE MiPyMEs')
            self.guaranteePage.search('1000', '50', '500', '11942', '19-08-2020', '01-12-2020', '12', '19-08-2021', '14')
            self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Americano', 'Trimestral', 'Capital de trabajo')
            self.guaranteePage.guardar()
            self.assertEqual(self.guaranteePage.return_no_element_text(),
                             'La frecuencia de amortización no se corresponde con el sistema seleccionado.')
            time.sleep(7)
        except:
            self.driver.save_screenshot('no funciona.png')




    def test_AM_VALIDACION_nro_op_repetida_HIPOTECARIO(self):
        try:
            self.loginPage.search('27315508776', 'admin')
            self.dashPage.search()
            self.clientePage.search('20336888280', 'Préstamo ARS - FAE MiPyMEs')
            self.guaranteePage.search('1000', '50', '500', '19472', '19-08-2020', '01-12-2020', '12', '19-08-2021', '24')
            self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Al vencimiento', 'Capital de trabajo')
            self.guaranteePage.guardar()
            self.assertEqual(self.guaranteePage.return_no_element_text(), 'El número de operación 19472 ya existe para otra garantía vigente de esta entidad.')
        except:
            self.driver.save_screenshot('no funciona.png')


    def test_AM_VALIDACION_COM7006_con_garantia_en_el_sistema_HIPOTECARIO(self):
        self.loginPage.search('27315508776', 'admin')
        self.dashPage.search()
        self.clientePage.search('20336888280', 'Préstamo ARS - FAE MiPyMEs')
        self.guaranteePage.search('1000', '100', '1000', '4652', '28-08-2020', '01-12-2020', '12', '28-08-2021', '24')
        self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Al vencimiento', 'Com7006')
        self.guaranteePage.guardar()
        self.assertEqual(self.guaranteePage.return_no_element_text(), 'No puede proceder con el alta ya que el cliente ya posee una garantía de FAE MiPyMEs en el sistema.')

    def test_AM_VALIDACION_porcentage_cobertura_NEUQUEN(self):
        self.loginPage.search('20273233572', 'admin')
        self.dashPage.search()
        self.clientePage.search('20336888280', 'Préstamo ARS - FAE MiPyMEs')
        self.guaranteePage.search('1000', '50', '5000', '19442', '28-08-2020', '01-12-2020', '12', '28-08-2021', '24')
        self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Al vencimiento', 'Capital de trabajo')
        time.sleep(4)
        self.guaranteePage.guardar()
        time.sleep(3)
        self.assertEqual(self.guaranteePage.return_no_element_text(),
                         'El porcentaje de cobertura no puede superar el 100%.')
        time.sleep(1)

    def test_AM_VALIDACION_monto_garantizado_maximo_PATAGONIA(self):
        self.loginPage.search('2332830654', 'admin')
        self.dashPage.search()
        self.clientePage.search('27118674443', 'Préstamo ARS - FAE MiPyMEs')
        self.guaranteePage.search('1000100', '50', '500050', '19442', '28-08-2020', '01-12-2020', '12', '28-08-2021', '24')
        self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Al vencimiento', 'Com7006')
        time.sleep(5)
        self.guaranteePage.guardar()
        time.sleep(4)
        self.assertEqual(self.guaranteePage.return_no_element_text(),
                         'El monto garantizado no puede superar los $500.000 para el destino de fondos seleccionado.')
        time.sleep(3)

    def test_CULTURA_BNA(self):
        self.loginPage.search('20173983523', 'admin')
        self.dashPage.search()
        self.clientePage.search('30-71297570-5', 'Préstamo ARS - FAE MiPyMEs')
        self.guaranteePage.search('1000', '50', '500', '19442', '28-08-2020', '01-12-2020', '12', '28-08-2021', '24')
        self.guaranteePage.select_by_operation('Préstamo', 'Fija', 'Alemán', 'Mensual', 'Cultura')
        time.sleep(6)
        self.guaranteePage.guardar()
        time.sleep(21)




    def tearDown(self):
        self.driver.save_screenshot('esto funciona cda.png')
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
