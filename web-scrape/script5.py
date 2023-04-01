from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

# response = browser.get('https://www.freecodecamp.org/news/git-cheat-sheet/')
response = browser.get('https://github.com/firstcontributions/first-contributions/')

lmnts = browser.find_elements(By.TAG_NAME, 'code')

# txtfile = open('C:\\Users\\APB\\Desktop\\git-commands.txt', 'a')
txtfile = open('C:\\Users\\APB\\Desktop\\github-contributions-how.txt', 'a')

for lmnt in lmnts:
    # print(lmnt.text + "\n")
    txtfile.write(lmnt.text + "\n")

txtfile.close()    