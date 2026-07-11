#crypto.py, 
import argparse, requests
import time,sys
import random

def make_delay():    
    time.sleep(round(random.triangular(1.5,2.5),3))
    return 
    
    


#
parser = argparse.ArgumentParser(description="Crypto price tracker")

# positional — required, accepts multiple values
parser.add_argument("coins", nargs="+", help="coin ids e.g. bitcoin ethereum")

# optional with value
parser.add_argument("--currency", default="usd", help="currency to convert to")

# flag
parser.add_argument("--verbose", action="store_true", help="show extra info")

args = parser.parse_args()
#args.coins (list)
#args.currency
#args.verbose (boolean)
def main():
    coins = args.coins
    currency = args.currency
    verbose = args.verbose
    session = requests.Session()
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux; x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}
    link = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(coins)}&vs_currencies={currency}{'&include_market_cap=true' if verbose else ''}"
    
    make_delay()
    try:
        res = session.get(link, headers=headers, timeout=10)
        res.raise_for_status()
        if not res:
            print(f"no results found with coin(s) {', '.join(coins)} on \"{currency}\"")
            
    except Exception as e:
        print(f"Error: {e}\n(probably an issue with your device)")
        sys.exit(1)
    
   
    

print(args.coins)     # ['bitcoin', 'ethereum']
print(args.currency)  # 'usd'
print(args.verbose)   # True or False