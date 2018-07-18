import requests
from bs4 import BeautifulSoup
import csv
URL="https://www.values.com/inspirational-quotes"
r=requests.get(URL)
soup= BeautifulSoup(r.content,'html5lib')
#print(soup.prettify())
quotes=list()
table= soup.find('div',attrs={'id':'portfolio'})
for row in table.findAll('div',attrs={'class': 'portfolio-image'}):
    quote={}
    quote['url']= row.a['href']
    quote['image']= row.img['src']
    quote['lines']= row.img['alt']
    quotes.append(quote)

filename='inspirational_quotes.csv'
with open(filename,'w') as f:
    w=csv.DictWriter(f,['url','image','lines'])
    w.writeheader()
    for quote in quotes:
        w.writerow((quote))


#with urllib.request.urlopen('http://python.org/') as response:
#    html = response.read()
#    print(html)
