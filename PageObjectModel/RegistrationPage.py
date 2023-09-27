from selenium.webdriver.common.by import By


class RegistrationPageVerification:

    def __init__(self, driver):
        self.driver = driver

    RegTab = (By.XPATH, "//a[normalize-space()='Register']")
    NameText = (By.XPATH, "//input[@id='name']")
    E_Mail_Address = (By.XPATH, "//input[@id='email']")
    Password = (By.XPATH, "//input[@id='password']")
    Confirm_Password = (By.XPATH, "//input[@id='password-confirm']")
    Register = (By.XPATH, "//button[@type='submit']")
    ErrorM = (By.XPATH, "//strong[normalize-space()='The email has already been taken.']")

    def getRegTab(self):
        return self.driver.find_element(*RegistrationPageVerification.RegTab)

    def getNameText(self):
        return self.driver.find_element(*RegistrationPageVerification.NameText)

    def getE_Mail_Address(self):
        return self.driver.find_element(*RegistrationPageVerification.E_Mail_Address)

    def getPassword(self):
        return self.driver.find_element(*RegistrationPageVerification.Password)

    def getConfirm_Password(self):
        return self.driver.find_element(*RegistrationPageVerification.Confirm_Password)

    def getRegister(self):
        return self.driver.find_element(*RegistrationPageVerification.Register)

    def getErrorM(self):
        return self.driver.find_element(*RegistrationPageVerification.ErrorM)
