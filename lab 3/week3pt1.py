## Part 1 of Lab Week 3 ##
## Shane Canny ##
## 28 Oct 2019 ##

import requests
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

print(page)
print("-------------------")
print (page.content)
