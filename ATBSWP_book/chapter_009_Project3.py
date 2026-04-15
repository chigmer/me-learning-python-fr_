import re
#Project 3: Extract Contact Information from Large Documents
#I excluded the pyperclip lines. nice to have though.
#Create email regex.


email_re = re.compile(r'''

[a-zA-Z0-9._%+-]+  
@   
[a-zA-Z0-9.-]+
\.[a-zA-Z]{2,4}
#why does this code malfunction when i add parentheses? i just want groupinggg
'''
, re.VERBOSE)
# Create phone number regex.
phone_re = re.compile(r'''

( (\d{3}|\(\d{3}\))? 
(\s|-|\.)? 
(\d{3})  
(\s|-|\.)
(\d{4}) 
(\s*(ext|x|ext\.)\s*(\d{2,5}))? 
)

''', re.VERBOSE)#re.VERBOSE ignores whitespace or newlines

text = "myemail@yoohoo.com randomtextrandomtext. Hi Al Sweigart my phone number is 000-999-1234"
#sample text

matches = []
for groups in phone_re.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[6] != '':
        phone_num += ' x' + groups[6]
    matches.append(phone_num)
for groups in email_re.findall(text):
    matches.append(groups)
if matches:
    print("Matches found: ")
    for i in matches:
            
            print(i + "\n")
else:
    print("no matches found")
    #notifies the user whenever there are no matches