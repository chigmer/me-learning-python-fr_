"""Practice Questions

1. What is the function that returns Regex objects? 2. Why are raw strings often used when creating Regex objects? 3. What does the search() method return?

4. How do you get the actual strings that match the pattern from a Match object?

5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?

6. Parentheses and periods have speciﬁc meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?

7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?

8. What does the | character signify in regular expressions? 9. What two things does the ? character signify in regular expressions?

10. What is the difference between the + and * characters in regular expressions?

11. What is the difference between {3} and {3,5} in regular expressions? 12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?

13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?

14. What is the difference between the .* and .*? regular expressions? 15. What is the character class syntax to match all numbers and lowercase letters?

16. How do you make a regular expression case-insensitive? 17. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?

18. If num_re = re.compile(r'\d+'), what will num_re.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?

19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?"""


"""

1. re.compile()
2. to avoid the mess of escape sequencing
3. a match object
4. use the group() function to get a value
5. r'(\d\d\d)-(\d\d\d-\d\d\d\d)
group 0 - full match
group 1 - area code (3 digits)
group 2 - phone num (3 digits + a hyphen + 4 digits)

6. use a backslash (\) to escape the character
7. if the regex object contains 0 or 1 capturing groups (non capturing groups exist btw), the list wouldnt be a list of tuples. if the regex object has 2 or more capturing groups, the list becomes a list of tuples
8. | is a pipe, matches one or the other, for example r'cat|dog'
9. ? can signify zero or one match, or the lazy/non-greedy version of a quantifier
10. + - one or more * - zero or more
11. {3}, 3 matches of a qualifier, {3, 5} a range of matches of a qualifier (eithet 3,4, or 5)
12. \d -decimal character (0-9), \w, word character (shorthand for [a-z0-9_]), \s is a literal space character, useful in character classes or verbose mode
13. the opposite of no. 12, e.g. NOT a decimal char, NOT a literal space
14. .* is a greedy quantifier, matches as much as it can, .*? is lazy and completes a whole match on the least amount of characters  (zero or more of ANY character which is literally a death sentence [in terms of match length] if youre not careful)
15. [a-z0-9] <- add some more characters here to match, special characters lose their special meanings inside too. except \s
16. re.IGNORECASE
17. the . character normally matches any character, for example ('A','a','€', ' ')
18. it would replace the decimal characters in the string to 'X'
19. ignores whitespace and newlines, useful for organized regex objects


"""