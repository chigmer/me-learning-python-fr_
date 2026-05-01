"""i now have data on my url table using INSERT,
i shall now display it using tabulate."""
import tabulate as tb
import sqlite3
conn = sqlite3.connect("seconddb_reference.db")
cur = conn.cursor()
cur.execute("PRAGMA table_info('url')")
columns = [column[1] for column in cur.fetchall()]
my_headers = tuple(columns)
cur.execute("SELECT * FROM url")
tabdata = cur.fetchall()

print(tb.tabulate(tabdata, headers=my_headers, tablefmt                ='simple'))
    

#conn.commit()