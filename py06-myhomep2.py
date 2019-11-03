## Part 4 of Lab Week 3 ##
## Shane Canny ##
##  03 Nov 2019 ##

import requests
from bs4 import BeautifulSoup
page = requests.get("https://oldwww.myhome.ie/residential/mayo/property-for-sale?page=1")
soup = BeautifulSoup(page.content, 'html.parser')
print (soup.prettify())
listings = soup.find("div", class_="topspot" )
print (listings)