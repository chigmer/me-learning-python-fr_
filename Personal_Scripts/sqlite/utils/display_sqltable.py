import sqlite3
"""
display_sqltable

Utility for viewing SQLite tables in a readable way.

Provides a function to print full or partial table contents,
with optional column selection by index and optional column name display.
"""
#making these help messages incase I forget
    
def display_table(conn,table_name,column_indexes=None,display_column_names=False):
    """
    
    
    
    Print rows from a SQLite table.

    conn must be a sqlite3 connection object  
    table_name must be the name of an existing table in the database  

    column_indexes is optional and selects columns by position  
    if not provided, all columns are displayed  

    display_column_names shows the selected column names after output  

    Example usage:
        conn = sqlite3.connect('test.db')
        display_table(conn, 'articles')
        display_table(conn, 'articles', [0, 2, 4], True)
    """
    if not isinstance(conn, sqlite3.Connection): 
        raise TypeError(conn)
    elif not isinstance(table_name,str):
        raise TypeError("table name must be a string")
    if column_indexes is not None:
        if not isinstance(column_indexes, (list, tuple)):
            raise TypeError("column_indexes must be a list or tuple of ints")
        if not all(isinstance(i, int) for i in column_indexes):
            raise TypeError("column_indexes must contain only integers")

    cur = conn.cursor()
    cur.execute("""
        SELECT 1
        FROM sqlite_master
        WHERE type = 'table'
        AND name = ?
        LIMIT 1;
    """, (table_name,))
    
    if cur.fetchone() is None:
        raise ValueError(f"No table named: {table_name}")
    cur.execute(f"PRAGMA table_info({table_name})")
    columns = [row[1] for row in cur.fetchall()]
    if column_indexes is not None:
        selected_columns = []
        for i in column_indexes:
            if i < 0 or i >= len(columns):
                raise IndexError(f"Invalid column index: {i}")
            selected_columns.append(columns[i])
            
    else:
        selected_columns = columns
    
       
    column_query = ", ".join(selected_columns)
    
    cur.execute(f"SELECT {column_query} FROM {table_name};")
    for row in cur:
        print(f"{row}\n")
    if display_column_names:
        print(f"\nCOLUMNS:\n{column_query}")
        
if __name__== "__main__":
    from pathlib import Path
    path =  Path.cwd().resolve().parent.parent / "news_aggregator_data.db"
    
    #print(path)
    if path.exists() and path.is_file():
        
        conn = sqlite3.connect(path)
        display_table(conn,"articles",display_column_names=True,column_indexes=[1,2,3,7])
    #guid, outlet, title, author, link, published_at, captured_at, summary, full_content
         
    
    
 
