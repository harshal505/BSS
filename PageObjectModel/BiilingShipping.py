from selenium.webdriver.common.by import By


class BillingShipping:

    def __init__(self, driver):
        self.driver = driver

    E_Mail_Address = (By.XPATH, "//input[@id='email']")
    Password = (By.XPATH, "//input[@id='password']")
    Login_btn = (By.XPATH, "//button[@type='submit']")
    First_Name = (By.XPATH, "//input[@id='first_name']")
    Last_Name = (By.XPATH, "//input[@id='last_name']")
    Phone = (By.XPATH, "//input[@id='phone']")
    Address = (By.XPATH, "//textarea[@id='address']")
    Zip_Code = (By.XPATH, "//input[@id='zip']")
    State_drp = (By.XPATH, "//select[@id='state']")

    def getE_Mail_Address(self):
        return self.driver.find_element(*BillingShipping.E_Mail_Address)

    def getPassword(self):
        return self.driver.find_element(*BillingShipping.Password)

    def getLogin_btn(self):
        return self.driver.find_element(*BillingShipping.Login_btn).click()

    def getFirst_Name(self):
        return self.driver.find_element(*BillingShipping.First_Name)

    def getLast_Name(self):
        return self.driver.find_element(*BillingShipping.Last_Name)

    def getPhone(self):
        return self.driver.find_element(*BillingShipping.Phone)

    def getAddress(self):
        return self.driver.find_element(*BillingShipping.Address)

    def getZip_Code(self):
        return self.driver.find_element(*BillingShipping.Zip_Code)

    def getState_drp(self):
        return self.driver.find_element(*BillingShipping.State_drp)
