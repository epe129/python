import sqlite3

def lisaa():
    # Connect to the SQLite database
    conn = sqlite3.connect("local.db")
    c= conn.cursor()

    # Example: Create a table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            NAME TEXT NOT NULL,
            SALASANA TEXT NOT NULL,
            ID INTEGER NOT NULL
        )
    ''')

    c.execute("INSERT INTO users (NAME, SALASANA, ID) VALUES ('wqe', 'moi123', 1)")

    # Commit changes
    conn.commit()
    print("asd")
    # Close conn
    conn.close()

def katso():
    conn = sqlite3.connect('local.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")

    # Fetch all records
    rows = c.fetchall()
    print(rows)
    for row in rows:
        print(f"name: {row[0]}, s: {row[1]}, id: {row[2]}, ")
    print("moi")
    c.close()
