"""Practice Questions

1. Brieﬂy describe the differences between the webbrowser, requests, and bs4 modules.

2. What type of object is returned by requests.get()? How can you access the downloaded content as a string value?

3. What requests method checks that the download worked? 
4. How can you get the HTTP status code of a requests response? 
5. How do you save a requests response to a ﬁle? 
6. What two formats do most online APIs return their responses in? 
7. What is the keyboard shortcut for opening a browser’s Developer Tools? 
8. How can you view (in the Developer Tools) the HTML of a speciﬁc ele-ment on a web page?
9. What CSS selector string would ﬁnd the element with an id attribute of main?
10. What CSS selector string would ﬁnd the elements with an id attribute of highlight?
11. Say you have a Beautiful Soup Tag object stored in the variable spam for the element <div>Hello, world!</div>. How could you get a string 'Hello, world!' from the Tag object?
12. How would you store all the attributes of a Beautiful Soup Tag object in a variable named link_elem?
13-18. pass, I'll learn those another time when I actually need them"""

"""
1.webbrowser–able to open a window on your default browser on a given valid URL
requests–3rd party module that handles seamless html extraction from links
bs4–3rd party module that can parse messy language like html that the user can extract specific content from easily
2. used code and its 'requests.models.Response'
3. raise_for_status() raises an error if the download didnt work
4. status_code(), you get a 3 digit number that can have different meanings

5. use open() with mode wb to preserve binary stuff
6. json and xml
7. F12 / ctrl + shift + I
8. click the element in the webpage while devtools is on
9. '#main' 
10. '#highlight'
11. get_text() method
12. link_elem = some_tag.attrs(), assuming some_tag is a BS tag obj, link_elem will be a dictionary containing all attributes


"""