# Not working, edit as you like.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# Open a web browser
driver = webdriver.Firefox()#replace with Chrome alternatively

# disclaimer
print("By using this script, you agree to the STEAM® SUBSCRIBER AGREEMENT, which can be found at: https://store.steampowered.com/subscriber_agreement/")
time.sleep(3)

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
driver.get("https://store.steampowered.com/join")
e = driver.find_element_by_id("email")
e.send_keys(Keys.CONTROL, 'v')
ee = driver.find_element_by_id("reenter_email")
ee.send_keys(Keys.CONTROL, 'v')
i = driver.find_element_by_id("captchaImg")
print(i.get_attribute('src'))
ii = raw_input("Solve The Capcha: ")
iit = driver.find_element_by_id("captcha_text")
iit.send_keys(ii)
agree = driver.find_element_by_id('i_agree_check')
agree.click()
con = driver.find_element_by_id('createAccountButton')
con.click()

# Submit the form
submit_button = driver.find_element_by_css_selector('button[type="submit"]')
submit_button.click()


print(f'Email: {email}')
print(f'Password: {password}')
driver.quit()

