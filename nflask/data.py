import sqlite3
con=sqlite3.connect('database.db')
print('successsfull')
con.execute('CREATE TABLE book(name char(30),author char(30),pdf char(30));')
print("successfully ")
con.close()