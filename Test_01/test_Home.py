import pytest


from PageObjectModel.HomePage import HomePageVerification
from Utilities.BaseClass import BaseClass


class TestHomePageValidations(BaseClass):

    def test_01(self):
        home = HomePageVerification(self.driver)
        logs = self.getLogger()
        logs.info("Home is started")
        print("the page title", home.getHomePage)
        assert home.getHomePage == "CredKart"
