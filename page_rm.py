from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Page_RMG:

    def __init__(self, my_driver):
        self.select_founds = (By.NAME, 'fund')
        self.select_finantial_entity =(By.NAME, 'finantialEntityId')
        self.select_start_date = (By.XPATH, '//*[@id="displayDate"]/div[1]/div/input')
        self.select_end_date = (By.XPATH, '/html/body/jhi-main/jhi-layout/div/div[2]/div/div[2]/jhi-report/div/div/div[2]/div[2]/jhi-input-datepicker/dp-date-picker/div[1]/div/input')
        self.request_report_button = (By.XPATH, '//*[@id="foga"]/div[2]/div/div[2]/jhi-report/div/div/div[3]/div/button')
        self.driver = my_driver


    def select_rmg(self, filtro_fondo, filtro_Efi, fecha_inicio, fecha_fin):
        self.select_founds = Select(self.driver.find_element(*self.select_founds))
        self.select_founds.select_by_visible_text(filtro_fondo)
        self.select_finantial_entity = Select(self.driver.find_element(*self.select_finantial_entity))
        self.select_finantial_entity.select_by_visible_text(filtro_Efi)
        self.driver.find_element(*self.select_start_date).send_keys(fecha_inicio)
        self.driver.find_element(*self.select_end_date).send_keys(fecha_fin)
        self.driver.find_element(*self.request_report_button).click()

