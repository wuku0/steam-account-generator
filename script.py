from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the web browser and navigate to tempmail.ninja
driver = webdriver.Firefox()
driver.get("https://tempmail.ninja/")
time.sleep(5)
# Find the element containing the email address and copy it
email_element = driver.find_element_by_id("emailtemporal")
email_element.click()
email = email_element.get_attribute("value")
time.sleep(5)
# Print the email address
print(email)

# Navigate to the password generator page
driver.get("https://www.dashlane.com/features/password-generator")

# Find the password element
password_element = driver.find_element_by_id("generated-password")

# Copy the password
password = password_element.get_attribute("value")

# Print the password
print(password)

# Close the browser
driver.close()
