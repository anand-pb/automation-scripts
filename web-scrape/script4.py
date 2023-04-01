from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

# response = browser.get('http://libgen.is')

# lmnt = browser.find_element(By.ID, 'searchform')
 
# lmnt.send_keys('steven strogatz sync')

# lmnt.submit()

# response = browser.get('http://libgen.is')

# mirr_lmnt = browser.find_element(By.TAG_NAME, 'a')

# mirr_lmnt.click()

# response = browser.get('http://libgen.is')

# lmnt = browser.find_element(By.TAG_NAME, 'h1')

# print(lmnt.text)

response = browser.get('http://libgen.is')

lmnt = browser.find_element(By.TAG_NAME, 'body')

print(lmnt.text)