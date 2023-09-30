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

def update_CRUD(record_id, column_name, data):
    dataset = "titanic_passengersDB"
    table_name = "titanic"

    conn = sqlite3.connect(dataset)
    cursor = conn.cursor()

    query = f"UPDATE {table_name} SET Survived=?, Pclass=?, Name=?, Sex=?, Age=?, SibSp=?, Parch=?, Ticket=?, Fare=?, Cabin=?, Embarked=? WHERE PassengerId=?"
    cursor.execute(query, (data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[0]))
    
    conn.commit()

    cursor.close()
    conn.close()

    print(f"Column '{column_name}' of ID {record_id} has been updated.")

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