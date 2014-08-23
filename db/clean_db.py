import sqlite3
import os

os.remove('../foosball.db')

schema = open('schema.sql', 'r').read()
preload = open('preload.sql', 'r').read()
conn = sqlite3.connect('../foosball.db')
cursor = conn.cursor()
cursor.executescript(schema)
cursor.executescript(preload)
conn.commit()
cursor.close()
conn.close()
