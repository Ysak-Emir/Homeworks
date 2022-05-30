import sqlite3
from sqlite3 import Error

database = r'hw.db'


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error:
        print(Error)
    return conn


def create_table(conn, sql_to_create_table):
    try:
        c = conn.cursor()
        c.execute(sql_to_create_table)
        return conn
    except Error:
        print(Error)


conn = create_connection(database)

sql_to_create_table = '''
CREATE TABLE products 
(id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0,
)'''


def create_product(conn, product):
    sql = '''INSERT INTO product (product_name, product_title, price, quantity) 
        VALUES (?, ?, ?, ?)'''
    try:
        c = conn.cursor()
        c.execute(sql, product)
        conn.commit()
        return c.lastrowid
    except Error as e:
        print(e)
    return None


def update_quantity(conn, product):
    sql = '''UPDATE product SET quantity = ? WHERE id = ?'''
    try:
        c = conn.cursor()
        c.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)


def update_price(conn, product):
    sql = '''UPDATE product SET price = ? WHERE id = ?'''
    try:
        c = conn.cursor()
        c.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)


def select_all_products(conn, rows):
    sql = '''SELECT * FROM product'''
    try:
        c = conn.cursor()
        c.execute(sql)
        rows = c.fetchall()

        for r in rows:
            print(r)
    except Error as e:
        print(e)


def select_product_val(conn, limit_for_price, limit_for_quantity):
    sql = '''SELECT * FROM product WHERE price <= ? and quantity <= ?'''
    try:
        c = conn.cursor()
        c.execute(sql, (limit_for_price, limit_for_quantity))
        rows = c.fetchall()

        for r in rows:
            print(r)
    except Error as e:
        print(e)


def search_product(conn, product_name):
    sql = '''SELECT * FROM product WHERE product_name like ?'''
    try:
        c = conn.cursor()
        c.execute(sql, [product_name])
        rows = c.fetchall()

        for r in rows:
            print(r)
    except Error as e:
        print(e)


def delete_product(conn, id):
    sql = '''DELETE FROM product WHERE id = ?'''
    try:
        c = conn.cursor()
        c.execute(sql, (id,))
        conn.commit()
    except Error as e:
        print(e)

if conn is not None:
    print('Connected Successfully')
    # create_table(conn, sql_create_table_product)
    # create_product(conn, ("Aple", "fruits", 80.5, 20))