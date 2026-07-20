#task: find all links within a given html script, use argparse to provide link, auto complete with set
import requests
from bs4 import BeautifulSoup
import argparse
from urllib.parse import urlparse
import sys
import shelve
from pathlib import Path
import time
from urllib.parse import urljoin
import json
#decorator task: make a CRUD decorator (only add becau)
path  = Path(".fetched_links") / "fetched.json"
def log(path):
    #runs on @log(path), returns decorator  
    def decorator(func):
        
        #decorator is the return value of log(path), a function that accepts another function
        #basically (log(path))(main)
        def wrapper(): 
        #finally, this function is returned by decorator(main) 
        #replaces the original function with this, logs stuff + runs the original function          
            path.parent.mkdir(exist_ok=True)
            data = func()
            if not data:
                return                  
            with open(path,"w") as f:
                data = tuple(data)
                json.dump(data, f, indent=4)       
        return wrapper
    return decorator
    
    
    
        
            
          
                
        
    
def extract_links(soup, base_url) -> list[str]:
    links = []

    for a in soup.find_all("a", href=True):
        href = a["href"].strip()

        if not href:
            continue
        if href.startswith("#"):
            continue
        if href.lower().startswith(("javascript:", "mailto:", "tel:")):
            continue

        full_url = urljoin(base_url, href)
        parsed = urlparse(full_url)

        if not parsed.scheme:
            continue
        if not parsed.netloc:
            continue

        links.append(full_url)

    return list(dict.fromkeys(links))  # dedupe + preserve order
    
        #copied most of these from ChatGPT, i dont want to deal with url headaches, and i dont want to deal with reading docs headaches
        #i still understand the logic tho
def normalize_url(text: str) -> str | None:
    text = text.strip()

    if not text:
        return None

    # add scheme if missing
    if "://" not in text:
        text = "https://" + text

    p = urlparse(text)

    if not p.netloc:
        return None

    return text
          
def parse_args() :
    parser = argparse.ArgumentParser(
        description="fetch website from user-supplied link, and extracts all URL's within the page")
    parser.add_argument("link",type=str,help = "your link")
    args = parser.parse_args()
    return args.link

def usage_limit():
    data_dir = Path(__file__).resolve().parent / ".indexdataOWM"
    data_dir.mkdir(parents=True, exist_ok=True)  # add this line
    db_path = data_dir / "call_stats"
    with shelve.open(str(db_path)) as db:
        # rest of function unchanged
        current_call = time.time()
        calls = db.get("call_list",[])
        calls = [c for c in calls if (current_call - c) < 45]
        if len(calls) >= 30: 
            return False 
        
        calls.append(current_call)
        db["call_list"] = calls 
        return True       
@log(path)    
#immediately calls log(path), then calls decorator(main) (the return value of log(path))
def main():
    session = requests.Session()
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux; x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    
}
    link = parse_args()
    #uncommet for testing
    #link ='https://wikipedia.org'
    link = normalize_url(link)
    if link is None:
        print("invalid URL")
        sys.exit()

    try:
        if usage_limit():
        
            res = session.get(link, headers=headers, timeout=10)
            res.raise_for_status()
            soup = BeautifulSoup(res.text,"html.parser")
            #makes a tree (yay)
            links = extract_links(soup,link)
            if links:
                print("Links Found:\n----------")
                for res_link in links:
                    print(res_link)
                    print("|")
                print("------------")
            return links
                    
            
        else:
            print("Error: too many requests")
            sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    
   
    
if __name__ == "__main__":
    main()