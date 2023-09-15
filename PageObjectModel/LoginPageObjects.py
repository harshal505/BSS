from selenium.webdriver.common.by import By


class LoginPageVerification:

    def __init__(self, driver):
        self.driver = driver

    LoginTab = (By.XPATH, "//a[normalize-space()='Login']")
    EmailText = (By.XPATH, "//input[@id='email']")
    PassWordText = (By.XPATH, "//input[@id='password']")
    LoginButton = (By.XPATH, "//button[normalize-space()='Login']")
    Expected_r = (By.XPATH, "//a[normalize-space()='harshal']")

    def getLoginTab(self):
        return self.driver.find_element(*LoginPageVerification.LoginTab)

    def getEmailText(self):
        self.driver.find_element(*LoginPageVerification.EmailText).clear()
        return self.driver.find_element(*LoginPageVerification.EmailText)

    def getPassText(self):
        self.driver.find_element(*LoginPageVerification.PassWordText).clear()
        return self.driver.find_element(*LoginPageVerification.PassWordText)

    def getLoginBut(self):
        return self.driver.find_element(*LoginPageVerification.LoginButton)

    def getExpected_Result(self):
        return self.driver.find_element(*LoginPageVerification.Expected_r)
