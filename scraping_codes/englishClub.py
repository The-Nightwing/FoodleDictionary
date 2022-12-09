from cgitb import strong
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

name=[]
data = pd.DataFrame(columns=["name"])
def scrape(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    l = soup.findAll(class_="picbox")
    for i in l:
        i_ = i.find("img", alt=True)
        name.append(i_["alt"])

    l = soup.find("div", {"id": "wordchecker"})
    p = l.find_all("p")
    for i in p:
        i_ = i.find("strong")
        name.append(i_.text.strip())

URLs = ["https://www.englishclub.com/vocabulary/food-vegetables.php","https://www.englishclub.com/vocabulary/food-fruits.php","https://www.englishclub.com/vocabulary/food-grains-beans-nuts.php","https://www.englishclub.com/vocabulary/food-meats.php","https://www.englishclub.com/vocabulary/food-seafood.php","https://www.englishclub.com/vocabulary/food-dairy.php","https://www.englishclub.com/vocabulary/food-cooking.php","https://www.englishclub.com/vocabulary/food-kitchens.php","https://www.englishclub.com/vocabulary/food-dining.php","https://www.englishclub.com/vocabulary/food-restaurants.php","https://www.englishclub.com/vocabulary/food-health.php","https://www.englishclub.com/vocabulary/food-british.php","https://www.englishclub.com/vocabulary/food-chinese.php","https://www.englishclub.com/vocabulary/food-french.php","https://www.englishclub.com/vocabulary/food-indian.php","https://www.englishclub.com/vocabulary/food-italian.php","https://www.englishclub.com/vocabulary/food-mexican.php","https://www.englishclub.com/vocabulary/food-thai.php"]
for i in URLs:
    scrape(i)

for i in range(len(name)):
    word = str(name[i])
    word_ = word.split(" (")
    word= word_[0]
    word= word.lower()
    name[i] = word
data["name"] = name

data.to_csv("vocab.csv")


