#crypto.py, 
import argparse, requests
import sys


    
    


#
parser = argparse.ArgumentParser(description="Crypto price tracker")

# positional — required, accepts multiple values
parser.add_argument("coins", nargs='+',help="coin ids e.g. bitcoin ethereum")

# optional with value
parser.add_argument("--currency", default="usd", help="currency to convert to")


args = parser.parse_args()
#args.coins (list)
#args.currency
#args.verbose (boolean) #scrapped
def main():
    coins = args.coins
    currency = args.currency
    
    session = requests.Session()
    link = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(coins)}&vs_currencies={currency}"
    
    #make_delay()
    try:
        res = session.get(link, timeout=10)
        #no need for user agent
        res.raise_for_status()                   
        res = res.json()
        if not res:
           print(f"no results found with coin(s) {', '.join(coins)} on \"{currency}\"")
           sys.exit()
        #{'bitcoin': {'usd': 63681}}
        for coin, value_dict in res.items():
            
            
            
            print(f"{coin}: {value_dict[currency]} {currency.upper()}")
            
        
        #add actual display, but test if res returns anything
        
            
        
            
            
                
          
        
    except Exception as e:
        print(f"Error: {e}\n")
        sys.exit(1)
if __name__ == "__main__":
    main()
    #OUTPUT:
    """
    $ python crypto.py bitcoin,solana,ethereum
    bitcoin: 64021 USD
    ethereum: 1776.39 USD
    solana: 79.08 USD
    """
        