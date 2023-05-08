import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# keeps the browser open even after finishing all the instructions
options = Options()
options.add_experimental_option('detach', True)

# stating which browser we are using and linking it with PATH
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

# Opening the site
driver.get('https://www.neuralnine.com/')

# finding links on website
# // means whole document; a refers to which tag; @href means the a tag schould contain an href attribute
# xpath is a language used to parse xml (like html)
links = driver.find_elements(By.LINK_TEXT, 'Books')
for link in links:
    # getting all the html nested inside the a tag and seeing if it contains Books
    if 'Books' in link.get_attribute("innerHTML"):
        # clicking on the link
        link.click()
        break

book_links = driver.find_elements(By.LINK_TEXT,
                                  'Books')

book_links[0].click()

driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
buttons = driver.find_elements(By.XPATH,
                               '//a[.//span[text()[contains(., "Paperback")]]]//span[text()[contains(., "₹")]]')
for button in buttons:
    print(button.get_attribute("innerHTML"))