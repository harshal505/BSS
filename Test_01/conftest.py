import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

driver=None

@pytest.fixture(scope="class")
def setup(request):
    global driver
    Browser_name = request.config.getoption("browser_name")

    if Browser_name == "chrome":
        driver = webdriver.Chrome()

    elif Browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    driver.get("https://automation.credence.in/shop")
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()

