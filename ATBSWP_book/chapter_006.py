"""Practice Questions

1. What is []?

2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)

For the following three questions, assume spam contains the list ['a', 'b', 'c', 'd'].

3. What does spam[int(int('3' * 2) // 11)] evaluate to? 4. What does spam[-1] evaluate to? 5. What does spam[:2] evaluate to? For the following three questions, assume bacon contains the list [3.14, 'cat', 11, 'cat', True].

6. What does bacon.index('cat') evaluate to? 7. What does bacon.append(99) make the list value in bacon look like? 8. What does bacon.remove('cat') make the list value in bacon look like? 9. What are the operators for list concatenation and list replication?

10. What is the difference between the append() and insert() list methods? 11. What are two ways to remove values from a list? 12. Name a few ways that list values are similar to string values. 13. What is the difference between lists and tuples? 14. How do you write the tuple value that has just the integer value 42 in it? 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?

16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

17. What is the difference between copy.copy() and copy.deepcopy()?

Practice Programs

For practice, write programs to do the following tasks.

Comma Code

Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns

a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your func-tion should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.

136 Chapter 6"""

answers = """
1. [] is an empty list
2. spam.insert(2,'hello')
3. 'd'
4. 'd'
5. ['a','b']
6. 1, .index() shows only the first instance on the list
7.[3.14, 'cat', 11, 'cat', True, 99]
8. [3.14, 11, 'cat', True], remove deletes the first instance of 'cat'
9. + and *
10. .append() adds a value on the very last location of the list, .insert() offers more flexibility, allowing you to put it anywhere on the list (needs an index value)
11. remove and del
12. both are iterable, both can be sliced, both can be assigned to a variable, etc.
13. main difference: lists are mutable, tuples are immutable
14. 42, or (42,)
15. changing the [] brackets to a parentheses
16. a reference to the list value
17. copy.copy() is a shallow copy that generates another reference to the same list value, copy.deepcopy() is a copy that generates an entirely new list from the original list, its slower but safer

stay tuned for practice programs mwahahaha


"""

#comma code
# 99% sure that after I'm done, this'll be inefficient but working

def commatize(group: list) -> str:
    sentence = ""
    if not isinstance(group,list):
        raise TypeError("the input should be a list.")        
    if not len(group) > 0:
        raise ValueError("the list value should not be empty")
    
   
        
    for i in range(len(group) - 1):
        sentence += group[i]
        if not group[-1] == group[i]:
            sentence += ", "
    if len(group) != 1:
        sentence += f"and {group[-1]}"
    else:
        return group[0]

       
        
    return sentence
        
if __name__ == "__main__":
    print(commatize(['male','man','guy'])) 
    print(commatize(["eggs"]))   
    

      


