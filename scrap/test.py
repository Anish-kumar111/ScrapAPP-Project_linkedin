import os
# import linkedin.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"C:/SeleniumDriver"
driver = webdriver.Chrome()
driver.get('https://www.mishodesigns.com/collections/rings-1')
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver.implicitly_wait(10)
# array = []
# all_links = driver.find_elements_by_class_name("ProductItem__Title Heading").text
# for i in all_links:
#  print(all_links)
elements = driver.find_elements(By.TAG_NAME, 'h2')

for e in elements:
    print(e.text)