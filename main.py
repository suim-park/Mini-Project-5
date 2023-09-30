# ETL-Query script
import sqlite3
from library.extract import extract
from library.transform import load_file
from library.query import create_CRUD, read_CRUD, update_CRUD, delete_CRUD, capture_screenshot

database_path = "mydatabase.db"  # 데이터베이스 파일 경로
table_name = "mytable"

# Extract .csv file
extract(url="https://github.com/datasciencedojo/datasets/blob/master/titanic.csv",
        file_path="Data/titanic.csv", save_folder="Data")

# Transform .csv file to .db file
load_file(dataset="/Data/titanic.csv")

# Create from CRUD
create_CRUD(892, 1, 1, "Rose, Miss. DeWitt Bukater", "female", 19, 0, 1, 12, 100, 2, "Q")

# Read from CRUD
read_CRUD()

# update from CRUD
update_CRUD(892, "Age", 18)

# delete from CRUD
delete_CRUD(892)

# save the database operation as screenshot
capture_screenshot("screenshot/operation.png")