import unittest
from selenium import webdriver
from FOGAR_page_object.pagelogin import PageLogin
from FOGAR_page_object.pagedash_admin import PageDashAdmin
from FOGAR_page_object.pagedash import PageDash
from FOGAR_page_object.page_rmn import PageRmn
import time
from selenium.webdriver.chrome.options import Options


class SearchCases(unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument("start-maximized")
        # option.add_argument("incognito")
        option.add_argument("--headless")
        self.driver = webdriver.Chrome('/home/tanqueta/PycharmProjects/pythonProject/chromedriver', options=option)
        #self.driver = webdriver.Chrome('/home/tanqueta/PycharmProjects/pythonProject/chromedriver')
        self.driver.get('http://dev-guaranteefunds.mobeats.com.ar/')
        self.driver.implicitly_wait(35)
        #self.driver.maximize_window()
        self.loginPage = PageLogin(self.driver)
        self.dash_adminPage = PageDashAdmin(self.driver)
        self.dashPage = PageDash(self.driver)
        self.rmn_page = PageRmn(self.driver)

    def test_report_admin_novelties_SF(self):
        try:
            self.loginPage.search('mfontenla', 'admin')
            self.dash_adminPage.reports_drop_down_menu_novelties()
            self.rmn_page.select_rmn(None, None)
            self.assertEqual(self.rmn_page.return_no_element_text(),
                             'Se ha iniciado la generación del reporte, se la enviaremos al mail: null en cuanto finalice.')
        except:
            self.driver.save_screenshot('no me funciona la pipeta.png')

    def test_report_admin_novelties_CF(self):
        try:
            self.loginPage.search('mfontenla', 'admin')
            self.dash_adminPage.reports_drop_down_menu_novelties()
            self.rmn_page.select_rmn('01-06-2020', '19-09-2020')
            self.assertEqual(self.rmn_page.return_no_element_text(),
                             'Se ha iniciado la generación del reporte, se la enviaremos al mail: null en cuanto finalice.')
        except:
            self.driver.save_screenshot('no me funciona la pipeta.png')

    def test_report_Efi_Supervielle_FAE_sf(self):
        try:
            self.loginPage.search('24318288506', 'admin')
            self.dashPage.reports_drop_down_menu_novelties()
            self.rmn_page.select_rmn(None, None)
            self.assertEqual(self.rmn_page.return_no_element_text(),
                             'Se ha iniciado la generación del reporte, se la enviaremos al mail: 24318288506@1 en cuanto finalice.')
        except:
            self.driver.save_screenshot('no me funciona la pipeta.png')

    def test_report_Efi_Supervielle_FAE_cf(self):
        try:
            self.loginPage.search('24318288506', 'admin')
            self.dashPage.reports_drop_down_menu_novelties()
            self.rmn_page.select_rmn('01-09-2020', '20-09-2020')
            self.assertEqual(self.rmn_page.return_no_element_text(),
                         'Se ha iniciado la generación del reporte, se la enviaremos al mail: 24318288506@1 en cuanto finalice.')
        except:
            self.driver.save_screenshot('no me funciona la pipeta.png')

    def tearDown(self):
        # self.driver.save_screenshot('esto funciona paaa.jpg')
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
