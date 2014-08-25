import sqlite3
import os

def clean():
    if os.path.isfile('foosball.db'):
        print("deleting database file")
        os.remove('foosball.db')
    print("creating db connection")
    conn = sqlite3.connect('foosball.db')
    print("loading schema")
    schema = open('db/schema.sql', 'r').read()
    print("loading sample data")
    preload = open('db/preload.sql', 'r').read()
    cursor = conn.cursor()
    print("executing schema")
    cursor.executescript(schema)
    print("executing sample data")
    cursor.executescript(preload)
    print("closing connection")
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    clean()
