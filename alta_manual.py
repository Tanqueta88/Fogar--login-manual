import unittest
from selenium import webdriver
from pageindex import PageIndex
from pageItems import PageItems
import time



class SearchCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/home/daniel/workspaces/fogar-testing/Automation - Clases/chromedriver')
        self.driver.get('https://preprod-guaranteefunds.mobeats.com.ar/#/')
        self.driver.implicitly_wait(5)
        self.indexPage = PageIndex(self.driver)  # crea el objeto del tipo PageItems= indexPage

    def test_LG_PREP(self):
        self.indexPage.search('20263000006')
        time.sleep(4)
        self.driver.find_element_by_xpath('//*[@id="foga"]/div[2]/div/div[2]/jhi-dashboard-user/jhi-guarantee/div/div[1]/jhi-button/button/span/span').click()
        self.driver.find_element_by_id('field_cuit').send_keys('20336888280')
        time.sleep(2)
        #self.indexPage.select_by_text('Préstamo ARS - FAE MiPyMEs')
        #time.sleep(3)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()