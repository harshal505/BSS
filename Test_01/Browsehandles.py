import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get(
    "file:///C:/Users/Harshal/AppData/Local/Temp/Tempc54816c3-8d2f-43e6-8037-1d33f78f1bff_upload_6e74e28e-2957-4fd2-9a51-7a5493e8d93f.zip/linkgeneration.html")
elements = driver.find_elements(By.TAG_NAME, "a")

for element in elements:
    element.click()

allWindows = driver.window_handles
print("all windows id", allWindows)
a = {}

for win in allWindows:
    driver.switch_to.window(win)
    key: str = driver.title
    value = win
    a.update({key: value})

print(a)
driver.switch_to.window(a.get("Facebook – log in or sign up"))
print(driver.title)
