import re
raw_text  = "I recommend the testers at https://pythex.org and https://regex101.com. Different programming languages have slightly different regular expression syntax, so be sure to select the “Python” flavor on these websites."
#as of 2026-03-05 11:03:21.029531
#i do not know the regex string for "after https://, include everything until .{3 letters}"
pattern = re.compile(r"https://(.*?\.[a-zA-Z]{3})")
#ill try to explain this copy pasted solution as best as i can
#r"". to avoid escape character mess
# https:// a literal.
#(.*? match everything after the literal, \. literal dot using escape sequence
#[a-zA-Z]{3}, ensures 3 letters only. includes lowercase and uppercase

#matching pattern should be 'https://pythex.org', but we have parentheses [called capturing group] and .findall only includes those group in its list value







#update: quick search and i cracked it
found = pattern.findall(raw_text)
if found:
    print(found)
else:
    print("no matches")
