from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Open a web browser
driver = webdriver.Firefox()#replace with Chrome alternatively


driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get('https://tempmail.ninja')

# Click the element with the ID "botoncopiar" to get the email
email_element = driver.find_element_by_id('botoncopiar')
email = email_element.text
email_element.click()


driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])
driver.get('https://www.dashlane.com/features/password-generator')

# Click the "Copy password" button to get the password
password_button = driver.find_element_by_css_selector('.button.button--primary')
password_button.click()

# Switch back to the first tab and navigate to the Steam sign-up page
driver.switch_to.window(driver.window_handles[0])
driver.get('https://store.steampowered.com/join/')

# Fill out the form on the sign-up page with the email and password
username_field = driver.find_element_by_id('username')
username_field.send_keys('my_username')
email_field = driver.find_element_by_id('email')
email_field.send_keys(email)
password_field = driver.find_element_by_id('password')
password_field.send_keys(password)

# Submit the form
submit_button = driver.find_element_by_css_selector('button[type="submit"]')
submit_button.click()


print(f'Email: {email}')
print(f'Password: {password}')
driver.quit()

