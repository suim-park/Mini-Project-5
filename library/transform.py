# Transform .csv file to .db (SQLite) file
import sqlite3
import csv
import os

# Load the .csv file and transform it for SQLite
def load_file(dataset="/Data/titanic.csv"):
    print(os.getcwd())
    titanic_load = csv.reader(open(dataset, newline=''), delimiter=',')
    conn = sqlite3.connect('titanic_passengersDB.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS titanic_passengersDB")
    c.execute("CREATE TABLE GroceryDB (PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked)")
    #insert
    c.executemany("INSERT INTO titanic_passengersDB VALUES (? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", titanic_load)
    conn.commit()
    conn.close()
    return "titanic_passengersDB.db"