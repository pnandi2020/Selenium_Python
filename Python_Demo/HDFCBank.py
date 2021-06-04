from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait



browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://netbanking.hdfcbank.com/netbanking/")
browser.switch_to.frame("login_page")
username = browser.find_element_by_name('fldLoginUserId').send_keys("1000")
submit = browser.find_element_by_xpath("//img[@alt='continue']")
#username.send_keys("1000")
submit.click()

browser.switch_to.default_content()
browser.switch_to.frame(1)
browser.find_element_by_link_text("Terms and Conditions").click()

wait = WebDriverWait(browser, 20)
page_title = browser.title
print(page_title)
browser.close()