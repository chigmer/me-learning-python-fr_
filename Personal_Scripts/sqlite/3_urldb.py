"""Make Database using SQLite."""

import sqlite3
import test_url_and_return_data as d
conn = sqlite3.connect("seconddb_reference.db")
cur = conn.cursor()
dump = d.scan_target_URL("https://en.wikipedia.org/wiki/330_West_42nd_Street",limit = 20, offset = 60)
#ive yet to make a third arg that specifies the offset, will do it sometime ig
#print(dump)
#print(d.reference)
conn.execute("""CREATE TABLE IF NOT EXISTS url (url_id INTEGER PRIMARY KEY, url TEXT NOT NULL,alias TEXT,status_code INT, is_active INT,response_time REAL,last_checked TEXT) STRICT""")
cur.executemany("""
    INSERT INTO url (url, alias, status_code, is_active, response_time, last_checked)
    VALUES (?, ?, ?, ?, ?, ?)
""", dump)
conn.commit()
"""url (Text)                                                 �alias (Text)                                              status (Integer)                                           is_active (Integer)
dur (Real)
get_now_iso() (Text)"""
#make queries


#conn.execute("""CREATE TABLE IF NOT EXISTS url (url_id INTEGER PRIMARY KEY, url TEXT NOT NULL,alias TEXT,status_code INT, is_active INT,response_time REAL,last_checked TEXT) STRICT""")


conn.commit()