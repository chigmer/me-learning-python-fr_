import requests
import sys
from bs4 import BeautifulSoup

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux; x86_64) Chrome/123.0.0.0'
}

try:
   
    res = session.get('https://forecast.weather.gov/MapClick.php?lon=-122.395&lat=37.789', headers=headers, timeout=10)
    
   
    # If the page is 404 or 500, it throws an exception immediately.
    res.raise_for_status() 
    
    # raw HTML uses .text
    
except requests.exceptions.RequestException as e:
    print(f"something broke: {e}")
    sys.exit(1)
html = res.text
#print(html)
#target content is "detailed forecast and its contents"
soup = BeautifulSoup(html,"html.parser")
title = soup.select_one("title")
elems = soup.select('#seven-day-forecast-container')
news_header = soup.select("#news-items #topnews h1")
news_content = soup.select("#news-items #topnews p")

"""UNFINISHEDDD"""
#if elems:
   # for elem in elems:
   #     print(f'{elem.get_text()}')
        #print("|")
        
#else:
#    print("no links found")
 
print(f"Current News:\n{news_header}\n{news_content}")    

