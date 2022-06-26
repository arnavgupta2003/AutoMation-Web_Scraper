from posixpath import split
from tkinter.ttk import Separator
import requests
from bs4 import BeautifulSoup

news_url = "https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html"

#Req
res = requests.get(news_url)
data = BeautifulSoup(res.text,'html.parser')

#Data
heading=data.find('h1').text

#STDOut
print(heading)
for i in range(5):
    cont = data.find_all(class_='Paragraph__component')[i].get_text(separator='\s')
    print(cont,end="\n")
    print("")