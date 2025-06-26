"""
Task 2: Automated Testing with AI
Automate a test case for a login page (valid/invalid credentials) using Selenium.
Demo site: https://practicetestautomation.com/practice-test-login/
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the Selenium WebDriver (Chrome)
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

def login(username, password):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)  # Wait for page to load
    
# Test with valid credentials
login("student", "Password123")
if "Logged In Successfully" in driver.page_source:
    print("Valid login: SUCCESS")
else:
    print("Valid login: FAILURE")
driver.back()

# Test with invalid credentials
login("student", "wrongpassword")
if "Your password is invalid!" in driver.page_source:
    print("Invalid login: SUCCESS (error detected)")
else:
    print("Invalid login: FAILURE (error not detected)")

driver.quit() 