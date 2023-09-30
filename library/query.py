# Query the database
import sqlite3

def create_CRUD(data):
    dataset = "titanic_passengersDB"
    table_name = "titanic"
    
    conn = sqlite3.connect(dataset)
    cursor = conn.cursor()

    query = f"INSERT INTO {table_name} VALUES (? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(query, data)

    conn.commit()

def read_CRUD():
    dataset = "titanic_passengersDB"
    table_name = "titanic"

    conn = sqlite3.connect(dataset)
    cursor = conn.cursor()

    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

def update_CRUD(record_id, column_name, new_value):
    dataset = "titanic_passengersDB"
    table_name = "titanic"

    conn = sqlite3.connect(dataset)
    cursor = conn.cursor()

    query = f"UPDATE {table_name} SET {column_name} = ? WHERE id = ?"  # 예시 쿼리
    cursor.execute(query, (new_value, record_id))
    
    conn.commit()

    cursor.close()
    conn.close()

    print(f"Column '{column_name}' of ID {record_id} has been updated.")

def delete_CRUD(record_id):
    dataset = "titanic_passengersDB"
    table_name = "titanic"

    conn = sqlite3.connect(dataset)
    cursor = conn.cursor()

    query = f"DELETE FROM {table_name} WHERE id = ?"  # 예시 쿼리
    cursor.execute(query, (record_id,))

    conn.commit()

    cursor.close()
    conn.close()

    print(f"Record with ID {record_id} has been deleted.")