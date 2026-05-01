import sys
import random
from time import sleep
from urllib.parse import urlparse, urljoin
from datetime import datetime

try:
    import requests
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    print("Error: this script uses third party modules:\nbs4\nrequests")
    sys.exit(1)

def check_link(session, url, headers):
    """Checks link status with exponential backoff for 429/5xx errors."""
    retries = 3
    base_backoff = 3
    dur = 0.000

    for i in range(retries):
        try:
            # HEAD is faster, but we follow redirects to check the final destination
            r = session.head(url, headers=headers, timeout=10, allow_redirects=True)
            duration = r.elapsed.total_seconds()
            dur = round(duration, 3)

            # Fallback to GET if HEAD isn't allowed
            if r.status_code == 405:
                r = session.get(url, headers=headers, timeout=10, stream=True, allow_redirects=True)
                duration = r.elapsed.total_seconds()
                dur = round(duration, 3)

            # Handle Rate Limiting
            if r.status_code == 429:
                sleep_time = (base_backoff * (2 ** i)) * random.uniform(0.8, 1.2)
                print(f"Rate limited on {url}. Backing off {sleep_time:.2f}s...")
                sleep(sleep_time)
                continue

            # Soft 404 Detection (Simple URL-based check)
            # If we asked for a page and ended up on an error-looking URL
            error_patterns = ['/404', '/error', '/not-found', '/search']
            if r.status_code == 200:
                if any(p in r.url.lower() for p in error_patterns) and any(p not in url.lower() for p in error_patterns):
                    return 404, dur  # Treat as Soft 404

            return r.status_code, dur
        except requests.exceptions.RequestException:
            return 0, dur

    return 429, dur

def make_delay():
    base = random.triangular(0.9, 2.9, 1.6)
    return round(base, 2)

def normalize_url(text: str) -> str | None:
    text = text.strip()
    if not text:
        return None
    if "://" not in text:
        text = "https://" + text
    p = urlparse(text)
    return text if p.netloc else None

def extract_links(soup, base_url) -> list[str]:
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if not href or href.startswith(("#", "javascript:", "mailto:", "tel:")):
            continue
        full_url = urljoin(base_url, href)
        parsed = urlparse(full_url)
        if parsed.scheme and parsed.netloc:
            links.append(full_url)
    return list(dict.fromkeys(links))

def extract_alias(url) -> str:
    domain = urlparse(url).netloc
    alias = domain.replace("www.", "").lower()
    return alias

def get_now_iso():
    """Returns the current local time in YYYY-MM-DD HH:MM:SS format."""
    # datetime.now() grabs the current system time
    now = datetime.now()

    # %Y = 4-digit year, %m = month, %d = day
    # %H = hour (24-hour), %M = minute, %S = second
    return now.strftime("%Y-%m-%d %H:%M:%S")

# Usage:
# print(get_now_iso())

def scan_target_URL(target: str, limit=None, offset=0) -> tuple[tuple,list[tuple] | None]:
    session = requests.Session()

    if limit is not None and not isinstance(limit, int):
        raise ValueError('invalid type for "limit"')
    if not isinstance(offset, int):
        raise ValueError('invalid type for "offset"')
    if offset < 0:
        raise ValueError("offset cannot be negative")

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux; x86_64) Chrome/123.0.0.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }

    link = normalize_url(target)
    if not link:
        print("Invalid URL")
        return None

    try:
        res = session.get(link, headers=headers, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        links = extract_links(soup, link)

        if not links:
            print("No links found.")
            sys.exit()

        print(f"Found {len(links)} unique links. Starting verification...\n")

        server_error_count = 0
        consecutive_403_count = 0
        url_data = []

        end = None if limit is None else offset + limit

        for url in links[offset:end]:
            url_current = []

            # Circuit Breaker: Stop if the server is clearly dying
            if server_error_count >= 5:
                #print("\n[!] Critical: Too many 5xx errors. Stopping.")
                break

            # Circuit Breaker: Stop if we are being blocked (403)
            if consecutive_403_count >= 5:
                #print("\n[!] Critical: Consecutive 403 Forbidden errors. We've been caught.")
                break

            sleep(make_delay())
            status, dur = check_link(session, url, headers)

            """url_data = {
"url": "https://www.google.com",
"alias": "Google Search",
"status_code": 200,
"is_active": 1,
"response_time": 0.154
}"""

            # 
            url_current.append(url)
            url_current.append(extract_alias(url))
            url_current.append(status)

            # ("https://www.google.com","Google",200,1,0.154)

            if status == 200 or (200 <= status < 400):
                print(f"[OK] {status} - {url}")
                server_error_count = 0
                consecutive_403_count = 0
                url_current.append(1)

                # working.append(f"OK: {url}")
            elif status == 404 or status == 410:
                print(f"[BROKEN] {status} - {url}")
                # broken.append(f"BROKEN: {url}")
                url_current.append(0)
                consecutive_403_count = 0
            elif status == 403:
                print(f"[FORBIDDEN] 403 - {url}")
                consecutive_403_count += 1
                url_current.append(1)
            elif 500 <= status < 600:
                print(f"[SERVER ERROR] {status} - {url}")
                server_error_count += 1
                url_current.append(0)
            else:
                print(f"[UNKNOWN/FAILED] {status} - {url}")
                url_current.append(0)

            url_current.append(dur)
            url_current.append(get_now_iso())

            url_data.append(tuple(url_current))
            parent_data = (link, get_now_iso())

        return parent_data,url_data  # The JUICE and PULP

    except Exception as e:
        print(f"Error: {e}")
        return None

reference = """
url (Text)
alias (Text)
status (Integer)
is_active (Integer)
dur (Real)
get_now_iso() (Text)
"""