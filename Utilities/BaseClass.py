import inspect
import logging

import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    @staticmethod
    def getLogger():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        file = logging.FileHandler('../Logs/LogFiles.log')
        formatter = logging.Formatter("%(lineno)s: %(asctime)s:%(levelname)s:%(name)s:%(message)s:")
        file.setFormatter(formatter)
        logger.addHandler(file)
        logger.setLevel(logging.DEBUG)
        return logger

    def getOption(self, ele, text):
        opt = Select(ele)
        opt.select_by_visible_text(text)
