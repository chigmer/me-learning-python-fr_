import re
pattern = re.compile(r'\bcat.*?\b')
print(pattern.findall('The cat found a catapult catalog in the catacombs.'))