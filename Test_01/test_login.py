import time

import pytest

# from selenium import webdriver

from Test_data.readfile import Read_test_data
from Utilities.BaseClass import BaseClass
from PageObjectModel.LoginPageObjects import LoginPageVerification
from Utilities import XLreadUtilies


# driver=webdriver.Chrome()


# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.find_element().click()

class Test_login(BaseClass):

    def test_02(self):
        self.getLogger().info("*********** Execution Started****************")
        LinV = LoginPageVerification(self.driver)
        path = r"H:\Harshal data\pythonProject\pythonProject2\Test_data\datafile.xlsx"
        rows = XLreadUtilies.getRowCount(path, "User")
        sheetName = "User"
        print(rows)
        LinV.getLoginTab().click()
        for r in range(2, rows + 1):
            LinV.getEmailText().send_keys(XLreadUtilies.readData(path, sheetName, r, 1))
            self.getLogger().info(XLreadUtilies.readData(path, sheetName, r, 1))
            LinV.getPassText().send_keys(XLreadUtilies.readData(path, sheetName, r, 2))
            self.getLogger().info(XLreadUtilies.readData(path, sheetName, r, 2))
            LinV.getLoginBut().click()
            if LinV.getExpected_Result() == "harshal":
                XLreadUtilies.writeData(path, sheetName, r, 4, "Pass")
                self.getLogger().info("**************Successful Login********************")
                self.getLogger().info("**************Positive Scenario********************")
            else:
                XLreadUtilies.writeData(path, sheetName, r, 4, "Fail")
                self.getLogger().error("*************Negative Scenario******************")
            exp_result = XLreadUtilies.readData(path, sheetName, r, 3)
            act_result = XLreadUtilies.readData(path, sheetName, r, 4)
