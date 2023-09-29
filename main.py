import sqlite3

connection = sqlite3.connect('practice.db')

table = 'CREATE TABLE grade (id integer primary key, name TEXT, surname TEXT, grade integer)'
cursor = connection.cursor()
cursor.execute(table)

connection.commit()