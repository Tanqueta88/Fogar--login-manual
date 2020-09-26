def search(self, item, pc, mon_gar, nro_op, f_acred, f_pv, p_tot, e_date, p_porc):
    if (item != None):
        self.driver.find_element(*self.input_total_loan_amount).send_keys(item)
    if (pc != None):
        self.driver.find_element(*self.input_coverage_percentage).send_keys(pc)
    if (mon_gar != None):
        self.driver.find_element(*self.input_guaranteed_amount).send_keys(mon_gar)
    # self.driver.find_element(*self.input_guarentee).send_keys(garantia)
    if (nro_op != None):
        self.driver.find_element(*self.input_operation_number).send_keys(nro_op)
    if (f_acred != None):
        self.driver.find_element(*self.input_accreditation_date).send_keys(f_acred)
    if (f_pv != None):
        self.driver.find_element(*self.input_first_expiration_date).send_keys(f_pv)
    if (p_tot != None):
        self.driver.find_element(*self.input_total_term).send_keys(p_tot)
    if (e_date != None):
        self.driver.find_element(*self.input_expiration_date).send_keys(e_date)
    if (p_porc != None):
        self.driver.find_element(*self.input_percentage_points).send_keys(p_porc)