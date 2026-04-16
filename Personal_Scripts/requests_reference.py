import requests,sys

# 1. Create a session (persists cookies/headers)
session = requests.Session()

# 2. Define your Headers
# If I leave this out, 'requests' identifies itself as a bot, "python-requests"
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux; x86_64) Chrome/123.0.0.0'
}

# 3. The actual call
try:
    # Use a timeout (in seconds) so you don't hang for 5 minutes
    res = session.get('http://quotes.toscrape.com/', headers=headers, timeout=10)
    
   
    # If the page is 404 or 500, it throws an exception immediately.
    res.raise_for_status() 
    
    # raw HTML uses .text
    
except requests.exceptions.RequestException as e:
    print(f"something broke: {e}")
    sys.exit(1)
print(res.text)

"""
Breakdown:
    -make a session using requests.Session() #define it to a variable
    -important: make a header that seems real enough that youre human
    -within a try except block,call get() to your session (defined to something), headers=whatever_variable u put your headers in,timeout=int
    -call raise_for_status on sesh variable, exception when 4xx
    -finally use .text on the variable where get was called
    -IMPORTANT: make sure to be cautious for every get() call you make, randomize the interval for each request and make it reasonably long.
    -result you get unreadable garbage which is html
    -use BeautifulSoup to read it
    
    


"""