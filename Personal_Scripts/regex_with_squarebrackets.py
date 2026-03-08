import re

phone_num_pattern_obj = re.compile(r'[0-9]{3}-[0-9]{3}-[0-9]{4}') 

match_obj = phone_num_pattern_obj.search('My number is 415-555-4242.')  

if match_obj:
    print(match_obj.group())
else:
    print("no matches")