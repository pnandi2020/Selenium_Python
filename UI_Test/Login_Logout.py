import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

# Step 1) Open Firefox
#browser = webdriver.ie(executable_path=IEDriverManager().install())
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# Step 2) Navigate to OrangeHRM
browser.get("https://opensource-demo.orangehrmlive.com/")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_name("txtUsername")
password = browser.find_element_by_name("txtPassword")
submit = browser.find_element_by_name("Submit")
username.send_keys("Admin")
password.send_keys("admin123")
# Step 4) Click Login
submit.click()
browser.find_element_by_partial_link_text("Welcome").click()
time.sleep(5)
browser.find_element_by_link_text("Logout").click()
login_panel=browser.find_element_by_xpath("//*[text()='LOGIN Panel']").is_displayed()
# if login_panel:
#     print("Logout successfully")
# else:
#     print("Unsuccessful")