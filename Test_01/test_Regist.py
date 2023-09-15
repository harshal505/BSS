import time

import pytest

from Utilities.BaseClass import BaseClass
from PageObjectModel.RegistrationPage import RegistrationPageVerification


class TestRegisValid(BaseClass):

    def test(self, getDataR):
        self.getLogger().info("Test case is started")
        reg = RegistrationPageVerification(self.driver)
        reg.getRegTab().click()
        time.sleep(2)
        reg.getNameText().send_keys(getDataR["name"])
        self.getLogger().info(getDataR["name"])
        time.sleep(2)
        reg.getE_Mail_Address().send_keys(getDataR["Email"])
        time.sleep(2)
        reg.getPassword().send_keys(getDataR["Password"])
        time.sleep(2)
        reg.getConfirm_Password().send_keys(getDataR["confpass"])
        time.sleep(2)
        reg.getRegister().click()
        time.sleep(5)


# pytest -rA test1_Regist.py

@pytest.fixture(params=[{"name": "harshal", "Email": "hbhagat505@gmail.com",
                         "Password": "12345@", "confpass": "12345@"}])
def getDataR(request):
    return request.param

# pytest -rA --html="../Reports/reg.html"
