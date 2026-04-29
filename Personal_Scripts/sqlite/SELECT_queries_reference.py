"""SELECT QUERIES"""
q = """SELECT column, another_column, …
FROM mytable
WHERE condition(s)
ORDER BY column ASC/DESC
LIMIT num_limit OFFSET num_offset"""
if __name__ == "__main__":
    print(q)