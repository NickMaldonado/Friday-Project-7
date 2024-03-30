import sqlite3

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect('users.db')

# Create a cursor object to execute SQL commands
c = conn.cursor()

# Create a table for storing user information
c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE,
                password TEXT
            )''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
