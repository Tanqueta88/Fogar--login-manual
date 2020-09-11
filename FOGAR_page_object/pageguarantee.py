from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class PageGuarantee:

    def __init__(self, my_driver):
        self.input_total_loan_amount = (By.NAME, 'Monto total préstamo')
        self.input_coverage_percentage = (By.NAME, 'Porcentaje de cobertura')
        self.input_guaranteed_amount = (By.NAME, 'Monto total garantizado')
        self.input_type_of_operation = (By.NAME, 'Tipo de Operación')
        self.input_operation_number = (By.NAME, 'Número de operación')
        self.input_accreditation_date = (By.XPATH, '//*[@id="displayDate"]/div[1]/div/input')
        self.input_first_expiration_date = (By.XPATH,
                                            '/html/body/jhi-main/jhi-layout/div/div[2]/div/div[2]/jhi-guarantee-update/div/form/jhi-custom-input[7]/jhi-input-datepicker/dp-date-picker/div[1]/div/input')
        self.input_total_term = (By.NAME, 'Plazo total (en mes)')
        self.input_expiration_date = (By.XPATH, '/html/body/jhi-main/jhi-layout/div/div[2]/div/div[2]/jhi-guarantee-update/div/form/jhi-custom-input[9]/jhi-input-datepicker/dp-date-picker/div[1]/div/input' )

        self.input_interest_rate_type = (By.NAME, 'Tipo tasa de interés')
        self.input_percentage_points = (By.NAME, 'Puntos porcentuales')
        self.input_amortization_system = (By.XPATH,
                                          '//*[@id="foga"]/div[2]/div/div[2]/jhi-guarantee-update/div/form/jhi-custom-input[12]/jhi-select/select')
        self.select_amortization_frequency = (By.NAME, 'Frecuencia de amortización del capital')
        self.select_destination_of_founds = (By.NAME, 'Destino de los fondos')
        self.save_button = (By.ID, 'save-entity')
        self.driver = my_driver

    def search(self, item, pc, mon_gar, nro_op, f_acred, f_pv, p_tot, e_date, p_porc):
        self.driver.find_element(*self.input_total_loan_amount).send_keys(item)
        self.driver.find_element(*self.input_coverage_percentage).send_keys(pc)
        self.driver.find_element(*self.input_guaranteed_amount).send_keys(mon_gar)
        self.driver.find_element(*self.input_operation_number).send_keys(nro_op)
        self.driver.find_element(*self.input_accreditation_date).send_keys(f_acred)
        self.driver.find_element(*self.input_first_expiration_date).send_keys(f_pv)
        self.driver.find_element(*self.input_total_term).send_keys(p_tot)
        self.driver.find_element(*self.input_expiration_date).send_keys(e_date)
        self.driver.find_element(*self.input_percentage_points).send_keys(p_porc)


    def select_by_operation(self, t_operation, i_rate, a_system, a_frecuency, d_founds):
        self.input_type_of_operation = Select(self.driver.find_element(*self.input_type_of_operation))
        self.input_type_of_operation.select_by_visible_text(t_operation)
        self.input_interest_rate_type = Select(self.driver.find_element(*self.input_interest_rate_type))
        self.input_interest_rate_type.select_by_visible_text(i_rate)
        self.input_amortization_system = Select(self.driver.find_element(*self.input_amortization_system))
        self.input_amortization_system.select_by_visible_text(a_system)
        self.select_amortization_frequency = Select(self.driver.find_element(*self.select_amortization_frequency))
        self.select_amortization_frequency.select_by_visible_text(a_frecuency)
        self.select_destination_of_founds = Select(self.driver.find_element(*self.select_destination_of_founds))
        self.select_destination_of_founds.select_by_visible_text(d_founds)

    def guardar(self):
        self.driver.find_element(*self.save_button).click()