from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuration
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://hrselfserve.info.yorku.ca/")

username = "xxx"  # Enter your ppy Username
password = "xxx"  # Enter your ppy password.

timein = "8:30AM"  # enter timein
timeout = "12:00PM"  # enter timeout

timein_2 = "1:00PM"  # enter timein
timeout_2 = "4:30PM"  # enter timeout

def find_element_retry(driver, by, value, retries=3, delay=2):
    for _ in range(retries):
        try:
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except Exception as e:
            print(f"Retrying due to: {e}")
            time.sleep(delay)
    raise Exception("Failed to locate element after retries")

try:
    # Wait for the 'linkser' button to be clickable and click it
    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "linkser"))
    )
    button.click()
    print("Clicked the linkser button.")

    # Wait for the username and password fields to be present
    username_field = find_element_retry(driver, By.ID, "mli")
    password_field = find_element_retry(driver, By.ID, "password")
    
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
    
    time.sleep(15)

    # Handle Duo authentication
    duo_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "trust-browser-button"))
    )
    duo_button.click()
    print("Clicked the Duo authentication button.")

    time.sleep(20)

    # Wait for the hours card to be clickable and click it
    hours_card = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='win0groupletPTNUI_LAND_REC_GROUPLET$1']"))
    )
    hours_card.click()
    print("Clicked the hours card button.")

    # Wait for the enter time button to be clickable and click it
    enter_time = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='win0groupletPTNUI_LAND_REC_GROUPLET$1']"))
    )
    enter_time.click()
    print("Clicked the enter time button.")

    time.sleep(10)

    # Find and fill in the time entry fields
    timein_field = find_element_retry(driver, By.ID, "PUNCH_TIME_1$6")
    time.sleep(5)
    timein_field.send_keys(timein)
    print("Entered In Timings")

    timeout_field = find_element_retry(driver, By.ID, "PUNCH_TIME_4$6")
    timeout_field.send_keys(timeout)
    print("Entered Out Timings")

    # Add another timestamp
    add_timestamp = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "ADD_PB$1"))
    )
    add_timestamp.click()
    print("Added another Time stamp")
    time.sleep(15)

    # Fill in the second set of time entries
    timein_field2 = find_element_retry(driver, By.ID, "PUNCH_TIME_1$7")
    timeout_field2 = find_element_retry(driver, By.ID, "PUNCH_TIME_4$7")

    timein_field2.send_keys(timein_2)
    print("Entered In Timings for the second time")
    timeout_field2.send_keys(timeout_2)
    print("Entered Out Timings for the second time")
    
    # Submit the time entries
    submit_button = WebDriverWait(driver, 10).until(
       EC.element_to_be_clickable((By.ID, "TL_LINK_WRK_SUBMIT_PB"))
    )
    submit_button.click()
    print("Submitted the time entries.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Wait for some time to observe the actions
    time.sleep(30)

    # Close the browser
    driver.quit()