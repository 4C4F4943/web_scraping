from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import urllib
import pandas as pd
from urllib.request import urlopen

from tqdm import trange

def tiny_url(url):
    apiurl = "http://tinyurl.com/api-create.php?url="
    tinyurl = urllib.request.urlopen(apiurl + url).read()
    return tinyurl.decode("utf-8")


class scrape():
  def __init__(self,url1,in_what,what_find):
    self.url1 = url1
    self.in_what = in_what
    self.what_find = what_find
    #print(self.what_find[0][0],",attrs=",self.what_find[0][1])
  def fetch_data(self):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    #print(self.url1)
    r = requests.get(self.url1)
    content = r.content
    soup = BeautifulSoup(content, features="html.parser")
    all1 = []
    #print(soup)
    #print(self.in_what[0],"attrs=",self.in_what[1])
    for d in soup.findAll(self.in_what[0],attrs=self.in_what[1]):
      #print("this is d: ",d)
      all2 = []
      for i in range(len(self.what_find)):
        #print(self.what_find[i][0],"attrs=",self.what_find[i][1])
        found = d.find(self.what_find[i][0],self.what_find[i][1])
                #print("this is found",found)
        all2.append(found)
      all1.append(all2)
    return all1
outp = []
how_many = 3
for z in range(1,how_many):
  this = scrape("https://lib.ugent.be/en/catalog?page="+str(z)+"&q=machine+learning",

  ["article",{'class':'col-md-12 search-result'}],

  [["h2",{"class":"search-result__title meta-title"}],
  ["span",{"class":"meta-type"}],
  ["small",{"class":"help-block text-center"}]],)
  test= this.fetch_data()
  #print("this is test: \n\n",test[:3])
  
  #print(len(test))
  for i in (t:=trange(len(test))):
    t.set_description("the page %.2f in the page %.2f"%(z,i))
    tm = []
    
    for j in range(len(test[i])):
      if j == 0:
        inb = test[i][j].a.text.strip().replace("\n","")
        url1 = "https://lib.ugent.be/"+test[i][j].a["href"]
        url2 = tiny_url(url1)
        tm.append(inb)
        tm.append(url2)
      elif j == 2:
        #print(test[i][j].text)
        #exit()
        try:
          inb = test[i][j].text.strip().replace("\n","")
          #print("this in inb: ",inb)
          tm.append("i CAN'T read it:(")
        except:
          tm.append("i can read it:)")
      else:
        inb = test[i][j].text.strip().replace("\n","")
        tm.append(inb)
    outp.append(tm)

for i in range(len(outp)):
  if outp[i][-1] != "i CAN'T read it:(":
    print(outp[i])

