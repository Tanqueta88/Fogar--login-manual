from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class PageGuaranteeSgr:

    def __init__(self, my_driver):
        self.input_total_loan_amount = (By.NAME, 'Monto total préstamo')
        self.input_coverage_percentage = (By.NAME, 'Porcentaje de cobertura')
        self.input_guaranteed_amount = (By.NAME, 'Monto máximo refianzado')
        self.select_type_of_operation = (By.NAME, 'Tipo de Operación')
        self.input_guarantee_number_SGR = (By.NAME, 'Número de la Garantía de la SGR')
        self.input_commission_earned = (By.NAME, 'Comisión devengada')
        self.input_date_of_instrumentation = (By.XPATH, '//*[@id="displayDate"]/div[1]/div/input')
        self.input_date_of_monetization = (By.XPATH, '/html/body/jhi-main/jhi-layout/div/div[2]/div/div[2]/jhi-guarantee-update/div/form/jhi-custom-input[8]/jhi-input-datepicker/dp-date-picker/div[1]/div/input')
        self.input_first_expiration_date = (By.XPATH, '/html/body/jhi-main/jhi-layout/div/div[2]/div/div[2]/jhi-guarantee-update/div/form/jhi-custom-input[9]/jhi-input-datepicker/dp-date-picker/div[1]/div/input')
        self.input_total_term = (By.NAME, 'Plazo total (en días)')
        self.input_expiration_date = (By.XPATH, '/html/body/jhi-main/jhi-layout/div/div[2]/div/div[2]/jhi-guarantee-update/div/form/jhi-custom-input[11]/jhi-input-datepicker/dp-date-picker/div[1]/div/input' )
        self.select_interest_rate_type = (By.NAME, 'Tipo tasa de interés')
        self.input_percentage_points = (By.NAME, 'Puntos porcentuales')
        self.select_amortization_system = (By.XPATH,
                                          '//*[@id="f2]/div/div[2]/jhi-guarantee-update/div/form/jhi-custom-input[12]/jhi-select/select')
        self.select_periodicity = (By.NAME, 'Periodicidad')
        self.select_destination_of_founds = (By.NAME, 'Destino de los fondos')
        self.save_button = (By.ID, 'save-entity')
        self.driver = my_driver

    def search(self, item, pc, mon_gar, nro_op, com_dev, f_ins, f_mon, f_pv, p_tot, e_date, p_por):
        self.driver.find_element(*self.input_total_loan_amount).send_keys(item)
        self.driver.find_element(*self.input_coverage_percentage).send_keys(pc)
        self.driver.find_element(*self.input_guaranteed_amount).send_keys(mon_gar)
        self.driver.find_element(*self.input_guarantee_number_SGR).send_keys(nro_op)
        self.driver.find_element(*self.input_commission_earned).send_keys(com_dev)
        self.driver.find_element(*self.input_date_of_instrumentation).send_keys(f_ins)
        self.driver.find_element(*self.input_date_of_monetization).send_keys(f_mon)
        self.driver.find_element(*self.input_first_expiration_date).send_keys(f_pv)
        self.driver.find_element(*self.input_total_term).send_keys(p_tot)
        self.driver.find_element(*self.input_expiration_date).send_keys(e_date)
        self.driver.find_element(*self.input_percentage_points).send_keys(p_por)


    def select_by_operation(self, t_operation, i_rate, a_system, a_frecuency, d_founds):
        self.select_type_of_operation = Select(self.driver.find_element(*self.select_type_of_operation))
        self.select_type_of_operation.select_by_visible_text(t_operation)
        self.select_interest_rate_type = Select(self.driver.find_element(*self.select_interest_rate_type))
        self.select_interest_rate_type.select_by_visible_text(i_rate)
        self.select_amortization_system = Select(self.driver.find_element(*self.select_amortization_system))
        self.select_amortization_system.select_by_visible_text(a_system)
        self.select_periodicity = Select(self.driver.find_element(*self.select_periodicity))
        self.select_periodicity.select_by_visible_text(a_frecuency)
        self.select_destination_of_founds = Select(self.driver.find_element(*self.select_destination_of_founds))
        self.select_destination_of_founds.select_by_visible_text(d_founds)
#
    def guardar(self):
        self.driver.find_element(*self.save_button).click()