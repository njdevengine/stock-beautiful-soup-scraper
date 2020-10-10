from requests import get
from bs4 import BeautifulSoup as Soup
from time import sleep

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Referer': 'https://cssspritegenerator.com',
         'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
         'Accept-Encoding': 'none',
         'Accept-Language': 'en-US,en;q=0.8',
         'Connection': 'keep-alive'}
base = "https://www.example.com/?page="        
results = []
for i in range(1,11):
    my_url = base+str(i)
    url = my_url
    d = get(url, headers=hdr)
    soup = Soup(d.content, 'html.parser')
    results.append(soup)
    sleep(10)
