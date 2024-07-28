from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://hrselfserve.info.yorku.ca/")

username = input("") #Enter your ppy Username
password = "XXXXXXX" #Enter your ppy password. 

try:
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "linkser"))
    )
    button.click()
    
    username_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "mli"))
    )

    password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "password"))
    )

    username_field.send_keys(username)
    password_field.send_keys(password)

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input.btn.btn-lg.btn-primary"))
    )
    login_button.click()

    
except Exception as e:
    print(f"An error took place: {e}")

time.sleep(20)

driver.quit()



