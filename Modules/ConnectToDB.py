import sqlite3

try:
    conn = sqlite3.connect('StockDB.db')
    cursor = conn.cursor()
except sqlite3.Error as sqlerror:
    print("Error !!!", sqlerror)
