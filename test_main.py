# Test main.py
from extract import extract
from transform import load_file
from query import create_CRUD, read_CRUD, update_CRUD, delete_CRUD, capture_screenshot

import sqlite3
import os


def test_extract():
    # Clean up by removing the downloaded file
    file_path = "Data/titanic.csv"
    if os.path.exists(file_path):
        os.remove(file_path)
    assert os.path.exists("Data/titanic.db")

def test_transform():
    # Define the path to the test CSV file
    dataset = "Data/titanic.csv"

    # Remove the database file if it exists to start fresh
    db_file = "titanic_passengersDB.db"
    if os.path.exists(db_file):
        os.remove(db_file)

    # Call the load_file function to load data into a database
    result = load_file(dataset)

    # Check if the database file was created
    assert os.path.exists(db_file)

    # Check if the result is the name of the created database file
    assert result == db_file

def test_create_CRUD():
    data = (893, 1, 3, "John, Mr. Doe", "male", 25, 0, 0, "12345", 7.25, 35, "S")
    create_CRUD(data)

    # Connect to the database and check if the data was inserted
    conn = sqlite3.connect("titanic_passengersDB")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM titanic WHERE id = 893")
    result = cursor.fetchone()

    assert result == data

    # Clean up by deleting the inserted data
    cursor.execute("DELETE FROM titanic WHERE id = 893")
    conn.commit()
    conn.close()

def test_read_CRUD():
    result = read_CRUD()

    # Check if the result is a list (assuming it contains multiple rows)
    assert isinstance(result, list)
    
    # Check if the result is not empty
    assert len(result) > 0

def test_update_CRUD():
    # Insert test data
    test_data = (893, 1, 3, "Jane, Miss. Smith", "female", 30, 0, 0, "54321", 8.0, 58, "C")
    create_CRUD(test_data)

    # Call the update_CRUD function to update a specific column
    record_id = 893
    column_name = "Age"
    new_value = 35
    update_CRUD(record_id, column_name, new_value)

    # Connect to the database and check if the data was updated
    conn = sqlite3.connect("titanic_passengersDB")
    cursor = conn.cursor()
    cursor.execute(f"SELECT {column_name} FROM titanic WHERE id = ?", (record_id,))
    result = cursor.fetchone()[0]

    # Check if the updated value matches the new value
    assert result == new_value

    # Clean up by deleting the inserted data
    cursor.execute("DELETE FROM titanic WHERE id = 893")
    conn.commit()
    conn.close()

def test_delete_CRUD():
    # Insert test data
    test_data = (893, 1, 3, "Bob, Mr. Johnson", "male", 28, 0, 0, "67890", 9.0, 50, "S")
    create_CRUD(test_data)

    # Call the delete_CRUD function to delete a record
    record_id = 893
    delete_CRUD(record_id)

    # Connect to the database and check if the record was deleted
    conn = sqlite3.connect("titanic_passengersDB")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM titanic WHERE id = ?", (record_id,))
    result = cursor.fetchone()

    # Check if the result is None, indicating the record was deleted
    assert result is None

def test_capture_screenshot():
    # Define a test file path for the screenshot
    file_path = "test_screenshot.png"

    # Call the capture_screenshot function to capture a screenshot
    capture_screenshot(file_path)

    # Check if the screenshot file exists
    assert os.path.exists(file_path)

    # Clean up by deleting the screenshot file
    os.remove(file_path)

if __name__ == "__main__":
    test_create_CRUD()
    test_read_CRUD()
    test_update_CRUD()
    test_delete_CRUD()
    test_capture_screenshot()
