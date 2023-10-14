from selenium import webdriver
import pytest


# driver = None


def test_verifyLoginPage(setup):
    driver.get("https://www.facebook.com")
    assert driver.title == "Facebook – log in or sign up"


@pytest.fixture
def setup():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield
    print(driver.title)
    driver.close()
