import sqlite3

connection =  sqlite3.connect("jewelry store.db")

def insert_new_product(connection, values):
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO products( label, price) VALUES(?,?)""", values)
        connection.commit()     