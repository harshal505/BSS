from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/dynamic_controls")
driver.find_element(By.XPATH, "//form[@id='checkbox-example']/child::button").click()
driver.implicitly_wait(10)
# req = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[@id='message']")))
req = driver.find_element(By.XPATH, "//p[@id='message']")
print(req.text)

driver.find_element(By.XPATH, "//form[@id='input-example']/child::button").click()
# driver.find_element(By.XPATH,"//p[@id='message']")
# req2 = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[@id='message']")))
req2 = driver.find_element(By.XPATH, "//p[@id='message']")
print(req2.text)
