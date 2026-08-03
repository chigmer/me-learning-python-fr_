# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "aiohttp",
#     "beautifulsoup4", 
# ]
# ///
import fetch_links
import asyncio
import time
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys
import shelve
from pathlib import Path
from urllib.parse import urljoin
path  = Path(".fetched_links") / "fetched.json"
import aiohttp


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
          
#def parse_args() :
#    parser = argparse.ArgumentParser(
#        description="fetch website from user-supplied link, and extracts all URL's within the page")
 #   parser.add_argument("link",type=str,help = "your link")
  #  args = parser.parse_args()
  #  return args.link

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
          
async def fetch(link: str):
    link = normalize_url(link)
    if link is None:
        print("invalid URL")
        sys.exit()

    if not usage_limit():
        print("Error: too many requests")
        sys.exit(1)

    headers = {
          
    
    'User-Agent': 'Mozilla/5.0 (X11; Linux; x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    

    }  # same as before

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link, headers=headers, timeout=aiohttp.ClientTimeout(total=10)) as res:
                res.raise_for_status()
                text = await res.text()
                soup = BeautifulSoup(text, "html.parser")
                links = extract_links(soup, link)
                if links:
                    print("Links Found:\n----------")
                    for res_link in links:
                        print(res_link)
                        print("|")
                    print("------------")
                return links
    except Exception as e:
        print(f"Error: {e}")
        #sys.exit(1)

#immediately calls log(path), then calls decorator(main) (the return value of log(path))
async def async_main(*args):
    current_time = time.time()
    results = await asyncio.gather(
        *(fetch(link) for link in args)
    
    )
    print(f"results: {results}")
    time_elapsed = time.time() - current_time
    print(f"Time elapsed for asynchronous requests: {time_elapsed:.2f} seconds")
def synchronous_main(*links):
    total_time_elapsed = float(0)
    for link in links:
        data = fetch_links.main(link)  # Call the synchronous main function
        print(data)
        time_elapsed = fetch_links.main(link)[0]  # Get the time elapsed from the tuple returned by main
        total_time_elapsed += time_elapsed
    print(f"Total time elapsed for synchronous requests: {total_time_elapsed:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(async_main("https://google.com", "https://bing.com", "https://duckduckgo.com"))
    synchronous_main("https://google.com", "https://bing.com", "https://duckduckgo.com") # Call the synchronous main function after the asynchronous calls
    