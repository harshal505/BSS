import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get(
    "file:///C:/Users/Harshal/AppData/Local/Temp/Tempb5bd5226-c80f-4d08-87fe-c0553798c3eb_upload_6e74e28e-2957-4fd2-9a51-7a5493e8d93f.zip/linkgeneration.html")
# time.sleep(5)
allElements = driver.find_elements(By.XPATH, "/html/body/ul/li/a")
# print(allBrowsers)
for item in allElements:
    item.click()
    time.sleep(2)
all_windows = driver.window_handles
for i in all_windows:
    driver.switch_to.window(i)
    if driver.title == "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!":
        break
print(driver.title)
Trend1 = driver.find_element(By.XPATH, "//div[@id='toast-ctn']")
drp = Select(Trend1)
drp.select_by_visible_text("Women Ethnic")
# actions = ActionChains(driver)
# ele = driver.find_element(By.XPATH, "//a[@class='_1BJVlg _11MZbx']")
# actions.move_to_element(Trend1).move_to_element(ele).click().perform()
time.sleep(5)
