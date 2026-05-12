import sqlite3

conn = sqlite3.connect("news_aggregator_data.db")
with open("dump.txt", "w", encoding="utf-8") as f:
    for line in conn.iterdump():
        f.write(line + "\n")