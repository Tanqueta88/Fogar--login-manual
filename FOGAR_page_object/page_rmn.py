from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class PageRmn:

    def __init__(self, my_driver):
        self.select_start_date_novelties = (By.XPATH, '//*[@id="displayDate"]/div[1]/div/input')
        self.select_end_date_novelties = (By.XPATH,
                                          '/html/body/jhi-main/jhi-layout/div/div[2]/div/div[2]/jhi-report/div/div/div[2]/jhi-input-datepicker/dp-date-picker/div[1]/div/input')
        self.request_report_button = (
            By.XPATH, '//*[@id="foga"]/div[2]/div/div[2]/jhi-report/div/div/div[3]/div/jhi-button/button/span/span')
        self.no_resulta_banner = (By.XPATH, '//*[@id="foga"]/div[2]/div/div[2]/jhi-notification/div[2]/p')
        self.driver = my_driver

    def select_rmn(self, fecha_inicio, fecha_fin):
        if (fecha_inicio != None):
            self.driver.find_element(*self.select_start_date_novelties).send_keys(fecha_inicio)
        if (fecha_fin != None):
            self.driver.find_element(*self.select_end_date_novelties).send_keys(fecha_fin)
        self.driver.find_element(*self.request_report_button).click()

    def return_no_element_text(self):
        return self.driver.find_element(*self.no_resulta_banner).text
