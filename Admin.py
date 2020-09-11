import unittest
from selenium import webdriver
from pagelogin import PageLogin
from pagedash_admin import PageDashAdmin
from page_rm import Page_RMG
import time
from selenium.webdriver.chrome.options import Options


class SearchCases(unittest.TestCase):

    def setUp(self):
        option = Options()
        # option.add_argument("start-maximized")
        # option.add_argument("incognito")
        # option.add_argument("--headless")
        self.driver = webdriver.Chrome('/home/tanqueta/PycharmProjects/pythonProject/chromedriver',
                                       chrome_options=option)
        self.driver.get('http://dev-guaranteefunds.mobeats.com.ar')
        self.driver.implicitly_wait(35)
        self.loginPage = PageLogin(self.driver)
        self.dash_adminPage = PageDashAdmin(self.driver)
        self.rm_page = Page_RMG(self.driver)

    def test_report_admin_Supervielle_FAE_Cf(self):
        self.loginPage.search('mfontenla', 'admin')
        self.dash_adminPage.reports_drop_down_menu()
        self.rm_page.select_rmg('Fogar - FAE MiPyMEs', 'Banco Supervielle S.A.', '03-08-2020', '30-09-2020')
        time.sleep(5)

    def test_report_admin_Supervielle_FAE_sf(self):
        self.loginPage.search('mfontenla', 'admin')
        self.dash_adminPage.reports_drop_down_menu()
        self.rm_page.select_rmg('Fogar - FAE MiPyMEs', 'Banco Supervielle S.A.', null, null)
        time.sleep(5)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
