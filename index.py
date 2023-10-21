import sqlite3

#Create conection to DB

conn= sqlite3.connect('database.db')
cursor= conn.cursor()