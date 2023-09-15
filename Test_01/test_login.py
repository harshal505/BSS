import time

import pytest

# from selenium import webdriver

from Test_data.Xlread import Read_test_data
from Utilities.BaseClass import BaseClass
from PageObjectModel.LoginPageObjects import LoginPageVerification


# driver=webdriver.Chrome()


# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.find_element().click()

class Test_login(BaseClass):

    def test_02(self, getData):
        LinV = LoginPageVerification(self.driver)
        self.getLogger().info("The  Chrome browser initiated")
        LinV.getLoginTab().click()
        # time.sleep(2)
        self.getLogger().info("The Email is " + (getData[0]))
        LinV.getEmailText().send_keys(getData[0])
        self.getLogger().info("The Password is " + (getData[1]))
        LinV.getPassText().send_keys(getData[1])
        LinV.getLoginBut().click()
        # self.driver.refresh()
        time.sleep(3)
        # expected_title = LinV.getExpected_Result().text()
        # if self.driver.title == expected_title:
        #     assert True
        # else:
        #     assert False


# @pytest.fixture(params=[{"Email": "hbhagat505@gmail.com", "": "Pass@123"}, {"Email": "hbhagat5055@gmail.com", "Password": "Pass@1234"}])

@pytest.fixture(params=Read_test_data.getData())
def getData(request):
    return request.param
# pytest -rA test_login.py
