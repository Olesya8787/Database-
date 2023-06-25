import sqlite3

connection =  sqlite3.connect("jewelry store.db")

def insert_new_customer(connection, values):
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO customers( name, surname, money, customer_cod) VALUES(?,?,?,?)""", values)
        connection.commit()     