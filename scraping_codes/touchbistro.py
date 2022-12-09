import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
URL = "https://www.touchbistro.com/blog/culinary-terms-for-restaurants/"
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
page = requests.get(URL,headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
data = pd.DataFrame(columns=["word","meaning"])
word=[]
meaning=[]
l = soup.find_all('ol')
for i in l:
    i_ = i.find_all('li')
    for k in i_:
        k_ = k.text.strip().lower().split(": ")
        meaning.append(k_[1])
        wo = k_[0]
        k__= wo.split(" (")
        w = k__[0].replace(" ","-")
        # d = {"word":word,"meaning":meaning}
        word.append(w)
        # data = data.append(d,ignore_index=True)
data["word"]=word
data["meaning"]=meaning
data.to_csv("culinary_vocab.csv")

