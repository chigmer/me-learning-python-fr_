"""
UPDATE: learned SELECT, FROM 
will use tb for display, im sick and tired of looking at lists of tuples and pretending THEYRE"""

import sqlite3
#import tabulate as tb

conn = sqlite3.connect("firstdb.db")
#make queries
#define cursor
cur = conn.cursor()
cur.execute("SELECT * FROM cats")
headers = [col[0] for col in cur.description]

cur.execute("SELECT * FROM cats")
data = cur.fetchall()


print(f"{headers}\n\n{data}")
#data is empty since i havent learned INSERT yet

#dont forget to commit, i advise against being lazy and autocommiting.

#conn.commit()