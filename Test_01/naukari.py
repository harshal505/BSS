import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.naukri.com/")
driver.maximize_window()
loginBtn = driver.find_element(By.XPATH, "//a[@id='login_Layer']")
loginBtn.click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']").send_keys(
    "harshall.bhagatt@gmail.com")
driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("9890728328")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
# time.sleep(3)
lbnbtt = WebDriverWait(driver, 10).until(
    expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt='naukri user profile img']")))
lbnbtt.click()
View_Update = WebDriverWait(driver, 10).until(
    expected_conditions.visibility_of_element_located((By.XPATH, "//a[@class='nI-gNb-info__sub-link']")))
View_Update.click()
time.sleep(2)
driver.find_element(By.XPATH, "//i[@title='Click here to delete your resume']").click()
driver.find_element(By.XPATH,
                    "//div[@class='lightbox model_open flipOpen']//button[@class='btn-dark-ot'][normalize-space()='Delete']").click()
time.sleep(1)
# driver.find_element(By.XPATH, "//div[@class='uploadCont']").send_keys("C:\\Users\\Harshal\\Downloads\\Harshal_B_updated_Resume.pdf")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='attachCV']").send_keys(
    r"H:\Latest Resume\Harshal_Bhagat_Updated_Resume.pdf")
time.sleep(1)
ele = driver.find_element(By.XPATH, "//span[@class='widgetTitle typ-16Bold'][normalize-space()='Resume headline']")
deleteBtn = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//span[normalize-space()='Resume headline']/following-sibling::span")))
deleteBtn.click()
driver.execute_script("arguments[0].scrollIntoView()", ele)
saveBtn = WebDriverWait(driver, 10).until(
    expected_conditions.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Save']")))
saveBtn.click()
driver.execute_script("window.scrollTo(0,0)")
profileBtn = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt='naukri user profile img']")))
profileBtn.click()

logOutBtn = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[@title='Logout']")))
logOutBtn.click()
time.sleep(1)
action = ActionChains(driver)
action.context_click().perform()
time.sleep(3)
