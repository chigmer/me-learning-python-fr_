from pathlib import Path
from utils import display_sqltable as D
import sqlite3
from datetime import datetime
import sys
import time

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
    rows = cur.fetchall()
    if not rows:
        print(f"Nothing Available on {chosen_outlet}")
        sys.exit(0)
    for row in rows:
        print("–" * 35)   
        if row[2] and row[2] != "N/A":
    # do the datetime formatting
            dt = datetime.strptime(row[2][11:], "%H:%M")
            formatted_time = dt.strftime("%-I:%M %p") 
        else:
            formatted_time = "Unknown"     
               
        print(f"Title: {row[0]}\n\n{row[1]}\n\nPublished At: {row[2][:11]}{formatted_time}\n\n\n")
        
def main_2():
    """Count articles per outlet ✓
Find the most recently published article✓
Find articles where summary is longer than X characters✓
Find duplicate titles if any exist ✓"""
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT outlet FROM articles")
    outlets = [outlet[0] for outlet in cur] 
    print("\n\n") 
    article_count = []
    earliest = []
    oldest = []
    long_summaries = []
    duplicates = None
    
    for i in outlets:
        cur.execute("SELECT outlet,COUNT(title) FROM articles WHERE outlet = ?",(i,))
        article_count.append(cur.fetchall()[0])
        cur.execute("SELECT published_at,outlet,title,link FROM articles WHERE outlet = ? ORDER BY published_at DESC LIMIT 1",(i,))
        earliest.append(cur.fetchone())
        cur.execute("SELECT published_at,outlet,title,link FROM articles WHERE outlet = ? ORDER BY published_at LIMIT 1",(i,))
        oldest.append(cur.fetchone())
        cur.execute("SELECT outlet,COUNT(title),AVG(length(summary)) from articles WHERE outlet = ? AND length(summary) >= 180",(i,))
        #outlet,count of titles with long summaries,avg length of said long summaries
        data = cur.fetchone()
        if data[1] > 0:
            long_summaries.append(data)
    cur.execute("SELECT guid, COUNT(*),title FROM articles GROUP BY guid HAVING COUNT(*) > 1;")
    dupes = cur.fetchall()
    if dupes:
        duplicates = dupes[0]
    
    
    #Display:
    print("Displaying ARTICLE COUNT in each outlet\n\n\n")  
    print("—+" * 25)
    
    
    for i in article_count:
        print(f"Articles in {i[0].upper()}: {i[1]}")
        
    print("Displaying EARLIEST articles\n\n\n")
    print("—+" * 25)
    
    for i in earliest:
        print(f"{'_' * 40}\n\nearliest article in {i[1].upper()}:\n{i[2]}\n\npublished at: {i[0]}\n\n{i[3]}\n\n")
        
    print("Displaying OLDEST articles\n\n\n")
    print("—+" * 25)
    
    for i in oldest:
        print(f"{'_' * 40}\n\noldest article in {i[1].upper()}:\n{i[2]}\n\npublished at: {i[0]}\n\n{i[3]}\n\n")
    time.sleep(0.3)
    print("Displaying outlets whose articles have more than 180 character in its summaries!\n\n")
    print("—+" * 25)
    print()
    for i in long_summaries:
        #('wired', 1, 180.0)
        print(f"{i[0].upper()}: {i[1]} {'article' if i[1] == 1 else 'articles'}\nAverage length of valid summaries: {int(i[2])} chars\n")
    print("-+" * 20)
    if duplicates:
        #guid, COUNT(*),title
        for i in duplicates:
            print(f"\"{i[2]}\"\n{i[1]} identical articles\nID: {i[0]}")
    
        
            
        
  
        
   
   
if __name__ == "__main__":
    main()
    while True:
        choices = ['y','n']
        user = input("Would you like to view some fun facts about the archive? (y\\n)\n>").lower().strip()
        if not user in choices:
            print("invalid choice.")
            continue
        break
     
    if user == "y":
        main_2()