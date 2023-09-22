from selenium.webdriver.common.by import By


class End_toEndVerification:
    def __init__(self, driver):
        self.driver = driver

    LoginTab = (By.XPATH, "//a[normalize-space()='Login']")
    EmailText = (By.XPATH, "//input[@id='email']")
    PassWordText = (By.XPATH, "//input[@id='password']")
    LoginButton = (By.XPATH, "//button[normalize-space()='Login']")
    Select_pro = (By.XPATH, "//div[@class='caption text-center']/descendant::a[1]")
    Add_itoCart = (By.XPATH, "//input[@value='Add to Cart']")
    Checkout = (By.XPATH, "(//div[@class='container'])[2]/descendant::a[5]")
    First_Name = (By.XPATH, "//input[@id='first_name']")
    Last_Name = (By.XPATH, "//input[@id='last_name']")
    Phone = (By.XPATH, "//input[@id='phone']")
    Address = (By.XPATH, "//textarea[@id='address']")
    Zip_Code = (By.XPATH, "//input[@id='zip']")
    State = (By.XPATH, "//select[@id='state']")
    Expiration_Date_Year = (By.XPATH, "//select[@id='exp_year']")
    Expiration_Date_Mon = (By.XPATH, "//select[@id='exp_month']")
    Owner = (By.XPATH, "//input[@id='owner']")
    CVV = (By.XPATH, "//input[@id='cvv']")
    Card_Number = (By.XPATH, "//input[@id='cardNumber']")
    checkout_btn = (By.XPATH, "//button[@id='confirm-purchase']")

    def getLoginTab(self):
        return self.driver.find_element(*End_toEndVerification.LoginTab)

    def getEmailText(self):
        return self.driver.find_element(*End_toEndVerification.EmailText)

    def getPassText(self):
        return self.driver.find_element(*End_toEndVerification.PassWordText)

    def getLoginBut(self):
        return self.driver.find_element(*End_toEndVerification.LoginButton)

    def getProduct(self):
        return self.driver.find_element(*End_toEndVerification.Select_pro)

    def getCart(self):
        return self.driver.find_element(*End_toEndVerification.Add_itoCart)

    def getCheckout(self):
        return self.driver.find_element(*End_toEndVerification.Checkout)

    def getFirst_Name(self):
        return self.driver.find_element(*End_toEndVerification.First_Name)

    def getLast_Name(self):
        return self.driver.find_element(*End_toEndVerification.Last_Name)

    def getPhone(self):
        return self.driver.find_element(*End_toEndVerification.Phone)

    def getAddress(self):
        return self.driver.find_element(*End_toEndVerification.Address)

    def getZip_Code(self):
        return self.driver.find_element(*End_toEndVerification.Zip_Code)

    def getState(self):
        return self.driver.find_element(*End_toEndVerification.State)

    def getExpiration_Date_Year(self):
        return self.driver.find_element(*End_toEndVerification.Expiration_Date_Year)

    def getExpiration_Date_Mon(self):
        return self.driver.find_element(*End_toEndVerification.Expiration_Date_Mon)

    def getOwner(self):
        return self.driver.find_element(*End_toEndVerification.Owner)

    def getCVV(self):
        return self.driver.find_element(*End_toEndVerification.CVV)

    def getCard_Number(self):
        return self.driver.find_element(*End_toEndVerification.Card_Number)

    def get_che_out_btn(self):
        return self.driver.find_element(*End_toEndVerification.checkout_btn)
