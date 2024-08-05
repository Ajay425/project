from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://hrselfserve.info.yorku.ca/")

username = ""  # Enter your ppy Username
password = ""  # Enter your ppy password.
timein = ""  #enter timein
timeout ="" #enter timeout


try:
    # Wait for the 'linkser' button to be clickable and click it
    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "linkser"))
    )
    button.click()
    print("Clicked the linkser button.")

    # Wait for the username and password fields to be present
    username_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "mli"))
    )
    password_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    
    # Ensure the username and password fields are visible and interactable
    WebDriverWait(driver, 20).until(
        EC.visibility_of(username_field)
    )
    WebDriverWait(driver, 20).until(
        EC.visibility_of(password_field)
    )

    # Input username and password
    username_field.send_keys(username)
    password_field.send_keys(password)
    print("Entered username and password.")

    # Wait for the login button to be clickable and click it
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input.btn.btn-lg.btn-primary"))
    )
    login_button.click()
    print("Clicked the login button.")
    
    time.sleep(30)
    # Wait for the hours card to be clickable and click it
    hours_card = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='win0groupletPTNUI_LAND_REC_GROUPLET$1']"))
    )
    hours_card.click()
    print("Clicked the hours card button.")

    enter_time = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='win0groupletPTNUI_LAND_REC_GROUPLET$1']"))
    )
    enter_time.click()
    print("Clicked the enter time button.")

    timein_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "PUNCH_TIME_1$8"))
    )
    timeout_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "PUNCH_TIME_4$8"))
    )
    
    timein_field.send_keys(timein)
    timeout_field.send_keys(timeout)
    
    #need to get the Id for in and out timestamps
    #in timestamps = PUNCH_TIME_1$8
    #out timestamp = PUNCH_TIME_4$8
    #id for submit button TL_LINK_WRK_SUBMIT_PB
except Exception as e:
    print(f"An error took place: {e}")

# Wait for some time to observe the actions
time.sleep(30)

# Close the browser
driver.quit()
