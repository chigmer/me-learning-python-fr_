"""
from Gemini 
PROJECT: Looter-CLI
GOAL: A defensive, CLI-based web-scraping utility.

FUNCTIONALITY:
1. Accept a target URL via argparse.
2. Spoof headers (User-Agent/Referer) to avoid immediate bot-detection.
3. Use BeautifulSoup to parse the HTML 'soup' for all <a> tags.
4. Filter links based on user-defined extensions (--ext pdf, zip, etc.).
5. Resolve relative paths using urllib.parse.urljoin.
6. Stream binary data to a dedicated local directory via pathlib.

STATUS: On hold until Chapter 12  is fully digested.
"""
