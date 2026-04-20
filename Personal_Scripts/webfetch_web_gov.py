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
news_header = soup.select_one("#news-items #topnews h1")
news_content = soup.select_one("#news-items #topnews p")
"""UNFINISHEDDD"""

#print(f"Current News:\n{news_header.get_text()}\n{news_content.get_text()}\n\n\n")  
#print(soup.prettify())  
#tr td b
location = soup.select_one("h2.panel-title")
if location:
    location = location.get_text()
else:
    location = "???"
table = soup.find("table")
table_info = {}
for row in table.find_all("tr"):
    current_label = row.select_one("td.text-right > b")
    current_value = row.select_one("td + td")
    if current_label and current_value:
        
        table_info[current_label.get_text(strip=True)] = current_value.get_text(strip=True)
print(f"Current Conditions at {location}")   
i=0
for k,v in table_info.items():
    print(f"{k}: {v}")
    if v in ("NA","NA NA MPH"):
        i += 1
if i >= 3:
    print("Apologies if weather.gov is so unhelpful")
    
#1st td- Label
#2nd td- Value

#upcoming task, use argparse to specify zipcode, raise Error if invalid zipcode. publishing to git :O
"""<table>                                                     <tr>                                                        <td class="text-right">                                     <b>                                                         Humidity
   </b>
  </td>
  <td>
   54%
  </td>
 </tr>
 
 <tr>
  <td class="text-right">
   <b>
    Wind Speed
   </b>
  </td>
  <td>
   NA NA MPH
  </td>
 </tr>
 
 <tr>
  <td class="text-right">
   <b>
    Barometer
   </b>
  </td>
  <td>
   NA
  </td>
 </tr>
 <tr>
  <td class="text-right">
   <b>
    Dewpoint
   </b>
  </td>
  <td>
   38°F (3°C)
  </td>
 </tr>
 <tr>
  <td class="text-right">
   <b>
    Visibility
   </b>
  </td>
  <td>
   NA
  </td>
 </tr>
 <tr>
  <td class="text-right">
   <b>
    Last update
   </b>
  </td>
  <td>
   20 Apr 03:43 AM PDT
  </td>
 </tr>
</table>


[Terminal session finished]"""
