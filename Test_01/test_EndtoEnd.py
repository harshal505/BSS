import time

import pytest

from PageObjectModel.EndtoEndPageObject import End_toEndVerification
from Utilities.BaseClass import BaseClass


class Test_End_toEnd(BaseClass):

    def test_end(self, getDataE):
        En = End_toEndVerification(self.driver)
        self.getLogger().info("The browser initiated")
        En.getLoginTab().click()
        # time.sleep(2)
        En.getEmailText().send_keys(getDataE["Email"])
        self.getLogger().info("The email text is " + getDataE["Email"])
        # time.sleep(2)
        En.getPassText().send_keys(getDataE["Password"])
        # time.sleep(1)
        En.getLoginBut().click()
        # time.sleep(5)
        En.getProduct().click()
        time.sleep(2)
        En.getCart().click()
        time.sleep(2)
        En.getCheckout().click()
        En.getFirst_Name().send_keys(getDataE["Name"])
        En.getLast_Name().send_keys(getDataE["Lname"])
        En.getPhone().send_keys(getDataE["Phone"])
        En.getAddress().send_keys(getDataE["Address"])
        En.getZip_Code().send_keys(getDataE["Zip"])
        self.getOption(En.getState(), getDataE["State"])
        self.getOption(En.getExpiration_Date_Year(), "2024")
        self.getOption(En.getExpiration_Date_Mon(), "February")

        time.sleep(10)


@pytest.fixture(params=[{"Email": "hbhagat505@gmail.com", "Password": "12345@",
                         "Name": "Harshal", "Lname": "Bhagat", "Phone": "9011112540",
                         "Address": "Pune", "Zip": "440029", "State": "Pune"}])
def getDataE(request):
    return request.param
# pytest -rA test_EndtoEnd.py
