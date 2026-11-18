import sqlite3
from queue import Queue

pool = Queue(maxsize=2)

pool.put(sqlite3.connect("college.db"))
pool.put(sqlite3.connect("college.db"))

def get_connection():
    return pool.get()

def release_connection(conn):
    pool.put(conn)

conn = get_connection()
print("Database connection obtained")

release_connection(conn)
print("Database connection returned to pool")