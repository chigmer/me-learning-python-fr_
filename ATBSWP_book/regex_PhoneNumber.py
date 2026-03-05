import re

phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}') 

match_obj = phone_num_pattern_obj.search('My number is 415-555-4242.')  

if match_obj:
    print(match_obj.group())
else:
    print("no matches")