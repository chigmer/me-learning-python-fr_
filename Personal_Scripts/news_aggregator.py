
#search news outlets, hardcoded for now and give me a polished feed of daily news
#use argparse for optional flags. would figure it out eventually
import argparse
import random
import newspaper
from newspaper import Article
import feedparser
import textwrap
import time
import requests
def make_delay():
    base = random.triangular(0.9, 2.9, 1.6)
    return round(base, 2)
def get_full_text(url):
    try:
        # Pass headers to avoid being blocked by simple scrapers
        config = newspaper.Config()
        config.browser_user_agent = 'Mozilla/5.0 (X11; Linux; x86_64) Chrome/123.0.0.0'
        config.request_timeout = 10

        article = Article(url, config=config)
        article.download()
        article.parse()
        
        if not article.text:
            return "[Extraction Failed: No text found. Might be a paywall.]"
        
        # Utilitarian formatting: Wrap the text so it fits the terminal nicely
        wrapper = textwrap.TextWrapper(width=80, initial_indent="    ", subsequent_indent="    ")
        return wrapper.fill(article.text)
    except Exception as e:
        return f"Failed to extract text: {e}"
        
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux; x86_64) Chrome/123.0.0.0'
}

def setup_args():
    parser = argparse.ArgumentParser(
        description="A news aggregator for someone living under a rock",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # Selection Logic
    targets = parser.add_mutually_exclusive_group()
    targets.add_argument("-o", "--outlets", nargs="+",
                        choices=['ap', 'reuters', 'bbc', 'npr', 'aljazeera', 'wsj', 'propublica'],
                        help="Specific sources to fetch")
                        
    targets.add_argument("--all", action="store_true", help="Fetch from every configured source")

    # Filter & Output
    parser.add_argument("-l", "--limit", type=int, default=3, help="Stories per source")
    # Format
    parser.add_argument("--mode", choices=['titles', 'brief', 'full'], default='brief',
                        help="Detail level: titles only, brief snippets, or full text (if possible)")
    
    # Utilities
    parser.add_argument("--browser", action="store_true", help="Open the top story of each source in your browser")
    
    #parser.add_argument("--database", action="store_true", help="Log these headlines to your SQLite archive")

    return parser.parse_args()
NEWS_FEEDS = {
    "ap": "https://rsshub.app/apnews/topics/apf-topnews",
    "reuters": "https://www.reutersagency.com/feed/",
    "bbc": "http://feeds.bbci.co.uk/news/rss.xml",
    "npr": "https://feeds.npr.org/1001/rss.xml",
    "aljazeera": "https://www.aljazeera.com/xml/rss/all.xml",
    "wsj": "https://feeds.a.dj.com/rss/RSSWorldNews.xml",
    "propublica": "https://feeds.propublica.org/propublica/main"
}

def fetch_xml(link):
    try:
    # Use a timeout (in seconds) so you don't hang for 5 minutes
        feedparser.USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        extra_headers = {
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com/' 
}
        res = feedparser.parse(link,request_headers=extra_headers)
  
    
    except Exception as e:
        #i do not know the exact error message for this one
        
        print(f"something broke: {e}")
        return None
    return res
def main():
    args = setup_args()
    if args.outlets:
        # Create a sub-dictionary of just the chosen outlets
        to_fetch = {k: NEWS_FEEDS[k] for k in args.outlets}
    elif args.all: 
        to_fetch = NEWS_FEEDS
    else:
        # Default fallback
        to_fetch = {"bbc": NEWS_FEEDS["bbc"], "npr": NEWS_FEEDS["npr"]}
    
    for outlet,URL in to_fetch.items():
        time.sleep(make_delay())
        print(f"fetching contents on {outlet.upper()}\n")
        xml = fetch_xml(URL)
        #quick check to see if if we got anything
        if not xml:
            print(f"couldnt find anything on {outlet}. skipping...")
            continue
                   
           
        else:
            if xml.status == 403:
                print(f"Forbidden from {outlet}. skipping")
                continue
            elif xml.status == 404:
                print(f"Resource from {outlet} is not found. skipping...")
                continue
            elif not hasattr(xml,"entries"):
                print(f"{outlet} has no entries, skipping.")
                continue
        xml.entries.sort(key=lambda x: x.get('published_parsed', 0), reverse=True)
        #copied this line above
        articles = []
        i = 1
        print(f"Lookup for {outlet} is successful.\n\n")
        time.sleep(1)
        #parser.add_argument("--mode", choices=['titles', 'brief', 'full'], default='brief',
                       
        for story in xml.entries[:args.limit]:
            timestamp = time.strftime("%Y-%m-%d %H:%M", story.published_parsed) if hasattr(story, 'published_parsed') else "N/A"
            print("—" * 35)
            print(f"\nHeadline {i}: {story.title}\n")
            print(f"Date: {timestamp}\n")
            i += 1
            print(f"Author: {story.get('author','Unknown')}\n\n")
            if not args.mode == 'titles':                      
                print(f"Summary:\n{story.get('summary','no summary available')}\n")
            if args.mode == "brief" or args.mode == "titles":
                print(f"Link: {story.get('link','no link available')}")
            
                continue
            elif args.mode == 'full':
                link = story.get("link",0)
                if link:
                    print("Fetching full article text... (patience is a virtue)")
                    time.sleep(make_delay())
                    full_text = get_full_text(story.link)
                # Just show the first 1000 characters so your terminal doesn't explode
                    if full_text:
                        print(f"Full Text:\n{full_text}") 
                else:
                    print("no link available")
            
           
        
            #would immediately fix if i see tags
        
            
                
                                        
                
            
    
    #-o = outlets
    #-l = limit
    #-q = query, just keywords is fine
    #--mode = either titles, brief, or full text
    #--browser, open in browser
    
    #LOG each one to the db
if __name__ == "__main__":
    main()

