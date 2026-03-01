import requests

url = "https://raw.githubusercontent.com/chigmer/me-learning-python-fr_/main/ATBSWP_book/chapter_7.py"

response = requests.get(url)

print(response.status_code)  # sanity check
print(response.text)
print(f"number of characters: {len(response.text)}")


#Web Fetch success!