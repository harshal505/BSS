import inspect
import logging

import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    @staticmethod
    def getLogger():
        # loggerName = inspect.stack()[1][3]
        # logger = logging.getLogger(loggerName)
        # file = logging.FileHandler(r'H:\Harshal data\pythonProject\pythonProject2\Logs\logfile.logs')
        # formatter = logging.Formatter("%(lineno)s: %(asctime)s:%(levelname)s:%(name)s:%(message)s:")
        # file.setFormatter(formatter)
        # logger.addHandler(file)
        # logger.setLevel(logging.DEBUG)
        # return logger
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler(r'H:\Harshal data\pythonProject\pythonProject2\Logs\logfile.logs')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
    def getOption(self, ele, text):
        opt = Select(ele)
        opt.select_by_visible_text(text)

    def getAlert(self, action):
        if action == "ok":
            self.driver.switch_to.alert.accept()
