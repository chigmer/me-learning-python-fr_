"""Make Database using SQLite."""
"""currently, i only know about defining columns, im not that far on the book"""
import sqlite3

conn = sqlite3.connect("firstdb.db")
#make queries
#make table, define column inside parentheses via column_name DATATYPE
conn.execute("""CREATE TABLE IF NOT EXISTS cats (name TEXT NOT NULL,birthdate TEXT,fur TEXT, personality TEXT,weight_kg REAL) STRICT""")
#NOT NULL ensures name is not None (basically mandatory)
#TEXT means string, REAL means float
#strict ensures type enforcing (throws exceptions)

"""types:
    TEXT
    NULL
    INT
    REAL
    BLOB (bytes)"""
#dont forget to commit

conn.commit()