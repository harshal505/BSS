from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.yahoo.com/")
Trend1 = driver.find_element(By.XPATH, "//div[@class='D(b) H(16px) Bxz(bb) Mt(8px)']/descendant::a[1]")
print(Trend1.text)
driver.close()