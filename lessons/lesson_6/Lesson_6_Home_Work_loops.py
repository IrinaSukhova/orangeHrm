'''
Homework Assignment: Using Loops
Objective: Open the web application, log in, navigate to the "HR Administration" section via the side menu, and click on the "Add User" button. Once on the "Add User" page, your task is to retrieve and list all the names of input fields relevant to user information, such as employee name, username, etc. Use loops to iterate over elements and gather this information.

Steps:

Open the web application in a browser.
Log into the application with provided credentials.1
From the side menu, navigate to the "HR Administration" section.
Click on the "Add User" button, usually represented by a big green button.
On the "Add User" form, identify all input fields related to user information.
Use a loop to iterate over these input fields and collect their names.
Print the list of field names you have collected.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://portnov_admin-trials711.orangehrmlive.com/client/#/dashboard")

driver.find_element(By.CSS_SELECTOR, "input[id='txtUsername']").send_keys("Admin")
driver.find_element(By.CSS_SELECTOR, "input[id='txtPassword']").send_keys("qTJn5@5APu")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(5)
driver.find_element(By.XPATH, "(//div[@id='menu-container'] //span[text()='HR Administration'])[1]").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, 'div[class="fixed-action-btn floating-add-btn tooltipped"]').click()

time.sleep(5)
section_texts = []
menu_items = driver.find_elements(By.XPATH, "//div[@class='modal-content ']//label")

for item in menu_items:
    section_texts.append(item.text)

print(section_texts)

# Close the browser
driver.quit()