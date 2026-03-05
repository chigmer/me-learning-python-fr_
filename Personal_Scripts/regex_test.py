import re
pattern_obj = re.compile(r"\d{3}-\d{3}-\d{4}")

print(pattern_obj.search('My number is 415-555-4242.').group())
#what is .group() for? ill search it ig
