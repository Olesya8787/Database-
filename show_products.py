import sqlite3

connection =  sqlite3.connect("jewelry store.db")

def show_products(connection):
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM products_discount""")
        result = cursor.fetchall()
        return result