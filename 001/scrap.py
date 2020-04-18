from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path='/home/twc/chromedriver')

driver.get('https://www.rightbros.co')

html_doc = driver.page_source
soup = BeautifulSoup(html_doc, 'lxml')

print(soup.prettify())

driver.quit()