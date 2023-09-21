from selenium import webdriver
import pytest

# driver = None


@pytest.fixture
def setup():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield
    print(driver.title)
    driver.close()


def test_verifyLoginPage(setup):
    driver.get("https://www.facebook.com")
