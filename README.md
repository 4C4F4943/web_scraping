# Annoying university website...

So here i was just finding out the universities library was open for not students. So of course i went and got myself a memberships card. But there was one really annoying thing.

They had some books that you could only read if you where studying at the college and practically all the books i want to read are "UGent only". 
But i was tired of scrolling through almost endless amounts of pages so i made this a generic webscraping thingy... Because don't we all love automating a thing that takes 10 minutes.

My result looks something like this:
<pre>
                                                Name                  link to book
0                Machine Learning and Biometrics      https://tinyurl.com/y5h3ryjg
1                      Lifelong machine learning      https://tinyurl.com/y4may3fy
2         Automated Machine Learning Methods, Sys...  https://tinyurl.com/y2m9d2sc
3         Flood Forecasting Using Machine Learnin...  https://tinyurl.com/y6k5usm9
4               Introduction to machine learning      https://tinyurl.com/y3uslk5d
5         Machine Learning With Radiation Oncolog...  https://tinyurl.com/yxl8d94y
6         Machine Learning - Advanced Techniques ...  https://tinyurl.com/y54j8l5q
7         Claim Models: Granular Forms and Machin...  https://tinyurl.com/y4xxkrra
8                   Machine learning for dummies      https://tinyurl.com/y6jpxwt9
</pre>
## further usage
If you want to use it for another website change this url. If youre website doesn,t have multiple pages then you do not need to use the pagenumber thing. 
You can just use 1 url.

```python
WITH_PAGES = requests.get("https://YOURE_URL.com/PAGE="+str(pageNo)+"THE_REST_OF_THE_URL")
WITHOUT_PAGES = requests.get("https://YOURE_URL.com")

```
But still very nice of the university to make a big part of their library public.
