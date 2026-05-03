import sqlite3

conn = sqlite3.connect("rps_data.db")
cur = conn.cursor()

# All sessions
cur.execute("SELECT * FROM sessions")
print("SESSIONS:")
for row in cur.fetchall():
    print(row)

print()

# All games
cur.execute("SELECT * FROM game")
print("GAMES:")
for row in cur.fetchall():
    print(row)

# Join both tables to see full picture
print("\nFULL VIEW:")
cur.execute("""
    SELECT s.source_id, s.winner, s.started_at, 
           g.game_number, g.player_won, g.computer_won
    FROM sessions s
    LEFT JOIN game g ON s.source_id = g.source_id
    ORDER BY s.source_id, g.game_number
""")
for row in cur.fetchall():
    print(row)

conn.close()