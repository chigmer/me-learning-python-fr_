#script only makes one request per run. so no rate limiter needed
#update: so pypi increased security, so i switched to wikipedia instead
import webbrowser
import argparse
import sys
try:
    from bs4 import BeautifulSoup
    import requests
except ModuleNotFoundError:
    print("this script uses:\nBeautiful Soup\nrequests\nensure that they're installed")
def parse_args() -> tuple:
    parser = argparse.ArgumentParser(description="A tool to search the PyPi database")
    parser.add_argument("term", type=str,nargs="+", help="your search term")
    parser.add_argument("-r","--results",type=int,default=3,help="the amount of results the script displays")
    args = parser.parse_args()
    return args.term, args.results
#https://pypi.org/search/?q=python
#https://pypi.org/project/python-rd-python-gitlab/  
  
    
def main():
    term,tabs=parse_args()
    #need to make an if statement if user does "term term" (crashes btw)
   
    url = f"https://en.wikipedia.org/w/index.php?search={'+'.join(term)}"


    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux; x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}

    try:
        res = requests.get(url,headers=headers, timeout=10)
    
   
        res.raise_for_status() 
        soup = BeautifulSoup(res.text,"html.parser")
    
        invalid = soup.select_one("p.mw-search-nonefound")
        if invalid:
            print(f"no search results for {" ".join(term)}.")
            sys.exit()
       
        results = soup.find_all('div', class_='mw-search-result-heading')
        print(f"found {len(results)} results.")
        for result in results[:tabs]:  
            link_tag = res.find('a')
            if link_tag:
        # Get the 'href' value
                path = link_tag.get('href')
        
        # Wikipedia gives relative paths 
                full_url = f"https://en.wikipedia.org{path}"
                webbrowser.open(full_url,new=1)
        
            
        

        
        
        
     
        #print(soup.prettify())
    
    # raw HTML uses .text
    except requests.exceptions.RequestException as e:
        print(f"something broke: {e}")
        sys.exit(1)
    
    
if __name__ == "__main__":
    main()
  