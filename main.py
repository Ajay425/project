from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/cookieclicker/")



WebDriverWait(driver, 5).until(#
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

WebDriverWait(driver, 10).until(#
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

cookie = driver.find_element(By.ID, "bigCookie")
cookie.click()

time.sleep(10)


#input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
#input_element.clear()
#input_element.send_keys("tech with tim" + Keys.ENTER)

#WebDriverWait(driver, 5).until(#
    #EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))
#)
###
#link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim") #finds based on the first thing on browser
#link.click()




driver.quit()
