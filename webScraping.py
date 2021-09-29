from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

options = webdriver.ChromeOptions()

options.add_argument("no-default-browser-check")
options.add_argument('headless')
options.add_argument('disable-dev-shm-usage')

driver = webdriver.Chrome('C:\Windows\chromedriver' , options=options)

id = []
title = []
description = []
completed = []

driver.get("http://localhost:8000/api/todos/")

content  = driver.page_source
soup = BeautifulSoup(content , "html.parser")

for ids in soup.findAll('span' , attrs={'class' : 'lit'} ):
    if ids.text != "GET, POST, HEAD, OPTIONS" and ids.text != "application/json" and ids.text != "Accept":
        id.append(ids.text)

for titles in soup.findAll('span' , attrs={'class' : 'str'}):
    if titles.text != "\"id\"" and titles.text != "\"title\"" and titles.text != "\"description\"" and titles.text != "\"completed\"" :
        title.append(titles.text)

for descriptions in soup.findAll('span' , attrs={'class' : 'kwd'}):
    description.append(descriptions.text)

# print(title[0])

i = 0
while i < len(title):
  print(title[i])
  i += 1
    

# driver.close()