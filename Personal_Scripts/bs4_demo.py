#not really a demo, just a test script

from bs4 import BeautifulSoup
from pathlib import Path
path = Path("Example_HTML")/ "example3.html"
with open(path) as file:
    example_html = file.read()
    
print(example_html)

soup = BeautifulSoup(example_html,"html.parser")
header = soup.select_one("body h1")
content = soup.select("body p")
link = soup.select_one("body p a")
img = soup.select("img[src]")
print("\n\n\n")
print(f"Title: {header.get_text()}\n")
for match in content:
    if len(match.get_text()) > 0:
        print(f"Text found: {match.get_text()}\n")

print("\n\n")
   
print(f"Link: {link['href']}")
for image in img:
    print(f"image found: {image['src']}")
"""<html> <head>                                              <title>Example Website Title</title> <style>               .slogan {                                                  color: gray; font-size: 2em;                               } </style>
</head> <body>
<h1>Example Website</h1>
<p>This &lt;p&gt; tag puts <b>content</b> into a <i>single</i> paragraph.</p> <p><a href ="https://inventwithpython.com">This text is a link</a> to books by <span id= "author">Al Sweigart</span>.</p>
<p><img src="wow_such_zophie_thumb.webp" alt="Close-up of my cat Zophie." /></p> <p class="slogan">Learn to program in Python!</p> <form>
<p><label>Username: <input id="login_user" placeholder="admin" /></label></p> <p><label>Password: <input id="login_pass" type="password" placeholder="swordfish" />
</form> </label></p>
<p><label>Agree to disagree: <input type="checkbox" /></label><input type="submit" value="Fake Button" /></p> </body> </html>




Title: Example Website




Link: https://inventwithpython.com
image: wow_such_zophie_thumb.webp

[Terminal session finished]"""