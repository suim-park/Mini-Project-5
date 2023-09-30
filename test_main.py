# Test main.py
from library.extract import extract_file
from library.transform import load_file
from library.query import create_CRUD, read_CRUD, update_CRUD, delete_CRUD

import sqlite3
import csv
import os


def test_extract_file():
    # 테스트 데이터를 다운로드할 임시 경로 설정
    temp_file_path = "Data/test_titanic.csv"

    # extract_file 함수를 호출하여 파일 다운로드
    result = extract_file(url="https://github.com/datasciencedojo/datasets/raw/master/titanic.csv", file_path=temp_file_path, save_folder="Data")

    # 파일이 성공적으로 다운로드되었는지 확인
    assert os.path.exists(result)

    # 다운로드한 파일 삭제 (테스트 이후 정리)
    os.remove(result)

def test_load_file():
    test_csv_file = "test.csv"
    with open(test_csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "PassengerId", "Survived", "Pclass", "Name", "Sex",
            "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"
        ])
        # 데이터 행
        writer.writerow([
            893, 0, 3, "Braund, Mr. Owen Harris", "male", 22, 1, 0, "A/5 21171", 7.25, "", "S"
        ])
    
    # 테스트용 DB 파일 경로
    test_db_file = "test_db.db"
    
    # CSV 파일을 DB로 로드
    load_file(test_csv_file, test_db_file, "test_table")
    
    # DB에서 데이터 확인
    conn = sqlite3.connect(test_db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM test_table")
    count = cursor.fetchone()[0]
    conn.close()
    
    # 예상된 데이터 행 수와 실제 데이터 행 수 비교
    assert count == 1

def test_create_CRUD():
    data = (893, 1, 3, "John, Mr. Doe", "male", 25, 0, 0, "12345", 7.25, "", "S")
    create_CRUD(data)

    # Connect to the database and check if the data was inserted
    conn = sqlite3.connect("titanic_passengersDB")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM titanic WHERE PassengerId = 893")
    result = cursor.fetchone()

    assert result == data

    # Clean up by deleting the inserted data
    cursor.execute("DELETE FROM titanic WHERE PassengerId = 893")
    conn.commit()
    conn.close()

def test_read_CRUD():
    test_data = (1, 0, 3, "Braund, Mr. Owen Harris", "male", 22, 1, 0, "A/5 21171", 7.25, "", "S")
    create_CRUD(test_data)
    result = read_CRUD()

    # Check if the result is a list (assuming it contains multiple rows)
    assert isinstance(result, list)
    
    # Check if the result is not empty
    assert len(result) > 0

def test_update_CRUD():
    # Insert test data
    test_data = (892, 1, 1, "Rose, Miss. DeWitt Bukater", "female", 19, 0, 1, 12, 100, 2, "Q")
    create_CRUD(test_data)

    # Call the update_CRUD function to update a specific column
    record_id = 892
    column_name = "Age"
    new_value = 18

    update_CRUD(record_id, column_name, new_value)
    new_database = read_CRUD()

    assert new_database == (892, 1, 1, "Rose, Miss. DeWitt Bukater", "female", 18, 0, 1, 12, 100, 2, "Q")

def test_delete_CRUD():
    # Insert test data
    test_data = (893, 1, 3, "Bob, Mr. Johnson", "male", 28, 0, 0, "67890", 9.0, "", "S")
    create_CRUD(test_data)

    # Call the delete_CRUD function to delete a record
    record_id = 893
    delete_CRUD(record_id)

    # Connect to the database and check if the record was deleted
    conn = sqlite3.connect("titanic_passengersDB")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM titanic WHERE PassengerId = ?", (record_id,))
    result = cursor.fetchone()

    # Check if the result is None, indicating the record was deleted
    assert result is None

if __name__ == "__main__":
    test_extract_file()
    test_load_file()
    test_create_CRUD()
    test_read_CRUD()
    test_update_CRUD()
    test_delete_CRUD()
