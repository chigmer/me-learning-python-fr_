import sqlite3
import test_url_and_return_data as d
import tabulate as tb
#help(tb.tabulate)
#tabulate(tabular_data, headers=(), tablefmt                ='simple', floatfmt='g', intfmt='', numalign='default', stralign='default', missingval='', showindex='default', disable_numparse=False, colglobalalign=None, colalign=None, preserve_whitespace=False, maxcolwidths=None, headersglobalalign=None, headersalign=None, rowalign=None, maxheadercolwidths=None, break_long_words=True, break_on_hyphens=True)
#display multiple tables. child_url + their info


HEADERS = [
    "root_url", "url_id", "url", "status_code", 
    "is_active", "response_time", "last_checked"
]

# The Column String for your SELECT statement
COLS = """
    url.url_id, 
    url.url, 
    url.status_code, 
    url.is_active, 
    url.response_time, 
    url.last_checked
"""#url.source_id #​crawled_sites.source_id
def main(db_name="seconddb_reference.db"):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    #id 0, root 1, time 2, 
    cur.execute("SELECT source_id, root_url, scanned_at FROM crawled_sites")
    root_list = cur.fetchall()
    
    
    i = 0
    for root in root_list:
        i += 1
        print(f"{i}. Scanned: {root[1]} on {root[2]}\n\n")
        cur.execute(f"""SELECT {COLS} FROM crawled_sites JOIN url ON crawled_sites.source_id = url.source_id WHERE crawled_sites.source_id = ? """,(root[0],)) 
        
        #should get a list of tuples if i use fetchall()
        
        table_data = cur.fetchall()
        HEADERS = [
    "url_id", "url", "status_code", 
    "is_active", "response_time", "last_checked"]
        print(tb.tabulate(table_data, headers=HEADERS, tablefmt='simple'))
        print("\n\n")
        

        
        
    
    
main()   

