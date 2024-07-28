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

try:
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "linkser"))
    )
    button.click()
except Exception as e:
    print(f"An error took place: {e}")

time.sleep(10)

driver.quit()



