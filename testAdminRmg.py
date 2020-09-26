import unittest
from selenium import webdriver
from FOGAR_page_object.pagelogin import PageLogin
from FOGAR_page_object.pagedash_admin import PageDashAdmin
from FOGAR_page_object.pagedash import PageDash
from FOGAR_page_object.page_rmg import PageRmg
import time
from selenium.webdriver.chrome.options import Options


class SearchCases(unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument("start-maximized")
        # option.add_argument("incognito")
        # option.add_argument("--headless")
        self.driver = webdriver.Chrome('/home/tanqueta/PycharmProjects/pythonProject/chromedriver',
                                       options=option)
        # self.driver = webdriver.Chrome('/home/tanqueta/PycharmProjects/pythonProject/chromedriver')
        self.driver.get('https://preprod-guaranteefunds.mobeats.com.ar/')
        self.driver.implicitly_wait(35)
        self.loginPage = PageLogin(self.driver)
        self.dash_adminPage = PageDashAdmin(self.driver)
        self.dashPage = PageDash(self.driver)
        self.rmg_page = PageRmg(self.driver)

    def test_report_admin_Supervielle_FAE_Cf(self):
        try:
            self.loginPage.search('mfontenla', 'admin')
            self.dash_adminPage.reports_drop_down_menu_guarentee()
            self.rmg_page.select_rmg('Fogar - FAE MiPyMEs', 'Banco Supervielle S.A.', '03-08-2020', '30-09-2020')
            self.assertEqual(self.rmg_page.return_no_element_text(),
                             "Se ha iniciado la generación del reporte, se la enviaremos al mail: null en cuanto finalice.")
        except:
            self.driver.save_screenshot('no funciona.png')

    def test_report_admin_Supervielle_FAE_sf(self):
        try:
            self.loginPage.search('mfontenla', 'admin')
            self.dash_adminPage.reports_drop_down_menu_guarentee()
            self.rmg_page.select_rmg('Fogar - FAE MiPyMEs', 'Banco Supervielle S.A.', None, None)
            self.assertEqual(self.rmg_page.return_no_element_text(),
                             'Se ha iniciado la generación del reporte, se la enviaremos al mail: null en cuanto finalice.')
        except:
            self.driver.save_screenshot('no funciona.png')

    def test_report_administrador_Supervielle_FAE_Cf(self):
        try:
            self.loginPage.search('mfontenla', 'admin')
            self.dash_adminPage.reports_drop_down_menu_guarentee()
            self.rmg_page.select_rmg('Fogar - FAE PCA', 'Banco Supervielle S.A.', '03-08-2020', '30-09-2020')
            time.sleep(2)
            self.assertEqual(self.rmg_page.return_no_element_text(),
                             'Se ha iniciado la generación del reporte, se la enviaremos al mail: null en cuanto finalice.')
        except:
            self.driver.save_screenshot('no funciona.png')

    def test_report_administrador_Supervielle_FAE_sf(self):
        try:
            self.loginPage.search('mfontenla', 'admin')
            self.dash_adminPage.reports_drop_down_menu_guarentee()
            self.rmg_page.select_rmg('Fogar - FAE PCA', 'Banco Supervielle S.A.', None, None)
            self.assertEqual(self.rmg_page.return_no_element_text(),
                             'Se ha iniciado la generación del reporte, se la enviaremos al mail: null en cuanto finalice.')
        except:
            self.driver.save_screenshot('no funciona.png')

    def test_report_Efi_Supervielle_FAE_sf(self):
        try:
            self.loginPage.search('24318288506', 'admin')
            self.dashPage.reports_drop_down_menu_guarentee()
            self.rmg_page.select_rmg('Fogar - FAE MiPyMEs', None, None, None)
            self.assertEqual(self.rmg_page.return_no_element_text(),
                             'Se ha iniciado la generación del reporte, se la enviaremos al mail: 24318288506@1 en cuanto finalice.')
        except:
            self.driver.save_screenshot('no funciona.png')

    def test_report_Efi_Supervielle_FAE_cf(self):
        try:
            self.loginPage.search('24318288506', 'admin')
            self.dashPage.reports_drop_down_menu_guarentee()
            self.rmg_page.select_rmg('Fogar - FAE MiPyMEs', None, '01-09-2020', '20-09-2020')
            self.assertEqual(self.rmg_page.return_no_element_text(),
                             'Se ha iniciado la generación del reporte, se la enviaremos al mail: 24318288506@1 en cuanto finalice.')
        except:
            self.driver.find_element('no funciona.png')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
