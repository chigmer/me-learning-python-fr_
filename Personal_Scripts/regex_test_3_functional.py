import re
raw_text  = "I was reading documentation⁠ and somehow ended up comparing https://python.org with https://developer.mozilla.org⁠ for no clear reason. Then I got distracted by a random article on https://medium.com⁠ about productivity, which of course linked to https://github.com⁠ repositories I absolutely did not need. At some point I checked https://stackoverflow.com⁠ for answers I could have reasoned out myself, and finally bookmarked https://realpython.com⁠ because pretending to be organized feels productive."
#as of 2026-03-05 11:03:21.029531
#i do not know the regex string for "after https://, include everything until .{3 letters}"
pattern = re.compile(r"https://(.*?\.[a-zA-Z]{3})")
#ill try to explain this copy pasted solution as best as i can
#r"". to avoid escape character mess
# https:// a literal.
#(.*? match everything after the literal, \. literal dot using escape sequence
#[a-zA-Z]{3}, ensures 3 letters only. includes lowercase and uppercase

#matching pattern should be 'https://pythex.org', but we have parentheses [called capturing group] and .findall only includes those group in its list value
#used lazy version

#bug found:to do, fix how the regex interprets the first and last part of the string
  






#update: quick search and i cracked it
found = pattern.findall(raw_text)
if found:
    print(found)
else:
    print("no matches")
