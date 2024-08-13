from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service 
from selenium.webdriver.firefox.options import Options
import time


options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe" 


service = Service("D:\geckodriver.exe")
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://demo.dealsdray.com/")
time.sleep(3)
username_input = "prexo.mis@dealsdray.com"
password_input = "prexo.mis@dealsdray.com"
username = driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username_input)
password = driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password_input)
login = driver.find_element(By.XPATH, "(//button)[2]").click()
time.sleep(2)
order = driver.find_element(By.XPATH, "(//button)[2]").click()
time.sleep(2)
suborder = driver.find_element(By.XPATH, "(//button)[3]").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//button)[6]").click()
time.sleep(2)
filepath = "D:\project\demo-data.xlsx"
choose = driver.find_element(By.XPATH, "(//input)[2]").send_keys(filepath)
time.sleep(2)
driver.find_element(By.XPATH, "(//button)[7]").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//button)[7]").click()
time.sleep(2)
alert = driver.switch_to.alert
alert.accept()
time.sleep(3)
screenshot_path = "D:\project1\last_page_screenshot.png"  
driver.save_screenshot(screenshot_path)
print(f"Screenshot saved to {screenshot_path}")
print("complete")
driver.quit()
