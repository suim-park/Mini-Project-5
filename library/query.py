# Query the database
import sqlite3

def create_CRUD(data):
    dataset = "titanic_passengersDB"
    table_name = "titanic"
    
    conn = sqlite3.connect(dataset)
    cursor = conn.cursor()

    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked)")

    query = f"INSERT INTO {table_name} VALUES (? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(query, data)

    conn.commit()
    conn.close()

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
    dataset = "titanic_passengersDB.db"
    table_name = "titanic"

    conn = sqlite3.connect(dataset)
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (PassengerId INT, Survived INT, Pclass INT, Name TEXT, Sex TEXT, Age INT, SibSp INT, Parch INT, Ticket TEXT, Fare REAL, Cabin TEXT, Embarked TEXT)")

    # Create a dynamic SQL query to update the specified column for a record
    query = f"UPDATE {table_name} SET {column_name}=? WHERE PassengerId=?"
    cursor.execute(query, (new_value, record_id))

    conn.commit()
    conn.close()

def delete_CRUD(record_id):
    dataset = "titanic_passengersDB"
    table_name = "titanic"

    conn = sqlite3.connect(dataset)
    cursor = conn.cursor()

    query = f"DELETE FROM {table_name} WHERE PassengerId = ?"  # 예시 쿼리
    cursor.execute(query, (record_id,))

    conn.commit()

    cursor.close()
    conn.close()

    print(f"Record with ID {record_id} has been deleted.")