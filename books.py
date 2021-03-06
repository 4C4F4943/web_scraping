import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import time
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from tqdm import trange
#url = https://drop.com/mechanical-keyboards/drops

import urllib.request

def tiny_url(url):
    apiurl = "http://tinyurl.com/api-create.php?url="
    tinyurl = urllib.request.urlopen(apiurl + url).read()
    return tinyurl.decode("utf-8")



def get_data(pageNo):  
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    r = requests.get("https://lib.ugent.be/en/catalog?max_year=2020&min_year=1950&page="+str(pageNo)+"&q=machine+learning&type=book")
    content = r.content
    soup = BeautifulSoup(content, features="html.parser")
    #print(soup)
    
    all1 = []
    for d in soup.findAll('article', attrs={'class':'col-md-12 search-result'}):
        
        #print("this is url1: ",url1)
        
        try:
            isUgent = d.find("small",attrs={"help-block text-center"}).text
            #print(isUgent.text)
            #print(isUgent.text)
            exit
        except:
            name = d.find("h2",attrs={"class":"search-result__title meta-title"}).a.text
            name = name[2:-1]
            als = []
            #print("this is name: ",name)
            # url1= d.find('a')["href"]
            url1 = d.find("a")
        
            url2 = "https://lib.ugent.be/"+url1["href"]
            url1 = tiny_url(url2)
            #print("it isnt ugent: ",name[2:-3].replace("\n",""))
            #print("not ugent:)")
            #print("url: ",url1)
            
            
            als.append(name[2:-3].replace("\n",""))
            als.append(url1)
            all1.append(als)
        
    return all1

results = []
no_pages = 20
#### for some reason this works [[['       Machine Learning and Biometrics    ', 'https://tinyurl.com/y5h3ryjg']]]
# should be like [[name,href],[name,href]]
for i in (t :=trange(1,no_pages +1)):
#for i in range(1, no_pages+1):
    t.set_description("the current page: {}".format(i))
    x = get_data(i)
    #print("this is x: ",x)
    if x != []:
        results.append(x)
    else:
        #print("not adding it")
        pass
#print("this is results: ",results)


flatten = lambda l: [item for sublist in l for item in sublist]
df = pd.DataFrame(flatten(results),columns=['Name','link to book'])
df.to_csv('books.csv', index=False, encoding='utf-8')

df = pd.read_csv("books.csv")
#pd.set_option("display.max_rows", None, "display.max_columns", None)
print(df)