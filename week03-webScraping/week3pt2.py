## Part 2 of Lab Week 3 ##
## Shane Canny ##
## 28 Oct 2019 ##
import requests
from bs4 import BeautifulSoup
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print (page)
print("-------------------")
print (page.content)
soup1 = BeautifulSoup(page.content, 'html.parser')
print("-------------------")
print (soup1.prettify())