# Transform .csv file to .db (SQLite) file
import sqlite3
import csv

# Load the .csv file and transform it for SQLite
def load_file(csv_file_path, db_file_path, table_name):
    # SQLite DB 연결
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    
    # 테이블 생성 (이미 존재하는 경우 무시)
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            PassengerId INTEGER,
            Survived INTEGER,
            Pclass INTEGER,
            Name TEXT,
            Sex TEXT,
            Age REAL,
            SibSp INTEGER,
            Parch INTEGER,
            Ticket TEXT,
            Fare INTEGER,
            Cabin TEXT,
            Embarked TEXT
        )
    ''')
    
    # CSV 파일 열기 및 데이터 삽입
    with open(csv_file_path, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # 첫 번째 행은 헤더이므로 건너뜁니다.
        for row in csv_reader:
            cursor.execute(f'''
                INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', tuple(row))
    
    # 변경사항 커밋 및 연결 닫기
    conn.commit()
    conn.close()