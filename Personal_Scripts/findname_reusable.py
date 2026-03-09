#match everything regex.
# (.*), . match everything except spaces tabs and newlines, * quantifier means zero or more of the preceding characters.
import re
def findname(text:str) -> list:
    namepattern = re.compile(r"First Name: (.*) Last Name: (.*)")
    return namepattern.findall(text)
    #no need for input validation and error handling, findall returns empty list automatically

if __name__ == "__main__":
    print(findname("First Name: Al Last Name: Sweigart"))
    
    #todo: accept dictionaries and/or list (havent checked either)
    #accept with different formatting(e.g. last name and first named swapped, exclude punctuation, etc.)
    #stress test with different inputs
    #i forgot the cause of the script returning a tuple, researching that too.
    
    #to github this goes