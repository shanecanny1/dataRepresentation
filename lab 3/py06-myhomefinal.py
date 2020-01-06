## Part 4 of Lab Week 3 ##
## Shane Canny ##
##  03 Nov 2019 ##

import requests
import csv
from bs4 import BeautifulSoup
page = requests.get("https://oldwww.myhome.ie/residential/mayo/property-for-sale?page=1")
soup = BeautifulSoup(page.content, 'html.parser')

home_file = open("home_file.csv",mode="w",encoding="utf-8")
home_writer = csv.writer(home_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

listings = soup.findAll("div", class_="resultBody")

for listing in listings:
    entryList=[]

    price=listing.find(class_="price")
    entryList.append(price)

    address=listing.find(class_="ResidentialForSale")
    entryList.append(address)
  

    home_writer.writerow(entryList)
home_file.close()
