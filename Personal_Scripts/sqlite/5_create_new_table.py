import sqlite3
import test_url_and_return_data as d

conn = sqlite3.connect("seconddb_reference.db")
cur = conn.cursor()

# Setup tables first (The "Skeleton")
cur.execute("""
CREATE TABLE IF NOT EXISTS crawled_sites(
    source_id INTEGER PRIMARY KEY,
    root_url TEXT UNIQUE,
    scanned_at TEXT
) STRICT
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS url (
    url_id INTEGER PRIMARY KEY,
    source_id INTEGER, 
    url TEXT NOT NULL,
    alias TEXT,
    status_code INT, 
    is_active INT,
    response_time REAL,
    last_checked TEXT,
    FOREIGN KEY(source_id) REFERENCES crawled_sites(source_id)
) STRICT
""")

prepared_links = ['https://en.wikipedia.org/wiki/Crusading_movement', 'https://en.wikipedia.org/wiki/North_Africa', 'https://en.wikipedia.org/wiki/Lok_Ma_Chau_station', 'https://en.wikipedia.org/wiki/Fiat_Turbina', 'https://en.wikipedia.org/wiki/Water', 'https://en.wikipedia.org/wiki/James_Blair_(MP)']

# The "Heart" of the script
for link in prepared_links:
    parent_data, dump = d.scan_target_URL(link, limit=20, offset=60)
    
    if parent_data and dump:
        # 1. Insert the parent (or ignore if it exists)
        cur.execute("INSERT OR IGNORE INTO crawled_sites (root_url, scanned_at) VALUES (?, ?)", parent_data)
        
        # 2. Find the ID (whether it was just created or already existed)
        cur.execute("SELECT source_id FROM crawled_sites WHERE root_url = ?", (parent_data[0],))
        actual_source_id = cur.fetchone()[0]
        #condition: root_url has a value of parent_data[0], no its forbidden to use f strings

        # 3. Stitch the ID to every child link
        final_dump = [(actual_source_id,) + row for row in dump]
        #couldve used insert() but gemini used this instead

        # 4. Bulk insert the children
        cur.executemany("""
            INSERT INTO url (source_id, url, alias, status_code, is_active, response_time, last_checked)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, final_dump)

        # Commit after each site so you don't lose data if it crashes
        conn.commit()
        print(f"Finished hoarding data from: {link}")

print("All crawls complete. The database is now properly populated and ready for a JOIN.")


"TODO: display my beautiful data using tabulate."
