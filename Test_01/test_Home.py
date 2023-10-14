import pytest


from PageObjectModel.HomePage import HomePageVerification
from Utilities.BaseClass import BaseClass


class TestHomePageValidations(BaseClass):

    def test_01(self):
        home = HomePageVerification(self.driver)
        logs = self.getLogger()
        logs.info("The chrome browser is initiated")
        logs.info("Home is started")
        print("the page title", home.getHomePage)
        assert home.getHomePage == "CredKart"
# pytest -rA test_Home.py