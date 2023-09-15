from selenium.webdriver.common.by import By


class HomePageVerification:

    def __init__(self, driver):
        self.driver = driver

    # HomeTitle = (By.XPATH, "/html/head/title")

    @property
    def getHomePage(self):
        return self.driver.title
