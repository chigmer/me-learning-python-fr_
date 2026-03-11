#Find website URLs that begin with http:// or https://
#findLink.py
import re

def findlink(text:str) -> list:
    pattern = re.compile(r"""
    (?:https?://) #the 'trigger' word that catches most email (assuming the writer is competent and includes the protocols in the text) this is just v1 cut me some slack
    
    (?:[A-Za-z0-9-]+\.)+#domain
    
    (?:[a-z]{2,}) #top level domain
    
    (?:/[^\s]*)?#optional group, catches content after the previous group
    
    
        
        """,re.VERBOSE | re.IGNORECASE) #realized way too late that I couldve just made the entire thing case insensitive
    return pattern.findall(text)
    
    
if __name__ == "__main__":
    print(findlink("""
    
    1. Standard: https://www.google.com and http://python.org.
    hello I am just a bad writer.and I dont care
    starch.starch.pres.pres
    http://start.stop.step/python/ilovepython
    https://HiAlSweigart.co.com/python/hi.html



"""))
    
     
    
