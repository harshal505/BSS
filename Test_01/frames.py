from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/nested_frames")
driver.switch_to.frame("frame-top")
# driver.switch_to.frame("frame-left")
# print(driver.find_element(By.XPATH, "//body").text)
# driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-middle")
print(driver.find_element(By.XPATH, "//div[@id='content']").text)
