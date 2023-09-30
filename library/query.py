# Query the database
import sqlite3

def query_5_rows():
    conn = sqlite3.connect("titanic_passengersDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM titanic_passengersDB")
    print("Top 5 rows of the titanic_passengersDB table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"

def sum_survivors():
    conn = sqlite3.connect("titanic_passengersDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(Survived) FROM titanic_passengersDB")

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    total_sum = result[0]
    print("Total Survivors:", total_sum)