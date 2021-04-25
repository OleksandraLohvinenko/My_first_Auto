from selenium import webdriver
from datetime import date, date

driver = webdriver.Chrome("D:\Downloads\chromedriver_win32 (1)\chromedriver.exe")

# Navigate to url
driver.get("https://www.y8.com/ ")

# Returns and base64 encoded string into image
driver.save_screenshot('./site/y8.com' + str(date.today()) + '.png')

driver.quit()