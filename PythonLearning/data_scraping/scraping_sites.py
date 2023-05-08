from bs4 import BeautifulSoup
import requests
import csv


def find_div_with_class(tag):
    return tag.name == 'div' and tag['class'] == ['col-md-10']


source = requests.get("https://www.imdb.com/chart/top/").text
soup = BeautifulSoup(source, "lxml")

file = open("imdb_top.csv", "w")
writer = csv.writer(file)

writer.writerow(["Rank", "Movie Title", "Cast", "Release Year", "IMDb Rating", "Total Votes"])

for tr in soup.tbody.find_all("tr"):
    td = tr.find("td", class_="titleColumn")
    rank = td.text.split(".")[0].strip()
    rates = tr.strong["title"].split()[3]
    writer.writerow([rank, td.a.text, td.a["title"], td.span.text[1:-1], tr.strong.text, rates])

file.close()
