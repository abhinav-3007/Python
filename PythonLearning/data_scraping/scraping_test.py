from bs4 import BeautifulSoup
import requests
import csv

# Oceania

link = requests.get("https://www.worldometers.info/coronavirus/").text
soup = BeautifulSoup(link,"lxml")
file = open("Africa.csv", "w")
writer = csv.writer(file)

writer.writerow(["S.no",
    "Country",
    "Total Cases",
    "New Cases",
    "Total Deaths",
    "New Deaths",
    "Total Recovered",
    "New Recovered",
    "Active Cases",
    "Serious/Critical",
    "Total Cases per 1M pop",
    "Deaths per 1M pop",
    "Total Tests",
    "Tests per 1M pop",
    "Population",
    "Continent",
    "1 Case every X ppl",
    "1 Death every X ppl",
    "1 Test every X ppl"
])



table = soup.find("table", id="main_table_countries_today")
serial = 1

for tr in table.tbody.find_all("tr"):
    li=[]
    for td in tr.find_all("td"):
        li.append(td.text.strip())

    if li[0] != "" and li[-4] == "Asia":
        li.pop(0)
        li.insert(0,serial)
        writer.writerow(li)
        serial+=1
