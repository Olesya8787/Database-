import sqlite3
from insert_new_product import insert_new_product
from insert_new_customer import insert_new_customer
from show_products import show_products

connection = sqlite3.connect("jewelry store.db")
cursor = connection.cursor()

cursor.execute ("""
    CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY AUTOINCREMENT, label TEXT, price INT)
""")
                
products =[
    ( "Eternal Love Bracelet", 225),
    ( "Infinity Bracelet", 290),
    ( "Reflection Ring", 1200),
    ( "Classic Ring", 900),
    ( "Bold Pearl Drop Earrings", 800),
    ( "Marquise Topaz Earrings", 1300)
]         
# cursor.executemany("""
#   INSERT INTO products( label, price)
#   VALUES (?,?)
# """, products)  


cursor.execute ("""
    CREATE TABLE IF NOT EXISTS products_discount(id INTEGER PRIMARY KEY AUTOINCREMENT , label TEXT, price INT, discount INT)
""")
products_discount =[                
    ("Eternal Love Bracelet", 225, 20),
    ("Infinity Bracelet", 290, 20),
    ("Reflection Ring", 1200, 30),
    ( "Classic Ring", 900, 30),
    ("Bold Pearl Drop Earrings", 800, 15),
]              
# cursor.executemany("""
#   INSERT INTO products_discount(label, price, discount)
#   VALUES (?,?,?)
# """, products_discount)      

cursor.execute ("""
    CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, surname TEXT, money REAL, customer_cod INT)
""")
customers = [
    ("Ann", "Lewis", 15000, 23109),
    ("Mia", "Wood", 9000, 15098),
    ("William", "Haal", 20000, 67345),
    ("Eliza", "Smith", 8000, 16098),
    ("David", "Taylor", 8900, 24109),
    ("Harry", "White", 25550, 17098)
]                               
# cursor.executemany("""
#   INSERT INTO customers(name, surname, money, customer_cod)
#   VALUES (?,?,?,?)
# """, customers) 



cursor.execute ("""                
    CREATE TABLE IF NOT EXISTS card(product TEXT PRIMARY KEY, owner)
""")
                               
connection.commit()
print(connection)


is_running = True

while is_running :
    choose_action = input("""
        1) Add new product
        2) Add new customer
        3) Products catalog
        4)  Exit
     Answer : """.lower()    
    ) 

    if choose_action == "1" :
        print(" \f Add new products ")
        label = input("Enter products label : ")
        price  = input("Enter products price : ")
        values = ( label, price)
        insert_new_product(connection, values)

    elif  choose_action == "2" :
        print(" \f Add new customer ") 
        name = input("Enter your name : ")
        surname = input("Enter your surname : ")
        money = input("How much money do you have : ")
        customer_cod = input("Enter your customer_cod : ")
        values = ( name, surname, money, customer_cod)
        insert_new_customer(connection, values)

    elif  choose_action == "3":
        print(" \f Show products " )
        result =  show_products(connection)
        print(result) 
        
    elif choose_action == "4" :
        is_running = False      