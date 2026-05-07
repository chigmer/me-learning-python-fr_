from pathlib import Path
#from utils import display_sqltable as D
import sqlite3
from datetime import datetime
import sys


#path = Path.cwd() / "utils"
#script = Path.cwd().parent / "display_sqltable.py"
#IT WORKS!!!1!1

data = Path.cwd().parent / "news_aggregator_data.db"
conn = sqlite3.connect(data)
#display_table(conn, table_name, column_indexes=None, display_column_names=False)
#D.display_table(conn,"articles",None,True)

def main():
    #guid, outlet, title, author, link, published_at, captured_at, summary, full_content
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT outlet FROM articles")
    outlets = [outlet[0] for outlet in cur]
    print("choose an outlet from:")
    for i in outlets:
        print(i.upper())
    while True:
        user = input(">").lower().strip()
        if not user in outlets:
            print("invalid outlet")
            continue
        break
    chosen_outlet = user.upper() #for display
    print(f"\nfetching data on {chosen_outlet}\n")
    cur.execute("SELECT title,summary,published_at FROM articles WHERE outlet = ? ",(user,))
    if not cur.fetchall():
        print(f"Nothing Available on {chosen_outlet}")
        sys.exit(0)
    for row in cur:
        print("–" * 35)   
        if row[2] and row[2] != "N/A":
    # do the datetime formatting
            dt = datetime.strptime(row[2][11:], "%H:%M")
            formatted_time = dt.strftime("%-I:%M %p") 
        else:
            formatted_time = "Unknown"     
               
        print(f"Title: {row[0]}\n\n{row[1]}\n\nPublished At: {row[2][:11]}{formatted_time}\n\n\n")
if __name__ == "__main__":
    main()   
        