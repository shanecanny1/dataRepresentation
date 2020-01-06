## Part 3 of Lab Week 3 ##
## Shane Canny ##
## 28 Oct 2019 ##

from bs4 import BeautifulSoup
with open("../carviewer.html") as fp:
 soup = BeautifulSoup(fp,'html.parser')

print(soup.prettify())