import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://talkpython.fm/episodes/transcript/118/serverless-software'

uReq(my_url)

#opening up connection, grabbing the page
uClient = uReq(my_url)

#saves client into a variable
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

# all of the page's html is now saved as page_soup