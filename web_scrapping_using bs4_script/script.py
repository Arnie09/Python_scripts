from bs4 import BeautifulSoup
import urllib.request
import re

string = '21.Jump.Street.2012.720p.BluRay.x264.YIFY'
url = 'https://www.google.com/search?q='
url2 = '+imdb&ie=UTF-8&oe=UTF-8'

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
req = opener.open(url+string+url2)
soup = BeautifulSoup(req)

soup.prettify()

links_for_movie = []
for link in soup.findAll('a'):
    links = link.get('href')
    if("imdb.com" in links):
        links_for_movie.append(links)

String = re.findall('https://www.imdb.com/title/[a-zA-Z0-9]+/',links_for_movie[0])

req = opener.open(String[0])
soup = BeautifulSoup(req)

print("Name: ",soup.find('h1').text.strip())

print("Year: ",re.findall('(\d\d\d\d)',soup.find('h1').text.strip())[0])

print("Rating: ",soup.findAll('span',{'itemprop':'ratingValue'})[0].text.strip())

print("Duration: ",soup.findAll('time',{'datetime':'PT109M'})[0].text.strip())

print("Genre and release date: ",end = " ")
for stuff in soup.findAll('div',{'class':'subtext'})[0].findAll('a'):
    strings = stuff.text.strip()
    print(strings,end = " ")

print()

print("Director/s: ",end = " ")
for stuff in soup.findAll('div',{'class':'credit_summary_item'})[0].findAll('a'):
    print(stuff.text.strip(),end = " ")

print()

req.close()