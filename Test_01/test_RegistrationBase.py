import random
import string
import time

import pytest

from PageObjectModel.RegistrationPage import RegistrationPageVerification
from Utilities.BaseClass import BaseClass


class Test_Registration(BaseClass):

    @pytest.mark.sanity
    def test_Name(self):
        reg = RegistrationPageVerification(self.driver)
        reg.getRegTab().click()
        name = random_generator()
        reg.getNameText().send_keys(name)
        reg.getE_Mail_Address().send_keys(random_generator() + "@gmail.com")
        reg.getPassword().send_keys("12345@")
        reg.getConfirm_Password().send_keys("12345@")
        reg.getRegister().click()
        time.sleep(5)
        if reg.getSuccess().text == name:
            assert True
        else:
            self.driver.save_screenshot(r"H:\\Harshal data\\pythonProject\\pythonProject2\\Screen_shot\\Regitrar.png")
            assert False


def random_generator(size=8, char=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(char) for x in range(size))
