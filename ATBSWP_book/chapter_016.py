"""
for me in the future:
    
    its currently May 11, 2026. Ive made a news aggregator recently. That's all.
    
    
    """
    
"""Practice Questions

1. What Python instructions will obtain a Connection object for a SQLite database in a ﬁle named example.db?

2. What Python instruction will create a new table named students with

TEXT columns named first_name, last_name, and favorite_color?

3. How do you connect to a SQLite database in autocommit mode? 

4. What’s the difference between the INTEGER and REAL data types in SQLite?

5. What does strict mode add to a table? 

6. What does the * in the query 'SELECT * FROM cats' mean? 

7. What does CRUD stand for? 

8. What does ACID stand for? 

9. What query adds new records to a table?

10. What query deletes records from a table? 

11. What happens if you don’t specify the WHERE clause in an UPDATE query? 

12. What is an index? What code would create an index for a column named birthdate in a table named cats?

13. What is a foreign key? 

14. How can you delete a table named cats? 

15. What “ﬁlename” do you specify to create an in-memory database? 

16. How can you copy a database to another database?"""

"""
1. connect() from the sqlite3 module, if you wish to obtain the db 'example.db', you pass it as an arg and usually, store it in a variable
connection = sqlite3.connect('example.db') #creates if it doesnt exist
2. CREATE TABLE IF NOT EXISTS students (first_name TEXT, last_name TEXT, favorite_color TEXT)
#technically, IF NOT EXISTS isnt related in creating a table, but its common practice to leave it there to prevent errors if the table exists already
3. oof. i wouldnt do this, but if i would, i would do sqlite3.connect('ex.db',isolation_level=None)
4. integer can be compared to python datatype int, and REAL can be compared to float, ones a whole number, ones a decimal with a dec. point
5. raises an error if a piece of data inserted to a column is of the wrong type
6. every column available
7. Create, Read, Update, Delete
8. no idea, but i vaguely remember that its used for ensuring data is either completely written or not written
9. INSERT
10. DELETE
11. every row gets updated, the WHERE clause is practically mandatory unless you wish to rewrite the entire table
12. improves SELECT queries by creating a faster path for a specific column (googled what an index is cuz i didnt use it even ONCE in my projects),CREATE INDEX index_name ON cats (birthdate);
13. a relational value to connect one row to another table row, used by JOIN
14. DROP TABLE cats (i like the implication that you literally just drop the table onto the ground)
15. :memory:, stored on.. you guessed it, system memory
16. call the method iterdump() on the connection object, open a file with open(), and iterate the connection inside of it. this 'should' recreate the different sql queries to CRUD the table.




 """