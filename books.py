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
#url = https://drop.com/mechanical-keyboards/drops

import urllib.request

def tiny_url(url):
    apiurl = "http://tinyurl.com/api-create.php?url="
    tinyurl = urllib.request.urlopen(apiurl + url).read()
    return tinyurl.decode("utf-8")



def get_data(pageNo):  
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    r = requests.get("https://lib.ugent.be/en/catalog?max_year=2020&min_year=1950&page="+str(pageNo)+"&q=machine+learning&type=book")
    #print("https://lib.ugent.be/en/catalog?max_year=2020&min_year=1950&page="+str(pageNo)+"&q=machine+learning&type=book")
    #print("this thing: ",r)
    #r = requests.get('https://www.banggood.com/search/mechanical-keyboard/0-0-0-1-'+str(pageNo) + '-60-0-price-0-0_p-'+str(pageNo) +'.html')#, headers=headers)#, proxies=proxies)
    content = r.content
    soup = BeautifulSoup(content)
    #print(soup)
    
    all1 = []
    for d in soup.findAll('article', attrs={'class':'col-md-12 search-result'}):
        #name = d.find('a', attrs={'article':'middle_productsDetail_text_180710|category|18206083330'}).text
        
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
            print("not ugent:)")
            #print("url: ",url1)
            
            
            als.append(name[2:-3].replace("\n",""))
            als.append(url1)
            all1.append(als)
        # print("this is all1: ",all1)
        #print('this is name:\n','#'*30,name)
        #print('n: ',n)
        #print(d.find('a',)['href'])
        #print(d.xpath('//a[@class="middle_productsDetail_text_180710|category|18206083330"]/text()'))
        #print(d.find('img')['src'])
        #n = name.find_all('img', alt=True)
        #print(n[0]['alt'])
        #keyboard_name = d.find('a', attrs={'class':'title exclick'})
        #rating = d.find('span', attrs={'class':'a-icon-alt'})
        #users_rated = d.find('a', attrs={'class':'a-size-small a-link-normal'})
        #price = d.find('span', attrs={'class':'price notranslate'})
        #n_reviews = d.find('a', attrs={'dpid': 'middle_productsReview_image_180710|category|18206083331'}).text
        #test_name_link = d.find('a', attrs={'dpid':'middle_productsDetail_text_180710|category|18206083330'})['href']
        #url = tiny_url(url1)
        #print('shorted url: ',url)
        #print('this is price:', price)
    #print("this is all1 somewhere else: ",all1)
    #print("this is all1: ",all1)
    return all1

results = []
no_pages = 10
#### for some reason this works [[['       Machine Learning and Biometrics    ', 'https://tinyurl.com/y5h3ryjg']]]
# should be like [[name,href],[name,href]]
for i in range(1, no_pages+1):
    x = get_data(i)
    #print("this is x: ",x)
    if x != []:
        results.append(x)
    else:
        print("not adding it")
        pass
#print("this is results: ",results)

#file = open("books.data","w+")
#file.write(str(results))
#file.read()
flatten = lambda l: [item for sublist in l for item in sublist]
df = pd.DataFrame(flatten(results),columns=['Name','link to book'])
df.to_csv('books.csv', index=False, encoding='utf-8')

df = pd.read_csv("books.csv")
#pd.set_option("display.max_rows", None, "display.max_columns", None)
print(df)