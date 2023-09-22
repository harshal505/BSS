import pytest

from PageObjectModel.RegistrationPage import RegistrationPageVerification
from Utilities.BaseClass import BaseClass


class Test_Registration(BaseClass):

    @pytest.mark.sanity
    def test_Name(self):
        reg = RegistrationPageVerification(self.driver)
        reg.getRegTab().click()
        reg.getNameText().send_keys("A")
        self.getLogger().info("The Element is Recady to accept the Alphabets")

    def test_Email(self):
        reg = RegistrationPageVerification(self.driver)
        reg.getE_Mail_Address().send_keys("B")
        self.getLogger().info("The Element is Ready to accept the Alphabets")
