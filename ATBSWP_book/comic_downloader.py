import requests
import os
from bs4 import BeautifulSoup
def crawl_xkcd(max_comics=5):
    url = 'https://xkcd.com'
    os.makedirs('xkcd_comics', exist_ok=True)
    
    comics_downloaded = 0
    
    while comics_downloaded < max_comics:
        print(f"[*] Fetching page: {url}")
        res = requests.get(url)
        res.raise_for_status()
        
       
        soup = BeautifulSoup(res.text, 'html.parser')
        
        
        # 1. FIND THE COMIC IMAGE
        # The image is inside a <div> with id="comic"
        comic_elem = soup.select_one('#comic img')
        
        if not comic_elem:
            print("[!] Could not find comic image.")
        else:
            
            comic_url = 'https:' + comic_elem.get('src')
            print(f"[+] Downloading image: {comic_url}")
            
            # 2. SAVE THE IMAGE, use iter_content() to iterate bytes 
            res_img = requests.get(comic_url)
            res_img.raise_for_status()
            
            filename = os.path.join('xkcd_comics', os.path.basename(comic_url))
            with open(filename, 'wb') as f:
                for chunk in res_img.iter_content(100000):
                    f.write(chunk)
            
            comics_downloaded += 1

        # 3. FIND THE PREVIOUS LINK
        # The 'Previous' button is an <a> tag with rel="prev"
        prev_link = soup.select_one('a[rel="prev"]')
        url = 'https://xkcd.com' + prev_link.get('href')
        # Termination logic: the first comic's "prev" link is "#"
        if prev_link.get('href') == '#':
            break

    print(f"\n[DONE] {comics_downloaded} comics saved to 'xkcd_comics' folder.")

if __name__ == "__main__":
    crawl_xkcd() # limit here, default=5
    """   The Content I scraped:
    
     <li>
     <a accesskey="p" href="/3235/" rel="prev">
      &lt; Prev
     </a>
    </li>
    <li>
     <a href="//c.xkcd.com/random/comic/">
      Random
     </a>
    </li>
    <li>
     <a accesskey="n" href="#" rel="next">
      Next &gt;
     </a>
    </li>
    <li>
     <a href="/">
      &gt;|
     </a>
    </li>
   </ul>
   <div id="comic">
    <img alt="Border Message" src="//imgs.xkcd.com/comics/border_message.png" srcset="//imgs.xkcd.com/comics/border_message_2x.png 2x" style="image-orientation:none" title="Thanks to differences in logging regulations, the messages actually turned out to be visible from the air."/>
"""
