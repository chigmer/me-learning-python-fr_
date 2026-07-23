import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from Personal_Scripts.fetch_links import main
from retry import retry
from log_func import log
#main('en.wikipedia.org')
#<function main at 0x7832ba4d60>


"""Actual Code!"""

@retry(3)
@log(".fetchedd")
def main_2(link: str):
    return main(link)
    
    
    
if __name__ == "__main__":    
    main_2("https://en.wikipedia.org/wiki/Melbourne")