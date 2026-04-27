from bs4 import BeautifulSoup
import requests
import argparse
import sys
import os
from datetime import datetime

"""Flickr downloader."""
#use argparse for search
#show number of results
#save to hidden dir (gitignore it too)
#


def download_flickr_image(url):
    folder = ".flickr_images"
    os.makedirs(folder, exist_ok=True)
    
    date_str = datetime.now().strftime("%m-%d-%Y_%H%M%S")
    ext = url.split('.')[-1].split('?')[0]
    filename = os.path.join(folder, f"{date_str}.{ext}")
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
        res = requests.get(url, stream=True, headers=headers, timeout=10)
        
        if res.status_code != 200:
            return False
            
        with open(filename, 'wb') as f:
            for chunk in res.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
        
        return True

    except Exception:
        return False
         
def parse_args():
    parser = argparse.ArgumentParser(
        description="Download images from Flickr"
    )
    parser.add_argument("term",type=str,help="search term to browse for a category of pics.")  
    parser.add_argument("-l","--limit",type=int,default=3,help="the amount of results the script displays")
    
    
    args = parser.parse_args()
    if args.limit >= 25:
        print("too many images. i refuse to cooperate any longer.")
        sys.exit(1)
        
    
    return args.term,args.limit
   
        
              
    
def extract_images(soup,limit:int):
    title = soup.find("title")
    images = soup.select("img[src*='staticflickr.com']")

    img_links = []
    if len(images) < limit:
        limit = len(images)
        print(f"only found {len(images)} results. ")
    else:
        print(f"found {len(images)} results.")
        #i completely forgot abt this
        
    for tag in images[:limit]:
        img_url = tag.get("src")
        if not img_url:
            continue
        if img_url.endswith('.svg') or '.svg?' in img_url:
            continue
        else:
            if img_url.startswith("//"):
                img_url = f"https:{img_url}"
            elif not img_url.startswith("http"):
  
                img_url = f"https://www.flickr.com{img_url}"
        img_links.append(img_url)

        #protocol was always cut off from the html for some reason
    return title,img_links
def main():
    session = requests.Session()
    term,limit = parse_args()
    term = term.strip().lower()
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux; x86_64) Chrome/123.0.0.0'
}
    try:
   
        res = session.get(f'https://www.flickr.com/search/?text={term.replace(" ","+").strip("+")}', headers=headers, timeout=10) 
    
   
    #
        res.raise_for_status() 
    
    # 
    
    except requests.exceptions.RequestException as e:
        print(f"something broke: {e}")
        sys.exit(1)
    soup = BeautifulSoup(res.text,"html.parser")
    title,img_links = extract_images(soup,limit)
    
    if not img_links:
        print(f"Error: No images found for '{term}'. Try searching for something that actually exists.")
        sys.exit()
    """downloading the pictures"""
    print(title.get_text())
    print("\n\n")
    while True:
        choice = input("Do you wish to proceed in downloading the images? (y/n)\n>").lower().strip()
        if choice == "y":
            break
        elif choice == "n":
            sys.exit()
        else:
            print(f"invalid response: {choice}")
    for img_url in img_links:
        status = download_flickr_image(img_url)
        if not status:
            print("error in creating image. skipping")
                        
    print("Process completed.\ncheck directory '.flickr_images' ")
    #return error if no matches
if __name__ == "__main__":
    # Ensure git doesn't track the hoard   
    main()