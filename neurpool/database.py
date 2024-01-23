import sqlite3
from bs4 import BeautifulSoup
from datetime import datetime

# Assume 'numbers' is the list of numbers extracted using BeautifulSoup

# Create SQLite database and table
conn = sqlite3.connect('visitor_data.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS visitor_entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        percentage TEXT,
        pool_count INTEGER,
        aquapark_count INTEGER
    )
''')

# Insert data into the table
for entry in numbers:
    # Extracting percentage, pool count, and aquapark count from the list
    percentage, pool_count, aquapark_count = entry.split('%')[0], entry.split('(')[1].split(' ')[0], entry.split('(')[2].split(' ')[0]

    # Convert percentage and counts to appropriate data types
    percentage = float(percentage)
    pool_count = int(pool_count)
    aquapark_count = int(aquapark_count)

    # Insert data into the table
    cursor.execute('''
        INSERT INTO visitor_entries (percentage, pool_count, aquapark_count)
        VALUES (?, ?, ?)
    ''', (percentage, pool_count, aquapark_count))

# Commit the changes and close the connection
conn.commit()
conn.close()