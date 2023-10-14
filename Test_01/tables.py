from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/tables")

row = len(driver.find_elements(By.XPATH, "//table[@id='table1']/descendant::tr"))
print(row)
col = len(driver.find_elements(By.XPATH, "//table[@id='table1']/descendant::th"))
print(col)

for r in range(1, row):
    for c in range(1, col + 1):
        print(driver.find_element(By.XPATH, "//*[@id='table1']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text)
