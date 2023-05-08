from bs4 import BeautifulSoup
import csv
import pandas as pd

with open("blog.html") as html_file:
    soup = BeautifulSoup(html_file,"lxml")

# to get all code print soup. To get a specific tag, do soup.<tag name> like soup.title or soup.body. to get ony text add
# .text at the end. To add indent add .prettify. To define the class, use soup.find(div, class_=<class name>)
# To find all occurences of a tag, use find_all() in the same way as find(). to extract the url from an a tag use a["href"]
# You can use this for any tag parameter/attribute. eg: div["class"]

table = soup.find("table")

tr = table.find_all("tr")

data = [[td.text for td in trows.find_all("td")] for trows in tr[1:]]
print(data)