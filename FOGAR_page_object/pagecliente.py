from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class PageCliente:

    def __init__(self, my_driver):
        self.imput_cuit = (By.NAME, 'cuit')
        self.select_product_SGR = (By.XPATH, '//*[@id="foga"]/div[2]/div/div[2]/jhi-guarantee-update/div/div[2]/div[3]/select')
        #self.select_product = (By.XPATH, '//*[@id="foga"]/div[2]/div/div[2]/jhi-guarantee-update/div/div[2]/div[3]/select')
        self.continuar = (By.XPATH, '//*[@id="save-entity"]/span/span')
        self.driver = my_driver

    def search(self, cuit, producto):
        self.driver.find_element(*self.imput_cuit).send_keys(cuit)
        select_product = Select(self.driver.find_element(*self.select_product_SGR))
        select_product.select_by_visible_text(producto)
        self.driver.find_element(*self.continuar).click()



