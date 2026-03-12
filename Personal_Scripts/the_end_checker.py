#thought this was gonna be a cool idea
#check

import re
def is_end(text:str) -> bool:
    end_pattern = re.compile(r"""

(the[.\s]+end[.!?\s]*$) #accepts any character like punctuation or symbols as a fix
#special characters in a char class is unspecial, no need to escape


""", re.VERBOSE | re.IGNORECASE)
    match = end_pattern.search(text)
    if match:
        return match.group().strip(), match.start(), match.end()
    else:
        return 
if __name__ == "__main__":
    print(is_end(" Basically I said \"DID HE JUST SAY HIS LAST NAME WAS... BURGER?!?!. Does that come with fries??\"    The End... or is it?  Nah just messing with you THIS is the end.   "))
    #i have no idea how to display the location of where the match occurred
    #oh shit. i found an interesting result. is this because .* is greedy?
#update: Fixed it!! "." was WAY too broad





